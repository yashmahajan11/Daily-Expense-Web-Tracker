from flask import Flask,render_template,redirect,request,session,url_for,flash
import pymysql
import os


servername="localhost"
username="root"
password=""
dbname="webexpense"

app = Flask(__name__)
app.secret_key=os.urandom(24)


db=pymysql.connect(servername,username,password,dbname)
c=db.cursor()




# <--------------------------------Index------------------------------------->


@app.route("/", methods = ['GET','POST'])

def index():
    if 'user_id' in session:
        return render_template('home.html')
    else: 
        if(request.method == 'POST'):
            name = request.form.get('Name')
            email = request.form.get('email')
            tele = request.form.get('number')
            message = request.form.get('message')

            query="INSERT INTO contact(id,name,email,telephone,message) VALUES (NULL,'{}','{}','{}','{}')".format(name,email,tele,message)
            res=c.execute(query)
            db.commit()

            flash("Thank you for your valuable time!! We will get back to you soon.")

            return redirect('/')
         
        return render_template('index.html')





# <-------------------------------- Login ------------------------------------->

@app.route("/login", methods = ['GET','POST'])

def login():
    fullname = request.form.get('fullName')
    username = request.form.get('userName')
    password = request.form.get('pwd')

    query="SELECT * FROM user WHERE username = '{}' and password = '{}'".format(username,password)
    c.execute(query)
    res=c.fetchall()
    
    if len(res)>0:
        
        session['user_id']=res[0][0]
        session['username']=username
        session['fullname']=res[0][1]
        
        return redirect('/home')
    else:
        return render_template('login.html')




# <-------------------------------- Register ------------------------------------->


@app.route("/register", methods = ['GET','POST'])

def addUser():
        if 'user_id' in session:
            return redirect('/')

        if (request.method == 'POST'):
            fname = request.form.get('fullName')
            email = request.form.get('email')
            contact = request.form.get('phoneNo')
            username = request.form.get('userName')
            password = request.form.get('pwd')


            query="INSERT INTO user(user_id,fullname,email,phone_no,username,password) VALUES (NULL,'{}','{}','{}','{}','{}')".format(fname,email,contact,username,password)
            res=c.execute(query)
            db.commit()

            c.execute("SELECT * FROM user WHERE username = '{}'".format(username))
            my_user=c.fetchall()
            session['user_id']=my_user[0][0]
            session['username']=username
            session['fullname']=my_user[0][1]
            
            return redirect('/home')

        return render_template('register.html')



# <-------------------------------- Home ------------------------------------->

@app.route("/home")

def home():
    if 'user_id' in session:

        fname = request.form.get('fullName')
        user = session['fullname']

        query="select * from expense where fullname = '{}' ".format(user)
        c.execute(query)
        res=c.fetchall()

        totalExpense=0
        for i in res:
            totalExpense=totalExpense+i[1]
        

        query1="select * from income where fullname = '{}' ".format(user)
        
        c.execute(query1)
        res1=c.fetchall()
        
        totalIncome=0
        for x in res1:
            totalIncome=totalIncome+x[1]

        totalBalance=totalIncome-totalExpense

        totBal="{:,}".format(totalBalance)

        return render_template('home.html',totalBal=totBal)       
    else:
        return redirect('/')





# <-------------------------------- Logout ------------------------------------->


@app.route("/logout")
def logout():
    session.pop('user_id')
    return redirect('/')

        



# <-------------------------------- Add Income ------------------------------------->


@app.route("/addIncome", methods = ['GET','POST'])

def addIncome():
    if 'user_id' in session:
        if (request.method == 'POST'):
            income = int(request.form.get('income'))
            incometype = request.form.get('incomeType')
            incomedate = request.form.get('incomeDate')
            description = request.form.get('desc')
            fname = request.form.get('fullName')

            query="INSERT INTO income(i_id,income,incomeType,incomeDate,description,fullname) VALUES (NULL,'{}','{}','{}','{}','{}')".format(income,incometype,incomedate,description,session['fullname'])

            if income<=0:
                flash("You can't enter zero or negative amount! Please enter your amount again.")
                return redirect('/addIncome')


            else:
                res=c.execute(query)
                db.commit()
                return redirect('/incomeList')

        return render_template('addIncome.html')

    else:
        return redirect('/login')



# <-------------------------------- Income List ------------------------------------->


@app.route("/incomeList", methods = ['GET','POST'])
def incomeList():
    if 'user_id' in session:

        incomedate = request.form.get('incomeDate')
        fname = request.form.get('fullName')
        user = session['fullname']

        query="select * from income where fullname = '{}' order by incomeDate desc".format(user)
        
        c.execute(query)
        res=c.fetchall()
        
        totalIncome=0
        for x in res:
            totalIncome=totalIncome+x[1]

        totInc="{:,}".format(totalIncome)

        return render_template('incomeList.html',res=res,IncBal=totInc)

    else:
        return redirect('/login')




# <-------------------------------- Edit Income List ------------------------------------->


@app.route('/edit/<string:id_data>',methods = ['GET','POST'])

def get_data(id_data):
    c.execute("SELECT * FROM income WHERE i_id='{}'".format(id_data))
    data=c.fetchall()
    return render_template('edit.html',id_data=id_data,add=data[0])


