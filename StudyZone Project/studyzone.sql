-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: May 27, 2023 at 10:39 AM
-- Server version: 10.4.27-MariaDB
-- PHP Version: 8.0.25

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `studyzone`
--

-- --------------------------------------------------------

--
-- Table structure for table `auth_group`
--

CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL,
  `name` varchar(150) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `auth_group_permissions`
--

CREATE TABLE `auth_group_permissions` (
  `id` bigint(20) NOT NULL,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `auth_permission`
--

CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `auth_permission`
--

INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
(1, 'Can add log entry', 1, 'add_logentry'),
(2, 'Can change log entry', 1, 'change_logentry'),
(3, 'Can delete log entry', 1, 'delete_logentry'),
(4, 'Can view log entry', 1, 'view_logentry'),
(5, 'Can add permission', 2, 'add_permission'),
(6, 'Can change permission', 2, 'change_permission'),
(7, 'Can delete permission', 2, 'delete_permission'),
(8, 'Can view permission', 2, 'view_permission'),
(9, 'Can add group', 3, 'add_group'),
(10, 'Can change group', 3, 'change_group'),
(11, 'Can delete group', 3, 'delete_group'),
(12, 'Can view group', 3, 'view_group'),
(13, 'Can add content type', 4, 'add_contenttype'),
(14, 'Can change content type', 4, 'change_contenttype'),
(15, 'Can delete content type', 4, 'delete_contenttype'),
(16, 'Can view content type', 4, 'view_contenttype'),
(17, 'Can add session', 5, 'add_session'),
(18, 'Can change session', 5, 'change_session'),
(19, 'Can delete session', 5, 'delete_session'),
(20, 'Can view session', 5, 'view_session'),
(21, 'Can add contact', 6, 'add_contact'),
(22, 'Can change contact', 6, 'change_contact'),
(23, 'Can delete contact', 6, 'delete_contact'),
(24, 'Can view contact', 6, 'view_contact'),
(25, 'Can add subject', 7, 'add_subject'),
(26, 'Can change subject', 7, 'change_subject'),
(27, 'Can delete subject', 7, 'delete_subject'),
(28, 'Can view subject', 7, 'view_subject'),
(29, 'Can add subject modules', 8, 'add_subjectmodules'),
(30, 'Can change subject modules', 8, 'change_subjectmodules'),
(31, 'Can delete subject modules', 8, 'delete_subjectmodules'),
(32, 'Can view subject modules', 8, 'view_subjectmodules'),
(33, 'Can add subject details', 9, 'add_subjectdetails'),
(34, 'Can change subject details', 9, 'change_subjectdetails'),
(35, 'Can delete subject details', 9, 'delete_subjectdetails'),
(36, 'Can view subject details', 9, 'view_subjectdetails'),
(37, 'Can add user', 10, 'add_customuser'),
(38, 'Can change user', 10, 'change_customuser'),
(39, 'Can delete user', 10, 'delete_customuser'),
(40, 'Can view user', 10, 'view_customuser'),
(41, 'Can add question', 11, 'add_question'),
(42, 'Can change question', 11, 'change_question'),
(43, 'Can delete question', 11, 'delete_question'),
(44, 'Can view question', 11, 'view_question');

-- --------------------------------------------------------

--
-- Table structure for table `django_admin_log`
--

CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext DEFAULT NULL,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) UNSIGNED NOT NULL CHECK (`action_flag` >= 0),
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `django_admin_log`
--

