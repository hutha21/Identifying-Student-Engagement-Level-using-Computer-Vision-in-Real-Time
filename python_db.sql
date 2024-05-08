-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: May 08, 2024 at 07:50 PM
-- Server version: 10.4.25-MariaDB
-- PHP Version: 8.1.10

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `python_db`
--

-- --------------------------------------------------------

--
-- Table structure for table `login_lecturer`
--

CREATE TABLE `login_lecturer` (
  `no` int(11) NOT NULL,
  `username` varchar(200) NOT NULL,
  `password` varchar(200) NOT NULL,
  `name` varchar(200) NOT NULL,
  `id` varchar(200) NOT NULL,
  `email` varchar(200) NOT NULL,
  `phone_no` varchar(200) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `login_lecturer`
--

INSERT INTO `login_lecturer` (`no`, `username`, `password`, `name`, `id`, `email`, `phone_no`) VALUES
(1, 'admin', 'admin', 'Sham', '1123', 'sham@gmail.com', '0127725679'),
(2, 'sara', 'sara', 'Sarah', '1122', 'sarah@gmail.com', '01627802315'),
(3, 'ryan', 'ryan', 'Ryan ', '3322', 'ryan@gmail.com', '0142255789');

-- --------------------------------------------------------

--
-- Table structure for table `login_student`
--

CREATE TABLE `login_student` (
  `no` int(11) NOT NULL,
  `username` varchar(200) NOT NULL,
  `password` varchar(200) NOT NULL,
  `name` varchar(200) NOT NULL,
  `id` varchar(200) NOT NULL,
  `email` varchar(200) NOT NULL,
  `phone_no` varchar(200) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `login_student`
--

INSERT INTO `login_student` (`no`, `username`, `password`, `name`, `id`, `email`, `phone_no`) VALUES
(1, 'test', 'test', 'Hutha', '9311', 'hutha@gmail.com', '01126901415'),
(2, 'test2', 'test2', 'Faris2', '1192', 'faris@gmail.com', '60189126118'),
(3, 'john', 'password', 'John Dow', '2235', 'joh@gmail.com', '0123148141'),
(4, 'verr', 'verr1', 'Verrmen', '1399', 'verrmen@gmail.com', '0169488663');

-- --------------------------------------------------------

--
-- Table structure for table `student_engagement_level`
--

CREATE TABLE `student_engagement_level` (
  `no` int(11) NOT NULL,
  `student_id` varchar(200) NOT NULL,
  `student_name` varchar(200) NOT NULL,
  `lost_engagement_time` varchar(200) NOT NULL,
  `engagement_time` varchar(200) NOT NULL,
  `average_engagement` varchar(200) NOT NULL,
  `engagement_status` varchar(200) NOT NULL,
  `timestamp` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `student_engagement_level`
--

INSERT INTO `student_engagement_level` (`no`, `student_id`, `student_name`, `lost_engagement_time`, `engagement_time`, `average_engagement`, `engagement_status`, `timestamp`) VALUES
(15, '9311', 'Hutha', '6', '20', '77', 'Engage', '2022-11-16 19:18:19'),
(16, '9311', 'Hutha', '23', '119', '84', 'Engage', '2022-11-16 19:21:52'),
(17, '9311', 'Hutha', '40', '7', '15', 'Disengage', '2022-11-16 19:31:04'),
(18, '2235', 'John Dow', '24', '26', '52', 'Disengage', '2022-11-16 19:33:32'),
(19, '1399', 'Verrmen', '9', '28', '76', 'Engage', '2022-11-16 19:35:20'),
(20, '1399', 'Verrmen', '4', '35', '90', 'Engage', '2022-11-16 19:36:44'),
(21, '9311', 'Hutha', '6', '21', '78', 'Engage', '2022-12-07 08:39:05'),
(22, '9311', 'Hutha', '8', '28', '78', 'Engage', '2022-12-07 08:56:31'),
(23, '9311', 'Hutha', '5', '14', '74', 'Engage', '2022-12-07 09:20:53'),
(24, '9311', 'Hutha', '0', '39', '100', 'Engage', '2022-12-08 14:03:06');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `login_lecturer`
--
ALTER TABLE `login_lecturer`
  ADD PRIMARY KEY (`no`);

--
-- Indexes for table `login_student`
--
ALTER TABLE `login_student`
  ADD PRIMARY KEY (`no`);

--
-- Indexes for table `student_engagement_level`
--
ALTER TABLE `student_engagement_level`
  ADD PRIMARY KEY (`no`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `login_lecturer`
--
ALTER TABLE `login_lecturer`
  MODIFY `no` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `login_student`
--
ALTER TABLE `login_student`
  MODIFY `no` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `student_engagement_level`
--
ALTER TABLE `student_engagement_level`
  MODIFY `no` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=25;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