@app.route('/update/<string:id_data>',methods=['GET','POST'])
def edit(id_data):
    if (request.method=='POST'):
        income = request.form.get('income')
        incometype = request.form.get('incomeType')
        incomedate = request.form.get('incomeDate')
        description = request.form.get('desc')
        fname = request.form.get('fullName')

        c.execute("UPDATE income SET income = '{}' ,incomeType = '{}',incomeDate = '{}',description = '{}',fullname = '{}' WHERE i_id='{}'".format(income,incometype,incomedate,description,session['fullname'],id_data))
        db.commit()
        return redirect('/incomeList')

    else:
        return render_template('edit.html')





# <-------------------------------- Delete Income List ------------------------------------->


@app.route('/delete/<string:id_data>', methods = ['GET'])
def deleteIncome(id_data):
   
    if 'user_id' in session:
        c.execute("DELETE FROM income WHERE i_id='{}'".format(id_data,))
        db.commit()
        return redirect(url_for('incomeList'))

    else:
        return redirect('/login')




    




# <-------------------------------- Add Expense ------------------------------------->


@app.route("/addExpense", methods = ['GET','POST'])
def addExpense():
    if 'user_id' in session:
        if (request.method == 'POST'):
            expense = int(request.form.get('expense'))
            expensetype = request.form.get('expenseType')
            expensedate = request.form.get('expenseDate')
            description = request.form.get('desc1')
            fname = request.form.get('fullName')
        
            queryExp="INSERT INTO expense(e_id,expense,expenseType,expenseDate,description,fullname) VALUES (NULL,'{}','{}','{}','{}','{}')".format(expense,expensetype,expensedate,description,session['fullname'])
            

        
            fname = request.form.get('fullName')
            user = session['fullname']

            query="select * from expense where fullname = '{}' ".format(user)
            c.execute(query)
            res=c.fetchall()

            totalExpense=0
            for i in res:
                totalExpense=totalExpense+i[1]
            
            
            query1="select * from income where fullname = '{}' ".format(user)
            
            c.execute(query1)
            res1=c.fetchall()
            
            totalIncome=0
            for x in res1:
                totalIncome=totalIncome+x[1]

            totalBalance=totalIncome-totalExpense

            totBal="{:,}".format(totalBalance)

            if expense<=0:
                flash("You can't enter zero or negative amount! Please enter your amount again.")
                return redirect('/addExpense')

            elif totalBalance>expense:
                resExp=c.execute(queryExp)
                db.commit()
                return redirect('/expenseList')

            else:
                flash("You have insufficient balance! Please check your balance again.")
                return redirect('/addExpense')

        return render_template('addExpense.html')

    else:
        return redirect('/login')







# <-------------------------------- Expense List ------------------------------------->


@app.route("/expenseList", methods = ['GET','POST'])

def expenseList():
    if 'user_id' in session:
        expensedate = request.form.get('expenseDate')
        fname = request.form.get('fullName')
        user = session['fullname']

        query="select * from expense where fullname = '{}' order by expenseDate desc".format(user)
        c.execute(query)
        res=c.fetchall()

        totalExpense=0
        for i in res:
            totalExpense=totalExpense+i[1]

        totExp="{:,}".format(totalExpense)

        return render_template('expenseList.html',res=res,ExpBal=totExp)

    else:
        return redirect('/login')



# <-------------------------------- Edit Expense List ------------------------------------->


@app.route('/editE/<string:id_data>',methods = ['GET','POST'])

def get_Edata(id_data):
    c.execute("SELECT * FROM expense WHERE e_id='{}'".format(id_data))
    dataE=c.fetchall()
    return render_template('editE.html',id_data=id_data,addE=dataE[0])


@app.route('/updateE/<string:id_data>',methods=['GET','POST'])
def Eedit(id_data):
    if (request.method=='POST'):
        expense = request.form.get('expense')
        expensetype = request.form.get('expenseType')
        expensedate = request.form.get('expenseDate')
        description = request.form.get('desc1')
        fname = request.form.get('fullName')

        c.execute("UPDATE expense SET expense = '{}' ,expenseType = '{}',expenseDate = '{}',description = '{}',fullname = '{}' WHERE e_id='{}'".format(expense,expensetype,expensedate,description,session['fullname'],id_data))
        db.commit()
        return redirect('/expenseList')

    else:
        return render_template('editE.html')






# <-------------------------------- Delete Expense List ------------------------------------->


@app.route('/deleteExp/<string:id_data>', methods = ['GET'])
def deleteExpense(id_data):
   
    c.execute("DELETE FROM expense WHERE e_id='{}'".format(id_data))
    db.commit()
    return redirect(url_for('expenseList'))






# <-------------------------------------- feedback ---------------------------------------------->

@app.route("/feedback",methods =['GET','POST'])

def feedback():
    if 'user_id' in session:
        if(request.method == 'POST'):
            fullname = request.form.get('fullName')
            email = request.form.get('email')
            subject = request.form.get('subject')
            message = request.form.get('message')

            query="INSERT INTO feedback(fullname,email,subject,message) VALUES ('{}','{}','{}','{}')".format(fullname,email,subject,message)
            res=c.execute(query)
            db.commit()

            flash("Thank you for your valuable feedback!!")
            
            return redirect('/feedback')
        return render_template('feedback.html')       
    else:
        return redirect('/login')





if __name__ == "__main__":
    app.run(debug=True)