INSERT INTO `django_admin_log` (`id`, `action_time`, `object_id`, `object_repr`, `action_flag`, `change_message`, `content_type_id`, `user_id`) VALUES
(1, '2023-04-25 10:01:53.138354', '1', 'Subject object (1)', 1, '[{\"added\": {}}]', 7, 1),
(2, '2023-04-25 10:32:44.745586', '2', 'Subject object (2)', 1, '[{\"added\": {}}]', 7, 1),
(3, '2023-04-27 04:56:50.323601', '2', 'Subject object (2)', 2, '[{\"changed\": {\"fields\": [\"Subject Image\"]}}]', 7, 1),
(4, '2023-04-27 04:57:11.735065', '2', 'Subject object (2)', 2, '[{\"changed\": {\"fields\": [\"Sub name\"]}}]', 7, 1),
(5, '2023-04-27 04:57:36.245869', '3', 'Subject object (3)', 1, '[{\"added\": {}}]', 7, 1),
(6, '2023-04-27 04:57:50.990589', '4', 'Subject object (4)', 1, '[{\"added\": {}}]', 7, 1),
(7, '2023-04-27 04:58:03.455388', '5', 'Subject object (5)', 1, '[{\"added\": {}}]', 7, 1),
(8, '2023-04-27 07:15:59.280397', '1', 'Subject object (1)', 2, '[]', 7, 1),
(9, '2023-04-27 10:20:49.137821', '1', 'SubjectModules object (1)', 1, '[{\"added\": {}}]', 8, 1),
(10, '2023-04-27 10:41:09.977296', '6', 'Subject object (6)', 1, '[{\"added\": {}}]', 7, 1),
(11, '2023-04-27 10:41:23.430456', '6', 'Subject object (6)', 3, '', 7, 1),
(12, '2023-04-27 10:41:51.884719', '5', 'Subject object (5)', 2, '[]', 7, 1),
(13, '2023-05-02 07:23:38.764287', '2', 'SubjectModules object (2)', 1, '[{\"added\": {}}]', 8, 1),
(14, '2023-05-03 05:05:59.970709', '1', 'SubjectDetails object (1)', 1, '[{\"added\": {}}]', 9, 1),
(15, '2023-05-03 05:18:13.731144', '2', 'SubjectDetails object (2)', 1, '[{\"added\": {}}]', 9, 1),
(16, '2023-05-03 09:01:03.299072', '6', 'Contact object (6)', 3, '', 6, 1),
(17, '2023-05-03 09:01:05.487027', '7', 'Contact object (7)', 3, '', 6, 1),
(18, '2023-05-03 09:01:07.862393', '5', 'Contact object (5)', 3, '', 6, 1),
(19, '2023-05-03 09:01:10.921103', '4', 'Contact object (4)', 3, '', 6, 1),
(20, '2023-05-03 09:01:14.110536', '3', 'Contact object (3)', 3, '', 6, 1),
(21, '2023-05-03 16:22:47.045670', '8', 'Contact object (8)', 3, '', 6, 1),
(22, '2023-05-03 16:55:10.034447', '21', 'Contact object (21)', 3, '', 6, 1),
(23, '2023-05-03 16:55:13.277711', '20', 'Contact object (20)', 3, '', 6, 1),
(24, '2023-05-03 16:55:15.899365', '19', 'Contact object (19)', 3, '', 6, 1),
(25, '2023-05-03 16:55:18.582339', '18', 'Contact object (18)', 3, '', 6, 1),
(26, '2023-05-03 16:55:21.230397', '17', 'Contact object (17)', 3, '', 6, 1),
(27, '2023-05-03 16:55:24.232618', '1', 'Contact object (1)', 3, '', 6, 1),
(28, '2023-05-03 16:55:28.150387', '9', 'Contact object (9)', 3, '', 6, 1),
(29, '2023-05-07 08:13:27.001510', '30', 'Contact object (30)', 3, '', 6, 1),
(30, '2023-05-07 08:13:29.770681', '31', 'Contact object (31)', 3, '', 6, 1),
(31, '2023-05-07 08:13:32.569754', '32', 'Contact object (32)', 3, '', 6, 1),
(32, '2023-05-07 08:13:35.162629', '33', 'Contact object (33)', 3, '', 6, 1),
(33, '2023-05-07 08:13:37.637263', '34', 'Contact object (34)', 3, '', 6, 1),
(34, '2023-05-07 08:13:40.425480', '35', 'Contact object (35)', 3, '', 6, 1),
(35, '2023-05-07 08:13:44.311080', '36', 'Contact object (36)', 3, '', 6, 1),
(36, '2023-05-07 08:13:47.013929', '37', 'Contact object (37)', 3, '', 6, 1),
(37, '2023-05-07 08:13:51.024564', '38', 'Contact object (38)', 3, '', 6, 1),
(38, '2023-05-07 08:14:09.240464', '39', 'Contact object (39)', 2, '[{\"changed\": {\"fields\": [\"Message\"]}}]', 6, 1),
(39, '2023-05-09 07:29:33.174131', '7', 'Subject object (7)', 1, '[{\"added\": {}}]', 7, 1),
(40, '2023-05-09 07:30:00.088329', '8', 'Subject object (8)', 1, '[{\"added\": {}}]', 7, 1),
(41, '2023-05-09 07:32:17.026171', '3', 'SubjectModules object (3)', 1, '[{\"added\": {}}]', 8, 1),
(42, '2023-05-09 07:35:33.144934', '3', 'SubjectDetails object (3)', 1, '[{\"added\": {}}]', 9, 1),
(43, '2023-05-09 07:45:01.826856', '8', 'Subject object (8)', 3, '', 7, 1),
(44, '2023-05-09 07:45:06.540804', '7', 'Subject object (7)', 3, '', 7, 1),
(45, '2023-05-17 04:48:53.516556', '8', '123', 3, '', 10, 1),
(46, '2023-05-17 04:49:01.257675', '9', 'adf', 3, '', 10, 1),
(47, '2023-05-24 00:30:13.317358', '6', 'Apurba1', 3, '', 10, 1),
(48, '2023-05-24 00:30:19.160488', '5', 'apurba5', 3, '', 10, 1),
(49, '2023-05-24 00:30:24.663846', '4', 'apurba', 3, '', 10, 1),
(50, '2023-05-24 15:25:50.159097', '4', 'SubjectModules object (4)', 1, '[{\"added\": {}}]', 8, 1),
(51, '2023-05-25 02:36:32.808939', '4', 'SubjectModules object (4)', 3, '', 8, 1),
(52, '2023-05-25 02:40:34.262728', '5', 'SubjectModules object (5)', 1, '[{\"added\": {}}]', 8, 1),
(53, '2023-05-25 02:42:23.245921', '5', 'SubjectModules object (5)', 2, '[{\"changed\": {\"fields\": [\"Module desc\"]}}]', 8, 1),
(54, '2023-05-25 02:42:41.278821', '5', 'SubjectModules object (5)', 2, '[{\"changed\": {\"fields\": [\"Module desc\"]}}]', 8, 1),
(55, '2023-05-25 02:50:43.188128', '6', 'SubjectModules object (6)', 1, '[{\"added\": {}}]', 8, 1),
(56, '2023-05-25 02:51:40.318740', '7', 'SubjectModules object (7)', 1, '[{\"added\": {}}]', 8, 1),
(57, '2023-05-25 02:53:09.765978', '8', 'SubjectModules object (8)', 1, '[{\"added\": {}}]', 8, 1),
(58, '2023-05-25 02:53:58.342595', '9', 'SubjectModules object (9)', 1, '[{\"added\": {}}]', 8, 1),
(59, '2023-05-25 02:55:13.317337', '10', 'SubjectModules object (10)', 1, '[{\"added\": {}}]', 8, 1),
(60, '2023-05-25 02:56:42.541018', '11', 'SubjectModules object (11)', 1, '[{\"added\": {}}]', 8, 1),
(61, '2023-05-25 02:57:31.553806', '12', 'SubjectModules object (12)', 1, '[{\"added\": {}}]', 8, 1),
(62, '2023-05-25 02:58:11.040370', '13', 'SubjectModules object (13)', 1, '[{\"added\": {}}]', 8, 1),
(63, '2023-05-25 02:59:27.480378', '14', 'SubjectModules object (14)', 1, '[{\"added\": {}}]', 8, 1),
(64, '2023-05-25 03:04:46.198620', '15', 'SubjectModules object (15)', 1, '[{\"added\": {}}]', 8, 1),
(65, '2023-05-25 03:05:08.999359', '16', 'SubjectModules object (16)', 1, '[{\"added\": {}}]', 8, 1),
(66, '2023-05-25 03:05:41.088038', '17', 'SubjectModules object (17)', 1, '[{\"added\": {}}]', 8, 1),
(67, '2023-05-25 03:06:09.976357', '18', 'SubjectModules object (18)', 1, '[{\"added\": {}}]', 8, 1),
(68, '2023-05-25 03:06:43.997538', '19', 'SubjectModules object (19)', 1, '[{\"added\": {}}]', 8, 1),
(69, '2023-05-25 03:07:05.214742', '20', 'SubjectModules object (20)', 1, '[{\"added\": {}}]', 8, 1),
(70, '2023-05-25 03:07:20.575383', '21', 'SubjectModules object (21)', 1, '[{\"added\": {}}]', 8, 1),
(71, '2023-05-25 03:07:41.959997', '22', 'SubjectModules object (22)', 1, '[{\"added\": {}}]', 8, 1),
(72, '2023-05-25 04:40:40.313734', '23', 'SubjectModules object (23)', 1, '[{\"added\": {}}]', 8, 1),
(73, '2023-05-25 04:42:43.470494', '24', 'SubjectModules object (24)', 1, '[{\"added\": {}}]', 8, 1),
(74, '2023-05-25 04:43:43.479921', '25', 'SubjectModules object (25)', 1, '[{\"added\": {}}]', 8, 1),
(75, '2023-05-25 04:45:09.360518', '26', 'SubjectModules object (26)', 1, '[{\"added\": {}}]', 8, 1),
(76, '2023-05-25 04:48:12.656207', '27', 'SubjectModules object (27)', 1, '[{\"added\": {}}]', 8, 1),
(77, '2023-05-25 04:50:37.088794', '28', 'SubjectModules object (28)', 1, '[{\"added\": {}}]', 8, 1),
(78, '2023-05-25 04:53:30.107084', '29', 'SubjectModules object (29)', 1, '[{\"added\": {}}]', 8, 1),
(79, '2023-05-25 04:54:50.929393', '30', 'SubjectModules object (30)', 1, '[{\"added\": {}}]', 8, 1),
(80, '2023-05-25 04:58:03.149190', '31', 'SubjectModules object (31)', 1, '[{\"added\": {}}]', 8, 1),
(81, '2023-05-25 04:58:45.911667', '32', 'SubjectModules object (32)', 1, '[{\"added\": {}}]', 8, 1),
(82, '2023-05-25 04:59:39.793938', '33', 'SubjectModules object (33)', 1, '[{\"added\": {}}]', 8, 1),
(83, '2023-05-25 05:00:25.231421', '34', 'SubjectModules object (34)', 1, '[{\"added\": {}}]', 8, 1),
(84, '2023-05-25 05:01:36.810164', '34', 'SubjectModules object (34)', 2, '[{\"changed\": {\"fields\": [\"Module desc\"]}}]', 8, 1),
(85, '2023-05-25 05:02:04.717318', '35', 'SubjectModules object (35)', 1, '[{\"added\": {}}]', 8, 1),
(86, '2023-05-25 05:03:25.966623', '36', 'SubjectModules object (36)', 1, '[{\"added\": {}}]', 8, 1),
(87, '2023-05-25 05:05:27.176894', '37', 'SubjectModules object (37)', 1, '[{\"added\": {}}]', 8, 1);

-- --------------------------------------------------------

--
-- Table structure for table `django_content_type`
--

CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `django_content_type`
--

INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
(1, 'admin', 'logentry'),
(3, 'auth', 'group'),
(2, 'auth', 'permission'),
(4, 'contenttypes', 'contenttype'),
(6, 'main', 'contact'),
(10, 'main', 'customuser'),
(11, 'main', 'question'),
(7, 'main', 'subject'),
(9, 'main', 'subjectdetails'),
(8, 'main', 'subjectmodules'),
(5, 'sessions', 'session');

-- --------------------------------------------------------

