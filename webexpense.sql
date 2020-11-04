-- phpMyAdmin SQL Dump
-- version 5.0.2
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Nov 04, 2020 at 05:39 AM
-- Server version: 10.4.13-MariaDB
-- PHP Version: 7.4.8

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `webexpense`
--

-- --------------------------------------------------------

--
-- Table structure for table `contact`
--

CREATE TABLE `contact` (
  `id` int(11) NOT NULL,
  `name` text NOT NULL,
  `email` varchar(50) NOT NULL,
  `telephone` varchar(12) NOT NULL,
  `message` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `contact`
--

INSERT INTO `contact` (`id`, `name`, `email`, `telephone`, `message`) VALUES
(1, 'Suraj Lokhande', 'suraj@mail.com', '9869654512', 'I want to get to know about your website.'),
(2, 'Suraj Lokhande', 'suraj@gmail.com', '9865452312', 'I want to get know about your website'),
(3, 'Rahul Roy', 'rahul@gmail.com', '8564751232', 'I want some tips to save money');

-- --------------------------------------------------------

--
-- Table structure for table `expense`
--

CREATE TABLE `expense` (
  `e_id` int(11) NOT NULL,
  `expense` int(11) NOT NULL,
  `expenseType` varchar(32) NOT NULL,
  `expenseDate` date DEFAULT NULL,
  `description` text NOT NULL,
  `fullname` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `expense`
--

INSERT INTO `expense` (`e_id`, `expense`, `expenseType`, `expenseDate`, `description`, `fullname`) VALUES
(1, 7000, 'debit card', '2020-10-10', 'for shopping', 'Yash Mahajan'),
(2, 2000, 'cash', '2020-10-01', 'for grocery', 'Yash Mahajan'),
(3, 800, 'debit card', '2020-10-10', 'Train reservation', 'Yash Mahajan'),
(4, 599, 'gpay', '2020-10-18', 'Mobile recharge', 'Yash Mahajan'),
(5, 3000, 'debit card', '2020-10-27', 'for shoes', 'Yash Mahajan'),
(8, 2000, 'cash', '2020-11-01', 'for grocery', 'Yash Mahajan'),
(9, 500, 'gpay', '2020-10-31', 'for foods', 'Yash Mahajan'),
(10, 2300, 'cash', '2020-11-02', 'for electricity bill', 'Yash Mahajan'),
(11, 70000, 'debit card', '2020-11-03', 'for clothes', 'Sachin Tendulkar'),
(12, 45000, 'visa', '2020-11-04', 'for mobile', 'Sachin Tendulkar');

-- --------------------------------------------------------

--
-- Table structure for table `feedback`
--

CREATE TABLE `feedback` (
  `fullname` text NOT NULL,
  `email` varchar(50) NOT NULL,
  `subject` text NOT NULL,
  `message` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `feedback`
--

INSERT INTO `feedback` (`fullname`, `email`, `subject`, `message`) VALUES
('Yash Mahajan', 'yash@mail.com', 'About App', 'Hi its amazing app. No issues till now. Great work..!!'),
('Yash Mahajan', 'yash@gmail.com', 'About App', 'Good App.It helps me alot..!!'),
('Yash Mahajan', 'yash@mail.com', 'About App', 'great website..!!'),
('Sachin Tendulkar', 'sachin@gmail.com', 'About website', 'Great website');

-- --------------------------------------------------------

--
-- Table structure for table `income`
--

CREATE TABLE `income` (
  `i_id` int(11) NOT NULL,
  `income` int(11) NOT NULL,
  `incomeType` varchar(32) NOT NULL,
  `incomeDate` date DEFAULT NULL,
  `description` text NOT NULL,
  `fullname` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `income`
--

INSERT INTO `income` (`i_id`, `income`, `incomeType`, `incomeDate`, `description`, `fullname`) VALUES
(1, 30000, 'Salary', '2020-10-08', 'from salary', 'Yash Mahajan'),
(2, 20000, 'Salary', '2020-10-18', 'from salary', 'Yash Mahajan'),
(3, 25000, 'Salary', '2020-09-17', 'from salary', 'Yash Mahajan'),
(4, 40000, 'lottery', '2020-10-04', 'from lottery', 'Yash Mahajan'),
(5, 10000, 'cheque', '2020-10-14', 'from relatives', 'Yash Mahajan'),
(10, 30000, 'Salary', '2020-11-01', 'from salary', 'Yash Mahajan'),
(12, 40000, 'cash', '2020-10-01', 'from friends', 'Yash Mahajan'),
(14, 45000, 'cash', '2020-11-03', 'from selling bike', 'Yash Mahajan'),
(15, 500000, 'cheque', '2020-11-01', 'from salary', 'Sachin Tendulkar'),
(16, 2500000, 'cheque', '2020-10-30', 'from ads', 'Sachin Tendulkar');

-- --------------------------------------------------------

--
-- Table structure for table `user`
--

CREATE TABLE `user` (
  `user_id` int(11) NOT NULL,
  `fullname` text NOT NULL,
  `email` varchar(50) NOT NULL,
  `phone_no` varchar(15) NOT NULL,
  `username` varchar(30) NOT NULL,
  `password` varchar(32) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `user`
--

INSERT INTO `user` (`user_id`, `fullname`, `email`, `phone_no`, `username`, `password`) VALUES
(1, 'Yash Mahajan', 'yash@mail.com', '9869563212', 'yash123', 'yash123'),
(2, 'Sachin Tendulkar', 'sachin@gmail.com', '7898684512', 'sachin123', 'sachin123');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `contact`
--
ALTER TABLE `contact`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `expense`
--
ALTER TABLE `expense`
  ADD PRIMARY KEY (`e_id`);

--
-- Indexes for table `income`
--
ALTER TABLE `income`
  ADD PRIMARY KEY (`i_id`);

--
-- Indexes for table `user`
--
ALTER TABLE `user`
  ADD PRIMARY KEY (`user_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `contact`
--
ALTER TABLE `contact`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `expense`
--
ALTER TABLE `expense`
  MODIFY `e_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=13;

--
-- AUTO_INCREMENT for table `income`
--
ALTER TABLE `income`
  MODIFY `i_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=17;

--
-- AUTO_INCREMENT for table `user`
--
ALTER TABLE `user`
  MODIFY `user_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
