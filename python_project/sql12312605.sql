-- phpMyAdmin SQL Dump
-- version 4.7.1
-- https://www.phpmyadmin.net/
--
-- Host: sql12.freemysqlhosting.net
-- Generation Time: Nov 22, 2019 at 05:23 PM
-- Server version: 5.5.58-0ubuntu0.14.04.1
-- PHP Version: 7.0.33-0ubuntu0.16.04.3

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `sql12312605`
--

-- --------------------------------------------------------

--
-- Table structure for table `category`
--

CREATE TABLE `category` (
  `id` int(10) NOT NULL,
  `name` varchar(250) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `category`
--

INSERT INTO `category` (`id`, `name`) VALUES
(1, 'الإضاءات المنزلية'),
(3, 'إضاءات الحفلات'),
(4, 'الأجهزة المضيئة');

-- --------------------------------------------------------

--
-- Table structure for table `orders`
--

CREATE TABLE `orders` (
  `id` int(11) NOT NULL,
  `order_date` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `orders`
--

INSERT INTO `orders` (`id`, `order_date`) VALUES
(21, '2019-11-22'),
(22, '2019-11-22'),
(23, '2019-11-22'),
(24, '2019-11-22');

-- --------------------------------------------------------

--
-- Table structure for table `order_item`
--

CREATE TABLE `order_item` (
  `id` int(11) NOT NULL,
  `order_id` int(11) NOT NULL,
  `product_id` int(11) NOT NULL,
  `quantity` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `order_item`
--

INSERT INTO `order_item` (`id`, `order_id`, `product_id`, `quantity`) VALUES
(19, 21, 76, 1),
(20, 21, 90, 2),
(21, 23, 64, 2),
(22, 24, 79, 2),
(23, 24, 62, 2);

-- --------------------------------------------------------

--
-- Stand-in structure for view `order_view`
-- (See below for the actual view)
--
CREATE TABLE `order_view` (
`product_id` int(11)
,`product_name` varchar(250)
,`subcategory_name` varchar(250)
,`category_name` varchar(250)
,`price` decimal(10,0)
);

-- --------------------------------------------------------

--
-- Table structure for table `product_item`
--

CREATE TABLE `product_item` (
  `id` int(11) NOT NULL,
  `sub_cat_id` int(11) NOT NULL,
  `name` varchar(250) CHARACTER SET utf8 NOT NULL,
  `img_src` varchar(500) CHARACTER SET utf8 NOT NULL,
  `price` decimal(10,0) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `product_item`
--

INSERT INTO `product_item` (`id`, `sub_cat_id`, `name`, `img_src`, `price`) VALUES
(61, 9, 'شرارة نجوم الليل', '/static/images/party_light.jpg', '1'),
(62, 9, 'شرارة نجوم الليل', '/static/images/heart_light.jpg', '4'),
(63, 4, 'الشجرة المضيئة', '/static/images/light_tree.jpg', '110'),
(64, 6, 'البالونة الشفافة المضيئة', '/static/images/trans_baloon.jpg', '25'),
(65, 1, 'الستارة المضيئة', '/static/images/light_curtain.jpg', '120'),
(66, 3, 'الشموع الثلاثية المضيئة', '/static/images/3_colored_candle.jpg', '35'),
(67, 2, 'سلسة إضاءة البيبي لايت', '/static/images/baby_light.jpg', '35'),
(68, 2, 'سلك الليزر المضيء', '/static/images/led_light.jpg', '80'),
(69, 3, 'الشموع المضيئة الصغيرة', '/static/images/small_candles.jpg', '35'),
(70, 6, 'البالونات المضيئة في الظلام', '/static/images/light_baloons.jpg', '10'),
(71, 2, 'سلسة إضاءة كرة القطن ', '/static/images/cotton_ball.jpg', '35'),
(72, 1, 'ستارة النجوم', '/static/images/star_light.jpg', '100'),
(73, 5, 'صندوق الأحرف المضيء', '/static/images/light_board.jpg', '170'),
(74, 1, 'ستارة الشلال المضيء', '/static/images/waterfall_curtain.jpg', '110'),
(75, 10, 'المايكروفون المتنقل المضيء', '/static/images/light_mic.jpg', '80'),
(76, 2, 'سلسة إضاءة الفوانيس', '/static/images/fanoos_light1.jpg', '35'),
(77, 1, 'ستارة الشبكة المضيئة', '/static/images/web_curtain.jpg', '110'),
(78, 10, 'المايكروفون المتنقل', '/static/images/mic.jpg', '80'),
(79, 2, 'سلسة إضاءة الفوانيس والنجوم', '/static/images/star_moon_light.jpg', '35'),
(80, 2, 'سلسة إضاءة عقد الفانوس', '/static/images/fanoos_light.jpg', '35'),
(81, 4, 'شجرة الفوانيس المضيئة', '/static/images/fanoos_tree.jpg', '110'),
(82, 7, 'مكعبات الثلج المضيئة', '/static/images/ice_cubes.jpg', '35'),
(83, 8, 'الحذاء الرياضي المضيء', '/static/images/light_shoes.jpg', '50'),
(84, 10, 'كريستالة الليزر', '/static/images/crystal_light.jpg', '60'),
(85, 7, 'مكعبات الثلج الفسفورية', '/static/images/phosphoric_ice_cubes.jpg', '30'),
(86, 10, 'السماعات الهرمية المضيئة', '/static/images/headphones1.jpg', '90'),
(87, 7, 'الكوب المضيء', '/static/images/light_cups.jpg', '15'),
(88, 10, 'سماعة النافورة الراقصة', '/static/images/two_headphones.jpg', '100'),
(89, 11, 'السبورة المضيئة', '/static/images/light_blackboard.jpg', '175'),
(90, 8, 'الأساور الفسفورية', '/static/images/phosphoric_bracelet.jpg', '1');

-- --------------------------------------------------------

--
-- Table structure for table `sub_category`
--

CREATE TABLE `sub_category` (
  `id` int(11) NOT NULL,
  `category_id` int(11) NOT NULL,
  `name` varchar(250) CHARACTER SET utf8 NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `sub_category`
--

INSERT INTO `sub_category` (`id`, `category_id`, `name`) VALUES
(1, 1, 'الستائر المضيئة'),
(2, 1, 'السلاسل المضيئة'),
(3, 1, 'الشموع المضيئة'),
(4, 1, 'الأشجار المضيئة'),
(5, 1, 'الأحرف المضيئة'),
(6, 3, 'البالونات المضيئة'),
(7, 3, 'الأواني المضيئة'),
(8, 3, 'الإكسسورات المضيئة'),
(9, 3, 'الشرارة المضيئة'),
(10, 4, 'السماعات المضيئة'),
(11, 4, 'الألواح المضيئة');

-- --------------------------------------------------------

--
-- Structure for view `order_view`
--
DROP TABLE IF EXISTS `order_view`;

CREATE ALGORITHM=UNDEFINED DEFINER=`sql12312605`@`%` SQL SECURITY DEFINER VIEW `order_view`  AS  select `product_item`.`id` AS `product_id`,`product_item`.`name` AS `product_name`,`sub_category`.`name` AS `subcategory_name`,`category`.`name` AS `category_name`,`product_item`.`price` AS `price` from ((`category` join `sub_category`) join `product_item`) where ((`product_item`.`sub_cat_id` = `sub_category`.`id`) and (`sub_category`.`category_id` = `category`.`id`)) ;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `category`
--
ALTER TABLE `category`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `orders`
--
ALTER TABLE `orders`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `order_item`
--
ALTER TABLE `order_item`
  ADD PRIMARY KEY (`id`),
  ADD KEY `order_item_ibfk_1` (`order_id`),
  ADD KEY `order_item_ibfk_2` (`product_id`);

--
-- Indexes for table `product_item`
--
ALTER TABLE `product_item`
  ADD PRIMARY KEY (`id`),
  ADD KEY `sub_cat_id` (`sub_cat_id`);

--
-- Indexes for table `sub_category`
--
ALTER TABLE `sub_category`
  ADD PRIMARY KEY (`id`),
  ADD KEY `category_id` (`category_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `category`
--
ALTER TABLE `category`
  MODIFY `id` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=27;
--
-- AUTO_INCREMENT for table `orders`
--
ALTER TABLE `orders`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=25;
--
-- AUTO_INCREMENT for table `order_item`
--
ALTER TABLE `order_item`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=24;
--
-- AUTO_INCREMENT for table `product_item`
--
ALTER TABLE `product_item`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=121;
--
-- AUTO_INCREMENT for table `sub_category`
--
ALTER TABLE `sub_category`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=12;
--
-- Constraints for dumped tables
--

--
-- Constraints for table `order_item`
--
ALTER TABLE `order_item`
  ADD CONSTRAINT `order_item_ibfk_2` FOREIGN KEY (`product_id`) REFERENCES `product_item` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `order_item_ibfk_1` FOREIGN KEY (`order_id`) REFERENCES `orders` (`id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `product_item`
--
ALTER TABLE `product_item`
  ADD CONSTRAINT `product_item_ibfk_1` FOREIGN KEY (`sub_cat_id`) REFERENCES `sub_category` (`id`);

--
-- Constraints for table `sub_category`
--
ALTER TABLE `sub_category`
  ADD CONSTRAINT `sub_category_ibfk_1` FOREIGN KEY (`category_id`) REFERENCES `category` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