--
-- Table structure for table `django_migrations`
--

CREATE TABLE `django_migrations` (
  `id` bigint(20) NOT NULL,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `django_migrations`
--

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
(1, 'contenttypes', '0001_initial', '2023-04-25 09:55:01.696134'),
(2, 'contenttypes', '0002_remove_content_type_name', '2023-04-25 09:55:02.182921'),
(3, 'auth', '0001_initial', '2023-04-25 09:55:04.067888'),
(4, 'auth', '0002_alter_permission_name_max_length', '2023-04-25 09:55:04.683265'),
(5, 'auth', '0003_alter_user_email_max_length', '2023-04-25 09:55:04.721077'),
(6, 'auth', '0004_alter_user_username_opts', '2023-04-25 09:55:04.840467'),
(7, 'auth', '0005_alter_user_last_login_null', '2023-04-25 09:55:05.172031'),
(8, 'auth', '0006_require_contenttypes_0002', '2023-04-25 09:55:05.331724'),
(9, 'auth', '0007_alter_validators_add_error_messages', '2023-04-25 09:55:05.373169'),
(10, 'auth', '0008_alter_user_username_max_length', '2023-04-25 09:55:05.504650'),
(11, 'auth', '0009_alter_user_last_name_max_length', '2023-04-25 09:55:05.571167'),
(12, 'auth', '0010_alter_group_name_max_length', '2023-04-25 09:55:05.821876'),
(13, 'auth', '0011_update_proxy_permissions', '2023-04-25 09:55:05.875688'),
(14, 'auth', '0012_alter_user_first_name_max_length', '2023-04-25 09:55:05.933200'),
(15, 'main', '0001_initial', '2023-04-25 09:55:08.327636'),
(16, 'admin', '0001_initial', '2023-04-25 09:55:08.944633'),
(17, 'admin', '0002_logentry_remove_auto_add', '2023-04-25 09:55:09.034417'),
(18, 'admin', '0003_logentry_add_action_flag_choices', '2023-04-25 09:55:09.097973'),
(19, 'sessions', '0001_initial', '2023-04-25 09:55:09.441985'),
(20, 'main', '0002_auto_20230503_1213', '2023-05-03 06:43:27.502623'),
(21, 'main', '0003_auto_20230516_1034', '2023-05-16 14:47:37.481784'),
(22, 'main', '0004_question', '2023-05-18 10:36:55.967731');

-- --------------------------------------------------------

--
-- Table structure for table `django_session`
--

CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `django_session`
--

INSERT INTO `django_session` (`session_key`, `session_data`, `expire_date`) VALUES
('0uq1mkmze0r3jjx5xhlkydxat3wgtvt8', '.eJxVjDsOwjAQRO_iGlm2409CSZ8zWLveNQ4gW8qnQtydREoB3Wjem3mLCNta4rbwHCcSVxHE5bdDSE-uB6AH1HuTqdV1nlAeijzpIsdG_Lqd7t9BgaXsa89OD6SU7iA50gZ73bnMPlvTDTZ5DTSgZwRMvQ8ZSRkT9pgt5ISM4vMF5bQ4vA:1q2CEH:RZ7smI2caTvwbrjwnYtzFQT5t3PC3aVcigo8HfEy5tk', '2023-06-08 14:46:13.671535'),
('1kabf9n7v2kuaytfdajxdirafhu884ct', '.eJxVjMsOwiAQRf-FtSE8OpVx6b7fQAYYpGogKe3K-O_apAvd3nPOfQlP21r81nnxcxIXocXpdwsUH1x3kO5Ub03GVtdlDnJX5EG7nFri5_Vw_w4K9fKtDakM1qRRIyDoQUcLMASFzjhNMJ5NVooxs0NQLhm0yXHOAVUcIjGL9wesSzdQ:1q27HM:YJz7-hfx0-NxEawI7l5-MskVGyWYLIW3kurWE6a9_pE', '2023-06-08 09:29:04.514488'),
('3hjonmq3io0fv5tuz7ishqv9zxnzzj74', '.eJxVjDsOwjAQBe_iGln-rH-U9JzBWnttHECOFCcV4u4QKQW0b2bei0Xc1ha3UZY4ETszyU6_W8L8KH0HdMd-m3me-7pMie8KP-jg15nK83K4fwcNR_vWkDyi0YFISGW0CgKqAWOzdc5W7aRG0uhsTkYoLyWFEDzUCokcaB_Y-wO8xzbH:1pryyY:1yhEbXsBOda_OC1gvjokjk2fSc6Zw-kL7TKCWV87iJA', '2023-05-11 10:35:46.873556'),
('5u7hr9rmwkxhcx9306p1c50oe6q0nye5', '.eJxVjMsOgjAUBf-la9PcFrCtS_d-A7kvLGpKQmFl_HchYaHbmTnnbXpcl9yvVed-FHMxzpvTLyTkp5bdyAPLfbI8lWUeye6JPWy1t0n0dT3av4OMNW_r2CJIEyJTAwMII6QErk2BgDohYB1Eu-jDGZ1XUZGQnNuSZsMMbD5fEQc4fg:1pz96d:6p1OyLb86BMwZ5dNrK_TZLC_k3zMPzXPQc8ztRKXX_U', '2023-05-31 04:49:43.317284'),
('6vwaz4b1edgbfa5ybuorpgxmull1wpi1', '.eJxVjMsOwiAQRf-FtSE8OpVx6b7fQAYYpGogKe3K-O_apAvd3nPOfQlP21r81nnxcxIXocXpdwsUH1x3kO5Ub03GVtdlDnJX5EG7nFri5_Vw_w4K9fKtDakM1qRRIyDoQUcLMASFzjhNMJ5NVooxs0NQLhm0yXHOAVUcIjGL9wesSzdQ:1q24F0:nieBpU6I-FDHmici3PylusbqX0V1XyV56jzTuEYjT1I', '2023-06-08 06:14:26.924360'),
('7h0ghjr02r6ckxhmj9bbszlx6wojtlk2', '.eJxVjMEOwiAQRP-FsyHUUhY8eu83kIVdpGogKe3J-O9K0oOeJpn3Zl7C475lvzde_ULiIow4_XYB44NLB3THcqsy1rKtS5BdkQdtcq7Ez-vh_h1kbPm7tsiKGRwy6AA8srE9jY4qnNOYyKA1ABMGQ4QugB4IbSKYWA9OjeL9AQ28OK8:1ptJ1i:-0G386eeLlCv9BwDlV9cMRo6FWPYR2x3eBrGacXCNM0', '2023-05-15 02:12:30.402875'),
('7h20w369qlbsb2s9rjkqdrn2og9o6fx8', '.eJxVjDsOwjAQRO_iGlm2409CSZ8zWLveNQ4gW8qnQtydREoB3Wjem3mLCNta4rbwHCcSVxHE5bdDSE-uB6AH1HuTqdV1nlAeijzpIsdG_Lqd7t9BgaXsa89OD6SU7iA50gZ73bnMPlvTDTZ5DTSgZwRMvQ8ZSRkT9pgt5ISM4vMF5bQ4vA:1q1iEO:bXAOHZuODTa74gvpcJF6cfAO8qaQMzTGv3NRJvAK6KA', '2023-06-07 06:44:20.766997'),
('8q69pvl62edd3byecdykcylkqiiektj3', '.eJxVjMsOwiAQRf-FtSE8OpVx6b7fQAYYpGogKe3K-O_apAvd3nPOfQlP21r81nnxcxIXocXpdwsUH1x3kO5Ub03GVtdlDnJX5EG7nFri5_Vw_w4K9fKtDakM1qRRIyDoQUcLMASFzjhNMJ5NVooxs0NQLhm0yXHOAVUcIjGL9wesSzdQ:1q25iZ:xHLcK3D2Ece-61w0eWAVDE7CM7br-ekqyyEG6AFVM8g', '2023-06-08 07:49:03.135064'),
('8xhkk7kxdlr2jla1eha4xv5kxt925v2k', '.eJxVjDsOwyAQBe9CHSFjvpsyvc-AFhaCkwgkY1dR7h5bcpG0b2bem3nc1uK3nhY_E7syIdnldwwYn6kehB5Y743HVtdlDvxQ-Ek7nxql1-10_w4K9rLXEIAgGnCCRDZCCmcwaxtB2UE5NAgaQTnCkCmOAySnR4ouWQG7ZSX7fAH9nDfT:1pzGbI:HuE8ZSsbczw2go7ZrbK09iaNq_EkWdcGtn4FzBf0ZSE', '2023-05-31 12:49:52.757946'),
('8yr8sptyplbv77elxdd9cvymwnu5q3w2', '.eJxVjMsOwiAQRf-FtSE8OpVx6b7fQAYYpGogKe3K-O_apAvd3nPOfQlP21r81nnxcxIXocXpdwsUH1x3kO5Ub03GVtdlDnJX5EG7nFri5_Vw_w4K9fKtDakM1qRRIyDoQUcLMASFzjhNMJ5NVooxs0NQLhm0yXHOAVUcIjGL9wesSzdQ:1q2YUz:4E6aLmd2o6I0KB3YAi5oJOn9ivXKF6qz5j4YCCZaEfI', '2023-06-09 14:32:57.042016'),
('9fn3ev5qt0dfz6947e0q47wxmn8hcvx2', '.eJxVjEEOwiAQRe_C2hAoDIwu3fcMBBhGqoYmpV0Z765NutDtf-_9lwhxW2vYelnCROIijBGn3zHF_ChtJ3SP7TbLPLd1mZLcFXnQLseZyvN6uH8HNfb6rXVJqFNSA-AZiiEFA2aHBJYtekXeEBVWVrNh5zEjaway4MgwRGbx_gAAWzhP:1q0YoJ:4NyByRU0fx8bB5xIae-hiZxcMgK3erDJxQf1Oc6dfIo', '2023-06-04 02:28:39.625530'),
('akeaekn275zh0mkftthd1g188d6sd21x', '.eJxVjMEOwiAQRP-FsyHUUhY8eu83kIVdpGogKe3J-O9K0oOeJpn3Zl7C475lvzde_ULiIow4_XYB44NLB3THcqsy1rKtS5BdkQdtcq7Ez-vh_h1kbPm7tsiKGRwy6AA8srE9jY4qnNOYyKA1ABMGQ4QugB4IbSKYWA9OjeL9AQ28OK8:1ptjhQ:1L8h4iNheSDuQZCKjxJgdYbN2ke6lLUDjnOYWySMzfs', '2023-05-16 06:41:20.474945'),
('b1wq0iys7l5r0zvm0qytfp0ca5bg9q1j', '.eJxVjDsOwjAQBe_iGln-rH-U9JzBWnttHECOFCcV4u4QKQW0b2bei0Xc1ha3UZY4ETszyU6_W8L8KH0HdMd-m3me-7pMie8KP-jg15nK83K4fwcNR_vWkDyi0YFISGW0CgKqAWOzdc5W7aRG0uhsTkYoLyWFEDzUCokcaB_Y-wO8xzbH:1ptjup:4DBE6_Svr1jmyW_de-JFn6n_Ov0BA3sfQVNJ3Twiazg', '2023-05-16 06:55:11.869363'),
('bgc3jec7p49gp7fn38u4et5yzpibxjxt', '.eJxVjDsOwjAQRO_iGlm2409CSZ8zWLveNQ4gW8qnQtydREoB3Wjem3mLCNta4rbwHCcSVxHE5bdDSE-uB6AH1HuTqdV1nlAeijzpIsdG_Lqd7t9BgaXsa89OD6SU7iA50gZ73bnMPlvTDTZ5DTSgZwRMvQ8ZSRkT9pgt5ISM4vMF5bQ4vA:1q23ZA:C0ZnDUplZRyA6iMOiDBDCKmvgyl1BIHzTrGROLbKCPI', '2023-06-08 05:31:12.237614'),
('ddpxwu303x3tw8atugpgvgn8j5bdbjvf', '.eJxVjMsOwiAQRf-FtSE8OpVx6b7fQAYYpGogKe3K-O_apAvd3nPOfQlP21r81nnxcxIXocXpdwsUH1x3kO5Ub03GVtdlDnJX5EG7nFri5_Vw_w4K9fKtDakM1qRRIyDoQUcLMASFzjhNMJ5NVooxs0NQLhm0yXHOAVUcIjGL9wesSzdQ:1q27MH:ailtUYmktv_i68I0HT5MnuxHSM9wnG0-vcjgJQfuEv4', '2023-06-08 09:34:09.967749'),
('dv69qee1slwuhq13rt108drw4oeto5by', '.eJxVjEEKwyAQAP_iuUhW2ag99t43iO5qTVsUYnIK_XsRcmivM8Mcwod9K37vafULi6sAcfllMdAr1SH4GeqjSWp1W5coRyJP2-W9cXrfzvZvUEIvY0suZI5uIkZUwExa62hzRGMyoAXFjCpZBMhudpZZc3KgtJkpq8mIzxf1azff:1q2130:dCvH5igObHELUN9gdOixWqal_0iQd8Juemn7Mc5uwJI', '2023-06-08 02:49:50.148608'),
('ectistx1sp16fokkyj7apwhrd3ltgxfc', '.eJxVjMsOwiAQRf-FtSE8OpVx6b7fQAYYpGogKe3K-O_apAvd3nPOfQlP21r81nnxcxIXocXpdwsUH1x3kO5Ub03GVtdlDnJX5EG7nFri5_Vw_w4K9fKtDakM1qRRIyDoQUcLMASFzjhNMJ5NVooxs0NQLhm0yXHOAVUcIjGL9wesSzdQ:1q23N5:8FpvMyjELKK-F2vsdwCHY-t58xlZ4W3vrkjAdtDD0Kc', '2023-06-08 05:18:43.487660'),
('eknwqdo28u42723c24ujkldwvm3k1ra3', '.eJxVjMsOwiAQRf-FtSE8OpVx6b7fQAYYpGogKe3K-O_apAvd3nPOfQlP21r81nnxcxIXocXpdwsUH1x3kO5Ub03GVtdlDnJX5EG7nFri5_Vw_w4K9fKtDakM1qRRIyDoQUcLMASFzjhNMJ5NVooxs0NQLhm0yXHOAVUcIjGL9wesSzdQ:1q2aHB:7ddNdlDeg8-Abmog6x2i4-VJ3wpOSURC4w46EYwm5wA', '2023-06-09 16:26:49.288980'),
('fbm1arfv5uczr3qmce8zyw1n9tfrx80c', '.eJxVjMsOwiAQRf-FtSE8OpVx6b7fQAYYpGogKe3K-O_apAvd3nPOfQlP21r81nnxcxIXocXpdwsUH1x3kO5Ub03GVtdlDnJX5EG7nFri5_Vw_w4K9fKtDakM1qRRIyDoQUcLMASFzjhNMJ5NVooxs0NQLhm0yXHOAVUcIjGL9wesSzdQ:1q2o80:3EDWnV54_FIF04zwxoQ1sTAE8-VzFNHtTNTLO-a-OLk', '2023-06-10 07:14:16.522160'),
('fcygrjtt0hgy6knr6v6aec5f8vbqp9zw', '.eJxVjDsOwjAQRO_iGlm2409CSZ8zWLveNQ4gW8qnQtydREoB3Wjem3mLCNta4rbwHCcSVxHE5bdDSE-uB6AH1HuTqdV1nlAeijzpIsdG_Lqd7t9BgaXsa89OD6SU7iA50gZ73bnMPlvTDTZ5DTSgZwRMvQ8ZSRkT9pgt5ISM4vMF5bQ4vA:1q1pHK:vx0Pl3skqwD16ATCglljieXq97Ys6IXy_I6eujT2wpk', '2023-06-07 14:15:50.612873'),
('hmd8d7ucgk04xb3t68r3h32teaob7wmk', '.eJxVjEEOwiAQRe_C2hCmwlBcuu8ZCMyMUjU0Ke3KeHdD0oVu_3vvv1VM-1bi3mSNM6uLgqBOv2NO9JTaCT9SvS-alrqtc9Zd0QdtelpYXtfD_TsoqZVeExuD6NxIEAx4bwNaAGREyo7QuwFuIUgYkYy4hDRgwswC1uEZrPp8Ad-zNvk:1pzJxO:fbIPzmW0kgg6VRQCuxMuA2toreWRBaYzcQJp6wQbHnY', '2023-05-31 16:24:54.887960'),
('ho3ynds9v4gx5f940onrr1ovr48rkphb', '.eJxVjEEKwyAQAP_iuUhW2ag99t43iO5qTVsUYnIK_XsRcmivM8Mcwod9K37vafULi6sAcfllMdAr1SH4GeqjSWp1W5coRyJP2-W9cXrfzvZvUEIvY0suZI5uIkZUwExa62hzRGMyoAXFjCpZBMhudpZZc3KgtJkpq8mIzxf1azff:1q20os:uNma6bBXujsHjMnPJ-088VluHR95p39q8ZVufLtAAnU', '2023-06-08 02:35:14.928965'),
('j90yle7cv43mp2shter5vpmbgi8pteme', '.eJxVjMsOgjAUBf-la9PcFrCtS_d-A7kvLGpKQmFl_HchYaHbmTnnbXpcl9yvVed-FHMxzpvTLyTkp5bdyAPLfbI8lWUeye6JPWy1t0n0dT3av4OMNW_r2CJIEyJTAwMII6QErk2BgDohYB1Eu-jDGZ1XUZGQnNuSZsMMbD5fEQc4fg:1pz9Lk:eqqa76AlDnwWARn0-ykrjM2QvmdYZKunbpk_mJkiXXA', '2023-05-31 05:05:20.933893'),
('lfd6jaia05eend1lgzzft0lix814ouxi', '.eJxVjMsOwiAQRf-FtSE8OpVx6b7fQAYYpGogKe3K-O_apAvd3nPOfQlP21r81nnxcxIXocXpdwsUH1x3kO5Ub03GVtdlDnJX5EG7nFri5_Vw_w4K9fKtDakM1qRRIyDoQUcLMASFzjhNMJ5NVooxs0NQLhm0yXHOAVUcIjGL9wesSzdQ:1q27Ai:C5hvd6U3Df7GgORmFWJlM5JjXSbUorJJ_5J5hOhrFGI', '2023-06-08 09:22:12.615452'),
('lpvllc4ym52jhsa17k1dbbj0q5ic7wv0', '.eJxVjDsOwjAQRO_iGlm2409CSZ8zWLveNQ4gW8qnQtydREoB3Wjem3mLCNta4rbwHCcSVxHE5bdDSE-uB6AH1HuTqdV1nlAeijzpIsdG_Lqd7t9BgaXsa89OD6SU7iA50gZ73bnMPlvTDTZ5DTSgZwRMvQ8ZSRkT9pgt5ISM4vMF5bQ4vA:1pzBzr:B2pDGJ2O3OYSlPbRebABTFEk8oG8V8GmKDBeAuXpuFw', '2023-05-31 07:54:55.899044'),
('m53zxis4gbx552ooetgkk5iahv9lyiyw', '.eJxVjDsOwyAQBe9CHSG-a0iZ3mdAC6yDkwgkY1dR7h5bcpG0M_PemwXc1hK2TkuYM7syKdnlF0ZMT6qHyQ-s98ZTq-syR34k_LSdjy3T63a2fwcFe9nXk42QIkRF2jiLyRDpaNNgACxmoQx5mkiYnTsYAAlFTtqTlV5rJxT7fAEmKjho:1pz9nO:8sVzV8uzd9_bW0OB7iMU2S-DATs2CFHZAWWKORTgnao', '2023-05-31 05:33:54.828996'),
('o2r35af8lh6jfoac38fv0t1h2nuokzkl', '.eJxVjMsOwiAQRf-FtSFQHmVcuvcbyMAMUjUlKe3K-O_apAvd3nPOfYmI21rj1nmJE4mz0E6cfseE-cHzTuiO863J3OZ1mZLcFXnQLq-N-Hk53L-Dir1-a0gBC2hwTATWlAJJGRyL1wOokawdSBvM1gUPzJCNKZaU4jxYhQG9eH8ADyI4FA:1pzGj5:aD32ZKL1wM_DBHLfUKh4AeW8yiLlXEN2ySM6xb8URhY', '2023-05-31 12:57:55.372200'),
('oyaa374ujq0qw2mw27hkn43xxyhifuhc', '.eJxVjDsOwjAQBe_iGln-rH-U9JzBWnttHECOFCcV4u4QKQW0b2bei0Xc1ha3UZY4ETszyU6_W8L8KH0HdMd-m3me-7pMie8KP-jg15nK83K4fwcNR_vWkDyi0YFISGW0CgKqAWOzdc5W7aRG0uhsTkYoLyWFEDzUCokcaB_Y-wO8xzbH:1puF0X:tLDGBSpVZAcWVvHVNjk-dBSieokBCr5b-pcpLrTzGBE', '2023-05-17 16:07:09.189448'),
('oykdycosor3lu9qgns4oml36l1a1p8o3', '.eJxVjDsOwjAQBe_iGln-rH-U9JzBWnttHECOFCcV4u4QKQW0b2bei0Xc1ha3UZY4ETszyU6_W8L8KH0HdMd-m3me-7pMie8KP-jg15nK83K4fwcNR_vWkDyi0YFISGW0CgKqAWOzdc5W7aRG0uhsTkYoLyWFEDzUCokcaB_Y-wO8xzbH:1pru1J:9vpndbLWCBd_gYJcUchxTATh8koBHzk_TFAoAF0N2_Y', '2023-05-11 05:18:17.733521'),
('p4bmzkfa2evznhxvmpvtzqrjem4czvgr', '.eJxVjDsOwjAQRO_iGlm2409CSZ8zWLveNQ4gW8qnQtydREoB3Wjem3mLCNta4rbwHCcSVxHE5bdDSE-uB6AH1HuTqdV1nlAeijzpIsdG_Lqd7t9BgaXsa89OD6SU7iA50gZ73bnMPlvTDTZ5DTSgZwRMvQ8ZSRkT9pgt5ISM4vMF5bQ4vA:1q1hLz:S9TPhZt0EJ-9zXy-jrBJKhfwKRKMakN8QxUsbBueWPQ', '2023-06-07 05:48:07.330458'),
('p4s44izk3ml69fx7x8lg7qcle43ao8ri', '.eJxVjDsOwjAQBe_iGln-rH-U9JzBWnttHECOFCcV4u4QKQW0b2bei0Xc1ha3UZY4ETszyU6_W8L8KH0HdMd-m3me-7pMie8KP-jg15nK83K4fwcNR_vWkDyi0YFISGW0CgKqAWOzdc5W7aRG0uhsTkYoLyWFEDzUCokcaB_Y-wO8xzbH:1pu64O:AJoUcM-RI6HdJuufgG0OV-8IJb0-4RWjRq8KjFLUefg', '2023-05-17 06:34:32.168021'),
('r02d152cybtyo9zja45pgqshx1sbklct', '.eJxVjDsOwjAQRO_iGlm2409CSZ8zWLveNQ4gW8qnQtydREoB3Wjem3mLCNta4rbwHCcSVxHE5bdDSE-uB6AH1HuTqdV1nlAeijzpIsdG_Lqd7t9BgaXsa89OD6SU7iA50gZ73bnMPlvTDTZ5DTSgZwRMvQ8ZSRkT9pgt5ISM4vMF5bQ4vA:1q27sO:Vy7Ij78ikzLZ3aqlDQZ_77jOu0jlATjWnZCLyxWZzTg', '2023-06-08 10:07:20.020369'),
('rkby9j0g3c2bchpwjk3w2duk9rhwuyyh', '.eJxVjDsOwjAQBe_iGln-rH-U9JzBWnttHECOFCcV4u4QKQW0b2bei0Xc1ha3UZY4ETszyU6_W8L8KH0HdMd-m3me-7pMie8KP-jg15nK83K4fwcNR_vWkDyi0YFISGW0CgKqAWOzdc5W7aRG0uhsTkYoLyWFEDzUCokcaB_Y-wO8xzbH:1pu4mx:EBg_Xbt1fSTARzywxYS9BBveaGdl-cyqyN8bnwLz4fg', '2023-05-17 05:12:27.927891'),
('t8f9wdifogtto5ez6koif8llguc2ywho', '.eJxVjDsOwjAQRO_iGlm2409CSZ8zWLveNQ4gW8qnQtydREoB3Wjem3mLCNta4rbwHCcSVxHE5bdDSE-uB6AH1HuTqdV1nlAeijzpIsdG_Lqd7t9BgaXsa89OD6SU7iA50gZ73bnMPlvTDTZ5DTSgZwRMvQ8ZSRkT9pgt5ISM4vMF5bQ4vA:1q2CVr:O7SLByeafBgXGG8iFuuj8Tpu-7YHrrgiiucu3b_G8Ng', '2023-06-08 15:04:23.738143'),
('wbjberzle82ejyjsyewkj5irc4jsvwr6', '.eJxVjMsOwiAQRf-FtSE8OpVx6b7fQAYYpGogKe3K-O_apAvd3nPOfQlP21r81nnxcxIXocXpdwsUH1x3kO5Ub03GVtdlDnJX5EG7nFri5_Vw_w4K9fKtDakM1qRRIyDoQUcLMASFzjhNMJ5NVooxs0NQLhm0yXHOAVUcIjGL9wesSzdQ:1q2D78:wkW_9dvDT67jRlY8FNTeYn-AM_eMFE_0l_GogyQePrU', '2023-06-08 15:42:54.320930'),
('y0ptqvip8cemnucnyjvghauuykx5cypd', '.eJxVjDsOwjAQBe_iGln-rH-U9JzBWnttHECOFCcV4u4QKQW0b2bei0Xc1ha3UZY4ETszyU6_W8L8KH0HdMd-m3me-7pMie8KP-jg15nK83K4fwcNR_vWkDyi0YFISGW0CgKqAWOzdc5W7aRG0uhsTkYoLyWFEDzUCokcaB_Y-wO8xzbH:1q1qPL:Icxw-9uZrVMMrUkBeWHYQMcgubznNQ7bc4Zf2dGC7qA', '2023-06-07 15:28:11.158780'),
('yn1qud7zov4hgzwmngqo7uv395sa1i9s', '.eJxVjMsOwiAQRf-FtSE8OpVx6b7fQAYYpGogKe3K-O_apAvd3nPOfQlP21r81nnxcxIXocXpdwsUH1x3kO5Ub03GVtdlDnJX5EG7nFri5_Vw_w4K9fKtDakM1qRRIyDoQUcLMASFzjhNMJ5NVooxs0NQLhm0yXHOAVUcIjGL9wesSzdQ:1q2oVn:vY5y4Ywqq196LdLbWmcomeGtDo-k9ln0rTE0cvMSLWs', '2023-06-10 07:38:51.549559');

-- --------------------------------------------------------

--
-- Table structure for table `main_contact`
--

CREATE TABLE `main_contact` (
  `id` bigint(20) NOT NULL,
  `name` varchar(150) NOT NULL,
  `email` varchar(255) NOT NULL,
  `msg` longtext NOT NULL,
  `date` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `main_contact`
--

INSERT INTO `main_contact` (`id`, `name`, `email`, `msg`, `date`) VALUES
(39, 'Apurba', 'Sau@gmail.com', 'HII My Name is Apurba', '2023-05-07'),
(40, 'Apurba', 'apurbasau2003@gmail.com', 'Hii My Problems is This', '2023-05-09'),
(41, 'Apurba', 'apurbasau2003@gamil.com', 'adsfafafabflabflasf lask fl;asnflasdnf\'kasg', '2023-05-17'),
(42, 'asdfg', 'agda@gmail.com', 'asdfasdasdf', '2023-05-25'),
(43, 'apurba', 'apu@gmail.com', 'hiii', '2023-05-25'),
(44, 'apurba', 'apurba@gmail.com', 'aaaaa', '2023-05-25'),
(45, 'apurba', 'apurba@gmail.com', 'asdgsdfhgsfg', '2023-05-25');

-- --------------------------------------------------------

--
-- Table structure for table `main_customuser`
--

CREATE TABLE `main_customuser` (
  `id` bigint(20) NOT NULL,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  `contact_no` varchar(12) NOT NULL,
  `gender` varchar(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `main_customuser`
--

INSERT INTO `main_customuser` (`id`, `password`, `last_login`, `is_superuser`, `username`, `first_name`, `last_name`, `email`, `is_staff`, `is_active`, `date_joined`, `contact_no`, `gender`) VALUES
(1, 'pbkdf2_sha256$260000$JOl1YbHZmKXtZZ57ivIusn$nqUh39618lkZC1MBk6WDLoVOvEaSsQ22SG7xzJxzEpI=', '2023-05-27 07:58:53.991927', 1, 'admin', '', '', '', 1, 1, '2023-04-25 09:59:47.391274', '', ''),
(7, 'pbkdf2_sha256$260000$ykMt9KVADPvuiNjCY5Omp4$/+JWIVDOVrBwGfksf3zYnvv/BZkqm3nKXVSIAzJE4GI=', '2023-05-25 15:32:57.590324', 0, 'Sonay005', 'Apurba', 'Sau', 'apurbasau2003@gamil.com', 0, 1, '2023-05-16 14:50:33.614140', '9635236517', ''),
(16, 'pbkdf2_sha256$260000$UI4coCYgXXcTt67BH3r9NW$V0o2KLBDVq8HGXxvX2ZdhDKAFK3UhgUsSRp/HLCEJ6c=', NULL, 0, 'rshsfh', 'sfhdfh', 'hnipubfghhuobubu', 'dfghdfh@gmail.com', 0, 1, '2023-05-17 13:06:03.203402', '1234567890', ''),
(18, 'pbkdf2_sha256$260000$fNenCyJfTFGMIwi4zNaan6$bzlKkOSe4VdVCY+4bFDgbZ2MYXuIAxeYBtgBZaX4nig=', '2023-05-17 16:22:42.172257', 0, 'Apurba001', 'Apurba', 'Sau', 'apurbasau2003@gmail.com', 0, 1, '2023-05-17 16:11:52.923772', '9635236517', ''),
(19, 'pbkdf2_sha256$260000$0fNm2k7Gbn0ryhWysWsD7A$tjTcdKmDOED6DSvxI3+NkApr5xUbrCBcXOWW8RGjp3k=', '2023-05-17 16:24:54.880637', 0, 'asdfg', 'asdfg', 'asdfg', 'asdfg@gmail.com', 0, 1, '2023-05-17 16:23:39.737364', '1234567890', ''),
(20, 'pbkdf2_sha256$260000$8I5XapQn9RPHmZJXGv5cUS$4XStOAJy/ilZKUKsIvRlks8M+gMCVGWXuakU+k2E6gU=', NULL, 0, 'Apur', 'Are', 'Sa', 'apu@gmail.com', 0, 1, '2023-05-18 09:18:05.548000', '8563241758', ''),
(21, 'pbkdf2_sha256$260000$e3xJZ3NakV606aEiDwiaY7$raY/gLjCWTspiFemOMUQ/YxGFVjm+AWdCs+a7ccwjvQ=', NULL, 0, 'apyrbb', 'Raju', 'Pal', 'raju@gmil.com', 0, 1, '2023-05-18 09:22:04.362311', '1234567890', ''),
(22, 'pbkdf2_sha256$260000$8aMP6GZshXjFffVkwardcS$vy6DRg5OPJV83+JOOCpQHeItb3m4GK1WHZK10hQz+lA=', NULL, 0, 'Apurba12', 'Apurba', 'sau', 'apu@gmail.com', 0, 1, '2023-05-18 14:28:49.081376', '9635236517', ''),
(23, 'pbkdf2_sha256$260000$qz7xQhDlMkCqh3s78gj2EA$Lj8Q8X4JCIO3knH1FU6VXmet03Jfzf1xo+w2QjTRHJM=', NULL, 0, 'Apurba123', 'Apurba', 'sau', 'apu@gmail.com', 0, 1, '2023-05-18 14:29:22.387496', '9635236517', ''),
(24, 'pbkdf2_sha256$260000$SSoXy1LcKdI0RZksPL0zCE$5zKThwRUszLFDsjghZNU6rEk0gVRym9eDWReA9rfvGY=', NULL, 0, 'Apurba@22', 'Apurba', 'sau', 'apu@gmail.com', 0, 1, '2023-05-18 14:31:59.986485', '9635236517', ''),
(25, 'pbkdf2_sha256$260000$qkwmI6sVlCqdhQHSv2NQAq$3qUXZ05jf3iEhbCJzqLnJpaKcqtAQ1VgRbJIVgf60i8=', NULL, 0, 'Apurba@223', 'Apurba', 'sau', 'apu@gmail.com', 0, 1, '2023-05-18 14:32:45.297449', '9635236517', ''),
(26, 'pbkdf2_sha256$260000$uKqHMW9PXJ6XZNQdCWAIWH$v2NMf9sj4eLOG43SchYSmnA391nwAzgmuJWraEWz6Q4=', NULL, 0, 'sonay', 'sonay', 'sau', 'sonay@gmail.com', 0, 1, '2023-05-18 14:34:25.581488', '895674123', ''),
(27, 'pbkdf2_sha256$260000$UvxqYbxleV3r4sMVcDF0gu$OPR0lk2iuqF0IZpKKpsYyNYdUMyc9oigGUFHm79WArg=', NULL, 0, 'sonay2', 'sonay', 'sau', 'sonay@gmail.com', 0, 1, '2023-05-18 14:35:36.858288', '895674123', ''),
(28, 'pbkdf2_sha256$260000$osZkSLGbbm7uJWNOCX7lne$txTxGSOGBHEg6DQCvxx0Do1AFQm0rWD+pjWO6SmLUY8=', NULL, 0, 'sonay22', 'sonay', 'sau', 'sonay@gmail.com', 0, 1, '2023-05-18 14:37:02.194303', '895674123', ''),
(29, 'pbkdf2_sha256$260000$9Kfl1y8QWoffxUmo0C2pI7$MxA0+TBegmTi+Q5/J0WPpsx9i+k222d4HeFzyAv12XM=', NULL, 0, 'Sonay111', 'sonay', 'sau', 'apurbasau2003@gamil.com', 0, 1, '2023-05-18 14:39:22.083838', '7569841230', ''),
(30, 'pbkdf2_sha256$260000$W27k8eNFP3nANYKNL8z41t$Y+HNKLzmvQgpe7pT53i69PN7eW0mfy8DulSpheD+f40=', NULL, 0, 'Sonay1114', 'sonay', 'sau', 'apurbasau2003@gamil.com', 0, 1, '2023-05-18 14:40:44.490565', '7569841230', ''),
(31, 'pbkdf2_sha256$260000$53Eid6R2E1dO5zr1enklhF$lPrN0W0oqSxc242keK1emqsS7ImNb2cpviMF74IPr8I=', NULL, 0, 'Sonay114', 'sonay', 'sau', 'apurbasau2003@gamil.com', 0, 1, '2023-05-18 14:41:39.906859', '7569841230', ''),
(32, 'pbkdf2_sha256$260000$WFQbtGY7ZOg7mgQuJgXFsm$eHhUwPJfD/H8/4AUYpKiv7z864kyOGgjfN2S67OEXOQ=', NULL, 0, 'Apurba007', 'Apurbasau', '1', 'apurba@gmail.com', 0, 1, '2023-05-21 02:25:46.954036', '8523697410', '');

-- --------------------------------------------------------

--
-- Table structure for table `main_customuser_groups`
--

CREATE TABLE `main_customuser_groups` (
  `id` bigint(20) NOT NULL,
  `customuser_id` bigint(20) NOT NULL,
  `group_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `main_customuser_user_permissions`
--

CREATE TABLE `main_customuser_user_permissions` (
  `id` bigint(20) NOT NULL,
  `customuser_id` bigint(20) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `main_question`
--

CREATE TABLE `main_question` (
  `id` bigint(20) NOT NULL,
  `question` varchar(250) NOT NULL,
  `op1` varchar(250) NOT NULL,
  `op2` varchar(250) NOT NULL,
  `op3` varchar(250) NOT NULL,
  `op4` varchar(250) NOT NULL,
  `ans` varchar(250) NOT NULL,
  `sub_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `main_question`
--

INSERT INTO `main_question` (`id`, `question`, `op1`, `op2`, `op3`, `op4`, `ans`, `sub_id`) VALUES
(1, 'Who is father of c language', 'Steve Jobs', 'James Gosling', 'Dennis Ritchie', 'Rasmus Leedof', 'Dennis Ritchie', 1),
(2, 'Which of the following cannot be a variable name in c', 'volatile', 'true', 'friend', 'export', 'volatile', 1);

-- --------------------------------------------------------

--
-- Table structure for table `main_subject`
--

CREATE TABLE `main_subject` (
  `sub_id` int(11) NOT NULL,
  `sub_name` varchar(255) NOT NULL,
  `sub_img` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `main_subject`
--

INSERT INTO `main_subject` (`sub_id`, `sub_name`, `sub_img`) VALUES
(1, 'English', 'upload/English-Language-Level-System.jpg'),
(2, 'Mathemathics', 'upload/math.jpg'),
(3, 'History', 'upload/work-history-section-1024x683.jpg'),
(4, 'Geography', 'upload/geography_ball_300.jpg'),
(5, 'Science', 'upload/hand-drawn-science-education-background_23-2148499325.jpg');

-- --------------------------------------------------------

--
-- Table structure for table `main_subjectdetails`
--

CREATE TABLE `main_subjectdetails` (
  `sub_det_id` int(11) NOT NULL,
  `sub_cont` longtext NOT NULL,
  `sub_module_id` int(11) NOT NULL,
  `subject_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `main_subjectdetails`
--

INSERT INTO `main_subjectdetails` (`sub_det_id`, `sub_cont`, `sub_module_id`, `subject_id`) VALUES
(1, 'hiiiii', 2, 1),
(2, 'ghkfghikfyui', 1, 1);

-- --------------------------------------------------------

--
-- Table structure for table `main_subjectmodules`
--

CREATE TABLE `main_subjectmodules` (
  `sub_module_id` int(11) NOT NULL,
  `module_name` varchar(255) NOT NULL,
  `module_desc` longtext NOT NULL,
  `subject_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `main_subjectmodules`
--

INSERT INTO `main_subjectmodules` (`sub_module_id`, `module_name`, `module_desc`, `subject_id`) VALUES
(1, 'Module1', 'Sample text', 1),
(2, 'Module 2', 'hello', 1),
(5, 'class 10', '1. Quadratic Equations with one variable', 2),
(6, 'class 10', '2. Simple Interest', 2),
(7, 'class 10', '3. Theorems related to circle', 2),
(8, 'class 10', '4. Rectangular parallelopiped or Cuboid', 2),
(9, 'class 10', '5. Ratio and Proportion', 2),
(10, 'class 10', '6. Compound Interest and Uniform Rate of Increase or Decrease', 2),
(11, 'class 10', '7. Theorems related to Angles in a Circle', 2),
(12, 'class 10', '8. Right Circular Cylinder', 2),
(13, 'class 10', '9. Quadratic Surd', 2),
(14, 'class 10', '10.  Theorems related to Cyclic Quadrilateral', 2),
(15, 'class 10', '1. Father\'s help', 1),
(16, 'class 10', '2. Fable', 1),
(17, 'class 10', '3. The Passing Away of Bapu', 1),
(18, 'class 10', '4.  My Own True Family', 1),
(19, 'class 10', '5. Our Runaway Kite', 1),
(20, 'class 10', '6. Sea Fever', 1),
(21, 'class 10', '7. The Cat', 1),
(22, 'class 10', '8. The Snail', 1),
(23, 'class 10', '1. Concept of History', 3),
(24, 'class 10', '2. Reformation features and Reviews', 3),
(25, 'class 10', '3. Resistance and rebellion', 3),
(26, 'class 10', '4. About the beginning of the association', 3),
(27, 'class 10', '5.  Alternative Thoughts and Initiatives ( Middle Ninteenth to Early TwentiethCentury)', 3),
(28, 'class 10', '6. Peasants, Labor and Leftist Movements 20th Century India', 3),
(29, 'class 10', '7. Women, Students and marginalized Movements in 20th Century India', 3),
(30, 'class 10', '8. Post-Colonial India', 3),
(31, 'class 10', '1. External processes and the landforms created by them', 4),
(32, 'class 10', '2. The atmosphere', 4),
(33, 'class 10', '3. Barimodol', 4),
(34, 'class 10', '4. Waste Management', 4),
(35, 'class 10', '5. India-Natural Environment', 4),
(36, 'class 10', '6. India-Economic Environment', 4),
(37, 'class 10', '7.  Satellite images and geodesic maps', 4);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `auth_group`
--
ALTER TABLE `auth_group`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `name` (`name`);

--
-- Indexes for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  ADD KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`);

--
-- Indexes for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`);

--
-- Indexes for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD PRIMARY KEY (`id`),
  ADD KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  ADD KEY `django_admin_log_user_id_c564eba6_fk_main_customuser_id` (`user_id`);

--
-- Indexes for table `django_content_type`
--
ALTER TABLE `django_content_type`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`);

--
-- Indexes for table `django_migrations`
--
ALTER TABLE `django_migrations`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `django_session`
--
ALTER TABLE `django_session`
  ADD PRIMARY KEY (`session_key`),
  ADD KEY `django_session_expire_date_a5c62663` (`expire_date`);

--
-- Indexes for table `main_contact`
--
ALTER TABLE `main_contact`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `main_customuser`
--
ALTER TABLE `main_customuser`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`);

--
-- Indexes for table `main_customuser_groups`
--
ALTER TABLE `main_customuser_groups`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `main_customuser_groups_customuser_id_group_id_8a5023dd_uniq` (`customuser_id`,`group_id`),
  ADD KEY `main_customuser_groups_group_id_8149f607_fk_auth_group_id` (`group_id`);

--
-- Indexes for table `main_customuser_user_permissions`
--
ALTER TABLE `main_customuser_user_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `main_customuser_user_per_customuser_id_permission_06a652d8_uniq` (`customuser_id`,`permission_id`),
  ADD KEY `main_customuser_user_permission_id_38e6f657_fk_auth_perm` (`permission_id`);

--
-- Indexes for table `main_question`
--
ALTER TABLE `main_question`
  ADD PRIMARY KEY (`id`),
  ADD KEY `main_question_sub_id_28fc0cef_fk_main_subject_sub_id` (`sub_id`);

--
-- Indexes for table `main_subject`
--
ALTER TABLE `main_subject`
  ADD PRIMARY KEY (`sub_id`),
  ADD UNIQUE KEY `main_subject_sub_name_dd2dc674_uniq` (`sub_name`);

--
-- Indexes for table `main_subjectdetails`
--
ALTER TABLE `main_subjectdetails`
  ADD PRIMARY KEY (`sub_det_id`),
  ADD KEY `main_subjectdetails_sub_module_id_fe9d23b3_fk_main_subj` (`sub_module_id`),
  ADD KEY `main_subjectdetails_subject_id_b73f2983_fk_main_subject_sub_id` (`subject_id`);

--
-- Indexes for table `main_subjectmodules`
--
ALTER TABLE `main_subjectmodules`
  ADD PRIMARY KEY (`sub_module_id`),
  ADD KEY `main_subjectmodules_subject_id_e4ac419c_fk_main_subject_sub_id` (`subject_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `auth_group`
--
ALTER TABLE `auth_group`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_permission`
--
ALTER TABLE `auth_permission`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=45;

--
-- AUTO_INCREMENT for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=88;

--
-- AUTO_INCREMENT for table `django_content_type`
--
ALTER TABLE `django_content_type`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=12;

--
-- AUTO_INCREMENT for table `django_migrations`
--
ALTER TABLE `django_migrations`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=23;

--
-- AUTO_INCREMENT for table `main_contact`
--
ALTER TABLE `main_contact`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=46;

--
-- AUTO_INCREMENT for table `main_customuser`
--
ALTER TABLE `main_customuser`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=34;

--
-- AUTO_INCREMENT for table `main_customuser_groups`
--
ALTER TABLE `main_customuser_groups`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `main_customuser_user_permissions`
--
ALTER TABLE `main_customuser_user_permissions`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `main_question`
--
ALTER TABLE `main_question`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `main_subject`
--
ALTER TABLE `main_subject`
  MODIFY `sub_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- AUTO_INCREMENT for table `main_subjectdetails`
--
ALTER TABLE `main_subjectdetails`
  MODIFY `sub_det_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `main_subjectmodules`
--
ALTER TABLE `main_subjectmodules`
  MODIFY `sub_module_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=38;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`);

--
-- Constraints for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`);

--
-- Constraints for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  ADD CONSTRAINT `django_admin_log_user_id_c564eba6_fk_main_customuser_id` FOREIGN KEY (`user_id`) REFERENCES `main_customuser` (`id`);

--
-- Constraints for table `main_customuser_groups`
--
ALTER TABLE `main_customuser_groups`
  ADD CONSTRAINT `main_customuser_grou_customuser_id_13869e25_fk_main_cust` FOREIGN KEY (`customuser_id`) REFERENCES `main_customuser` (`id`),
  ADD CONSTRAINT `main_customuser_groups_group_id_8149f607_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`);

--
-- Constraints for table `main_customuser_user_permissions`
--
ALTER TABLE `main_customuser_user_permissions`
  ADD CONSTRAINT `main_customuser_user_customuser_id_34d37f86_fk_main_cust` FOREIGN KEY (`customuser_id`) REFERENCES `main_customuser` (`id`),
  ADD CONSTRAINT `main_customuser_user_permission_id_38e6f657_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`);

--
-- Constraints for table `main_question`
--
ALTER TABLE `main_question`
  ADD CONSTRAINT `main_question_sub_id_28fc0cef_fk_main_subject_sub_id` FOREIGN KEY (`sub_id`) REFERENCES `main_subject` (`sub_id`);

--
-- Constraints for table `main_subjectdetails`
--
ALTER TABLE `main_subjectdetails`
  ADD CONSTRAINT `main_subjectdetails_sub_module_id_fe9d23b3_fk_main_subj` FOREIGN KEY (`sub_module_id`) REFERENCES `main_subjectmodules` (`sub_module_id`),
  ADD CONSTRAINT `main_subjectdetails_subject_id_b73f2983_fk_main_subject_sub_id` FOREIGN KEY (`subject_id`) REFERENCES `main_subject` (`sub_id`);

--
-- Constraints for table `main_subjectmodules`
--
ALTER TABLE `main_subjectmodules`
  ADD CONSTRAINT `main_subjectmodules_subject_id_e4ac419c_fk_main_subject_sub_id` FOREIGN KEY (`subject_id`) REFERENCES `main_subject` (`sub_id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
