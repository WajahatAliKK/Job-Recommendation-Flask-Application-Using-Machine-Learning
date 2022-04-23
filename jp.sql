-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jul 31, 2021 at 08:12 AM
-- Server version: 10.4.20-MariaDB
-- PHP Version: 7.4.21

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `jp`
--

-- --------------------------------------------------------

--
-- Table structure for table `comp_p`
--

CREATE TABLE `comp_p` (
  `CID` int(11) NOT NULL,
  `Comp_Name` varchar(255) NOT NULL,
  `Comp_Email` varchar(255) NOT NULL,
  `Comp_Address` varchar(500) NOT NULL,
  `Comp_Type` varchar(255) NOT NULL,
  `Comp_Phone` varchar(255) NOT NULL,
  `Comp_Mobile` varchar(255) NOT NULL,
  `ZipCode` int(11) NOT NULL,
  `Img` varchar(535) NOT NULL,
  `Terms` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `comp_p`
--

INSERT INTO `comp_p` (`CID`, `Comp_Name`, `Comp_Email`, `Comp_Address`, `Comp_Type`, `Comp_Phone`, `Comp_Mobile`, `ZipCode`, `Img`, `Terms`) VALUES
(1, 'Bits&Bytes', 'bits&bytes@gmail.com', 'adjaskljasklfasklf', 'It Business', '03001234567', '03001234567', 71900, '', 'Yes');

-- --------------------------------------------------------

--
-- Table structure for table `jobs`
--

CREATE TABLE `jobs` (
  `JID` int(11) NOT NULL,
  `Jtitle` varchar(255) NOT NULL,
  `Jlocation` varchar(255) NOT NULL,
  `Jexperience` varchar(255) NOT NULL,
  `Deadline_Date` date NOT NULL,
  `Salayfrom` int(11) NOT NULL,
  `Salaryto` int(11) NOT NULL,
  `Designation` varchar(255) NOT NULL,
  `Statement` varchar(255) NOT NULL,
  `Quiz` varchar(65) NOT NULL,
  `Description` varchar(535) NOT NULL,
  `Posted_By` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `jobs`
--

INSERT INTO `jobs` (`JID`, `Jtitle`, `Jlocation`, `Jexperience`, `Deadline_Date`, `Salayfrom`, `Salaryto`, `Designation`, `Statement`, `Quiz`, `Description`, `Posted_By`) VALUES
(1, 'Python', 'Karachi', '3 Years', '2021-07-10', 100000, 150000, 'It Bussiness', 'no', 'yes', 'This is a test statment', 'Aqib'),
(26, 'Ruby', 'Lahore', '3 Years', '2021-06-30', 60000, 80000, 'It Bussiness', 'no', 'yes', 'You should have experience in Machine Learning(ML) as well as hands-on experience in Data science&nbsp;', 'Aqib'),
(27, 'Graphic Designer', 'Lahore', '3 Years', '2021-08-07', 80000, 100000, 'It Bussiness', 'yes', 'no', 'assadksadkjasd', 'Aqib');

-- --------------------------------------------------------

--
-- Table structure for table `jobs_applied`
--

CREATE TABLE `jobs_applied` (
  `ID` int(11) NOT NULL,
  `UID` int(11) NOT NULL,
  `JID` int(11) NOT NULL,
  `Fname` varchar(255) NOT NULL,
  `email` varchar(255) NOT NULL,
  `Job_title` varchar(255) NOT NULL,
  `Description` text NOT NULL,
  `Quiz_Score` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `jobs_applied`
--

INSERT INTO `jobs_applied` (`ID`, `UID`, `JID`, `Fname`, `email`, `Job_title`, `Description`, `Quiz_Score`) VALUES
(8, 5, 1, 'Test User', 'check@gmail.com', 'Python', 'asdsasafasfa', 3),
(9, 5, 26, 'Test User', 'check@gmail.com', 'Ruby', 'It is a test description', 3);

-- --------------------------------------------------------

--
-- Table structure for table `user`
--

CREATE TABLE `user` (
  `ID` int(11) NOT NULL,
  `fname` varchar(255) NOT NULL,
  `lname` varchar(255) NOT NULL,
  `email` varchar(255) NOT NULL,
  `phone` varchar(255) NOT NULL,
  `pass` varchar(255) NOT NULL,
  `dob` date NOT NULL,
  `role` varchar(255) NOT NULL,
  `Profile_Completion` varchar(65) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `user`
--

INSERT INTO `user` (`ID`, `fname`, `lname`, `email`, `phone`, `pass`, `dob`, `role`, `Profile_Completion`) VALUES
(1, 'MARC', 'Chishti', 'abdulrehmanchishti22@gmail.com', '03314581488', '1234567', '2021-06-23', 'user', ''),
(3, 'Aqib', 'Sheikh', 'XXQIB1234@gmail.com', '03213323123', '12345678', '2021-06-08', 'company', ''),
(5, 'Test', 'User', 'CHECK@gmail.com', '03331234567', '123456', '2021-07-13', 'user', '');

-- --------------------------------------------------------

--
-- Table structure for table `user_p`
--

CREATE TABLE `user_p` (
  `ID` int(11) NOT NULL,
  `UID` int(11) NOT NULL,
  `city` varchar(255) NOT NULL,
  `gender` varchar(255) NOT NULL,
  `Prof_Info` varchar(255) NOT NULL,
  `Experience` varchar(255) NOT NULL,
  `Skill_Recommended` varchar(255) DEFAULT NULL,
  `img` varchar(255) NOT NULL,
  `Term` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `user_p`
--

INSERT INTO `user_p` (`ID`, `UID`, `city`, `gender`, `Prof_Info`, `Experience`, `Skill_Recommended`, `img`, `Term`) VALUES
(1, 1, 'Lahore', 'Male', 'Python Developer', 'Less then 1 year', '[\'Software Developer\']', '', 'yes'),
(5, 5, 'Lahore', 'Male', 'Python Developer', 'Less then 1 year', '[\'UX Designer\']', '', 'yes');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `comp_p`
--
ALTER TABLE `comp_p`
  ADD PRIMARY KEY (`CID`),
  ADD UNIQUE KEY `Comp_Email` (`Comp_Email`),
  ADD UNIQUE KEY `Comp_Phone` (`Comp_Phone`);

--
-- Indexes for table `jobs`
--
ALTER TABLE `jobs`
  ADD PRIMARY KEY (`JID`);

--
-- Indexes for table `jobs_applied`
--
ALTER TABLE `jobs_applied`
  ADD PRIMARY KEY (`ID`);

--
-- Indexes for table `user`
--
ALTER TABLE `user`
  ADD PRIMARY KEY (`ID`),
  ADD UNIQUE KEY `email` (`email`),
  ADD UNIQUE KEY `email_2` (`email`),
  ADD KEY `email_3` (`email`);

--
-- Indexes for table `user_p`
--
ALTER TABLE `user_p`
  ADD PRIMARY KEY (`ID`),
  ADD KEY `ForeignKey` (`UID`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `comp_p`
--
ALTER TABLE `comp_p`
  MODIFY `CID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `jobs`
--
ALTER TABLE `jobs`
  MODIFY `JID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=28;

--
-- AUTO_INCREMENT for table `jobs_applied`
--
ALTER TABLE `jobs_applied`
  MODIFY `ID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;

--
-- AUTO_INCREMENT for table `user`
--
ALTER TABLE `user`
  MODIFY `ID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT for table `user_p`
--
ALTER TABLE `user_p`
  MODIFY `ID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `user_p`
--
ALTER TABLE `user_p`
  ADD CONSTRAINT `ForeignKey` FOREIGN KEY (`UID`) REFERENCES `user_p` (`ID`) ON DELETE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
