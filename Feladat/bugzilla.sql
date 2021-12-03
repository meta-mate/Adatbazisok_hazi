-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Dec 04, 2021 at 12:49 AM
-- Server version: 10.4.22-MariaDB
-- PHP Version: 8.0.13

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `bugzilla`
--

-- --------------------------------------------------------

--
-- Table structure for table `fejleszto`
--

CREATE TABLE `fejleszto` (
  `nev` varchar(32) COLLATE utf8_hungarian_ci NOT NULL,
  `id` int(11) NOT NULL,
  `email` varchar(48) COLLATE utf8_hungarian_ci NOT NULL,
  `csatlakozas` date NOT NULL,
  `szerepkorok` varchar(32) COLLATE utf8_hungarian_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_hungarian_ci;

--
-- Dumping data for table `fejleszto`
--

INSERT INTO `fejleszto` (`nev`, `id`, `email`, `csatlakozas`, `szerepkorok`) VALUES
('Lydia Thomas', 1, 'lydiathomas@gmail.com', '2017-01-01', 'A szekció'),
('Sophia Parker', 2, 's.parker@randatmail.com\n', '2017-02-03', 'A szekció'),
('Sam Robinson', 3, 's.robinson@randatmail.com\n', '2017-02-02', 'A szekció'),
('Edwin Gibson', 4, 'e.gibson@randatmail.com\n', '2017-05-20', 'A szekció'),
('Arianna Henderson', 5, 'a.henderson@randatmail.com\n', '2017-01-01', 'A szekció'),
('Alan Wilson', 6, '	a.wilson@randatmail.com', '2018-08-01', 'B szekció'),
('Elian Johnston', 7, 'e.johnston@randatmail.com', '2018-06-30', 'B szekció'),
('John Roberts', 8, 'j.roberts@randatmail.com\n', '2015-03-14', 'B szekció'),
('Ada Rogers', 9, 'a.rogers@randatmail.com\n', '2015-11-11', 'B szekció'),
('Adele Owens', 10, 'a.owens@randatmail.com\n', '2018-04-22', 'B szekció'),
('Adele Owens', 11, 'a.owens@randatmail.com\n', '2019-09-01', 'C szekció'),
('Byron Russell', 12, 'b.russell@randatmail.com\n', '2019-09-10', 'C szekció'),
('Violet Hall', 13, 'v.hall@randatmail.com\n', '2019-09-20', 'C szekció'),
('Olivia Carter', 14, 'o.carter@randatmail.com', '2017-05-01', 'C szekció'),
('Nicole Casey', 15, 'n.casey@randatmail.com\n', '2019-07-01', 'C szekció'),
('Miley Watson', 16, 'm.watson@randatmail.com\n', '2021-04-01', 'D szekció'),
('Vincent Richardson', 17, 'v.richardson@randatmail.com', '2020-03-05', 'D szekció'),
('Aiden Wright', 18, '2021-06-11', '0000-00-00', 'D szekció'),
('William Lloyd', 19, 'w.lloyd@randatmail.com', '2021-11-12', 'D szekció'),
('Emma Parker', 20, 'e.parker@randatmail.com\n', '2020-01-19', 'D szekció');

-- --------------------------------------------------------

--
-- Table structure for table `hibajelentes`
--

CREATE TABLE `hibajelentes` (
  `jelentesi_ido` datetime NOT NULL,
  `leiras` text COLLATE utf8_hungarian_ci NOT NULL,
  `id` int(11) NOT NULL,
  `nev` varchar(32) COLLATE utf8_hungarian_ci NOT NULL,
  `verzio` varchar(16) COLLATE utf8_hungarian_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_hungarian_ci;

--
-- Dumping data for table `hibajelentes`
--

INSERT INTO `hibajelentes` (`jelentesi_ido`, `leiras`, `id`, `nev`, `verzio`) VALUES
('2017-05-02 00:00:00', 'FELETTÉBB HIBÁS ÁM!', 8, 'launcher', '1.0'),
('2017-06-02 00:00:00', 'hiba-hiba-hiba (robothangon)', 12, 'launcher', '1.1.1'),
('2018-01-02 00:00:00', 'háde mi leheta baja', 1, 'tesztprog', '2.0'),
('2018-05-02 00:00:00', 'ÚJ SOK ÚJ HIBÁVAL! KIJAVÍTANI!!4!', 8, 'launcher', '1.1'),
('2019-01-01 00:00:01', 'valamiért nem működik', 2, 'tesztprog', '1.1'),
('2019-01-02 00:00:00', 'háde nem műkszik', 4, 'tesztprog', '1.1'),
('2019-07-02 05:00:00', 'én nem tudom miez denézdmeg hogy csillog', 4, 'főprogram', '1.0'),
('2019-11-02 12:00:00', 'ömm szerintem ez szétszakítja az univerzumot', 14, 'főprogram', '1.1'),
('2020-06-05 00:00:00', 'nem működik', 5, 'tesztprog', '1.0'),
('2021-06-02 05:00:00', 'felháborító! tűntessék el a szemem elől ezt! pfujj', 16, 'launcher', '1.2'),
('2088-06-05 00:00:00', 'az univerzum megeszi magát és Cthulhu szerint hagyjuk abba', 20, 'főprogram', '2.0');

-- --------------------------------------------------------

--
-- Table structure for table `javitas`
--

CREATE TABLE `javitas` (
  `changelog` text COLLATE utf8_hungarian_ci NOT NULL,
  `javitasi_ido` datetime NOT NULL,
  `leiras` text COLLATE utf8_hungarian_ci NOT NULL,
  `bejelento_id` int(11) NOT NULL,
  `jelentesi_ido` datetime NOT NULL,
  `nev` varchar(32) COLLATE utf8_hungarian_ci NOT NULL,
  `verzio` varchar(16) COLLATE utf8_hungarian_ci NOT NULL,
  `javito_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_hungarian_ci;

--
-- Dumping data for table `javitas`
--

INSERT INTO `javitas` (`changelog`, `javitasi_ido`, `leiras`, `bejelento_id`, `jelentesi_ido`, `nev`, `verzio`, `javito_id`) VALUES
('pár dolog', '2020-06-05 00:00:00', 'mostmar igen', 5, '2020-06-05 00:00:00', 'tesztprog', '1.0', 6),
('pár cucclé hibás volt', '2019-01-01 00:00:05', 'mostmár minden 999%-ban rendben', 2, '2019-01-01 00:00:01', 'tesztprog', '1.1', 6),
('na jólvan azért volt benne még hiba', '2019-01-02 00:00:09', 'csak higgy benne', 4, '2019-01-02 00:00:00', 'tesztprog', '1.1', 6),
('bele kellett rugdosni azt ment is', '2018-01-02 01:00:00', 'mintha uj lenne csakpersze nemhibákkal ahaha', 1, '2018-01-02 00:00:00', 'tesztprog', '2.0', 11),
('hihi nem volt nagy cucc (SZERETLEK)', '2017-06-02 00:00:00', 'b-b-bocsi én megoldottam köcsög-senpai', 8, '2017-05-02 00:00:00', 'launcher', '1.0', 7),
('belerajzoltam szivecskéket neked (NÉZD MEG)', '2017-05-02 00:50:05', 'mind megoldva :3 kérlek nézz rám', 8, '2017-05-02 00:00:00', 'launcher', '1.1', 7),
('HIBA EXTERMINÁLÁSA', '2017-06-02 00:00:01', 'kijavítva bip bup (android füttyel a végén)', 12, '2017-06-02 00:00:00', 'launcher', '1.1.1', 17),
('Angard! nagyerecsakide', '2021-06-02 05:00:10', 'kivégeztem ezt a felettébb piszkos hibát', 16, '2021-06-02 05:00:00', 'launcher', '1.2', 11),
('kérlek javítsd meg magad', '2019-07-02 05:00:11', 'elfogadott engem megjavítójaként uramatyám', 4, '2019-07-02 05:00:00', 'főprogram', '1.0', 2),
('nincs felem, van klónom, nincs realitásszakadás', '2019-11-02 14:00:00', 'beszippantotta az egyik felem, de így bezártam a portált, és lett egy klónom', 14, '2019-11-02 12:00:00', 'főprogram', '1.1', 2),
('csak egy ; hiányzott :)', '2159-06-05 00:00:00', 'kijavítva!', 20, '2088-06-05 00:00:00', 'főprogram', '2.0', 1);

-- --------------------------------------------------------

--
-- Table structure for table `szoftver`
--

CREATE TABLE `szoftver` (
  `nev` varchar(32) COLLATE utf8_hungarian_ci NOT NULL,
  `verzio` varchar(16) COLLATE utf8_hungarian_ci NOT NULL,
  `leiras` text COLLATE utf8_hungarian_ci DEFAULT NULL,
  `changelog` text COLLATE utf8_hungarian_ci DEFAULT NULL,
  `elozo_verzio` varchar(16) COLLATE utf8_hungarian_ci DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_hungarian_ci;

--
-- Dumping data for table `szoftver`
--

INSERT INTO `szoftver` (`nev`, `verzio`, `leiras`, `changelog`, `elozo_verzio`) VALUES
('főprogram', '1.0', 'polinomiális időben old meg np feladatokat', '', ''),
('főprogram', '1.1', 'p = np, gödel teljesíthetetlenségességtelen is', 'mostmár igaz, hogy ez a mondat nem igaz', '1.0'),
('főprogram', '2.0', '(p=np)==(p!=np), lekövetkezteti a lekövetkeztetést', 'kombinálva lett a kombináció. frankeinstein életrekelt', '1.1'),
('launcher', '1.0', 'a program indítófelülete', '', ''),
('launcher', '1.1', 'a program indítófelülete', 'design változtatások', '1.0'),
('launcher', '1.1.1', 'a program indítófelülete', 'design visszaállítása', '1.1'),
('launcher', '1.2', 'a program kezelő és indítófelülete', 'kezelési opciók áthelyezve az indítófelületbe', '1.1.1'),
('tesztprog', '1.0', 'főprogram 1.0-át teszteli', '', ''),
('tesztprog', '1.1', 'főprogram 1.0 és 1.1-et teszteli', '1.1 tesztek', '1.0'),
('tesztprog', '2.0', 'főprogram 1.0 , 1.1 és 2.0-et teszteli', '2.0 tesztek', '1.1');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `fejleszto`
--
ALTER TABLE `fejleszto`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `hibajelentes`
--
ALTER TABLE `hibajelentes`
  ADD PRIMARY KEY (`jelentesi_ido`),
  ADD KEY `hiba_helye` (`nev`,`verzio`),
  ADD KEY `bejelento` (`id`);

--
-- Indexes for table `javitas`
--
ALTER TABLE `javitas`
  ADD KEY `javito` (`javito_id`),
  ADD KEY `javitas` (`nev`,`verzio`),
  ADD KEY `jelentes` (`bejelento_id`,`jelentesi_ido`);

--
-- Indexes for table `szoftver`
--
ALTER TABLE `szoftver`
  ADD PRIMARY KEY (`nev`,`verzio`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `fejleszto`
--
ALTER TABLE `fejleszto`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=21;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `hibajelentes`
--
ALTER TABLE `hibajelentes`
  ADD CONSTRAINT `bejelento` FOREIGN KEY (`id`) REFERENCES `fejleszto` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `hiba_helye` FOREIGN KEY (`nev`,`verzio`) REFERENCES `szoftver` (`nev`, `verzio`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `javitas`
--
ALTER TABLE `javitas`
  ADD CONSTRAINT `javitas` FOREIGN KEY (`nev`,`verzio`) REFERENCES `szoftver` (`nev`, `verzio`),
  ADD CONSTRAINT `javito` FOREIGN KEY (`javito_id`) REFERENCES `fejleszto` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `jelentes` FOREIGN KEY (`bejelento_id`,`jelentesi_ido`) REFERENCES `hibajelentes` (`id`, `jelentesi_ido`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
