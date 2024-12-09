-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 06-12-2024 a las 20:32:17
-- Versión del servidor: 10.4.32-MariaDB
-- Versión de PHP: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `kickstock`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `marcas`
--

CREATE TABLE `marcas` (
  `id_marca` int(11) NOT NULL,
  `nom_marca` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `marcas`
--

INSERT INTO `marcas` (`id_marca`, `nom_marca`) VALUES
(1, 'NIKE'),
(2, 'ADIDAS'),
(3, 'PUMA'),
(4, 'REEBOK');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `modelos`
--

CREATE TABLE `modelos` (
  `id_modelo` int(11) NOT NULL,
  `nom_modelo` varchar(100) NOT NULL,
  `precio` int(11) NOT NULL,
  `cantidad` int(11) NOT NULL,
  `genero` varchar(100) NOT NULL,
  `talla` int(11) NOT NULL,
  `id_marca` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `modelos`
--

INSERT INTO `modelos` (`id_modelo`, `nom_modelo`, `precio`, `cantidad`, `genero`, `talla`, `id_marca`) VALUES
(1, 'NIKE AIR MAX 90', 139990, 9, 'HOMBRE', 39, 1),
(2, 'NIKE AIR FORCE 1', 119990, 12, 'UNISEX', 36, 1),
(3, 'ADIDAS SOLAR GLIDE 5', 74990, 15, 'MUJER', 32, 2),
(4, 'ADIDAS SAMBA OG', 89990, 10, 'MUJER', 36, 2),
(5, 'PUMA SKYROCKET LITE', 39990, 13, 'HOMBRE', 39, 3),
(6, 'PUMA CALI', 25990, 14, 'HOMBRE', 26, 3),
(7, 'REEBOK FLOATRIDE ENERGY X', 119990, 17, 'UNISEX', 36, 4),
(8, 'REEBOK CLUB C 85', 72990, 20, 'HOMBRE', 39, 4);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `tipo_calzado`
--

CREATE TABLE `tipo_calzado` (
  `id_tipo_calzado` int(11) NOT NULL,
  `nom_tipo_calzado` varchar(100) NOT NULL,
  `id_modelo` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `tipo_calzado`
--

INSERT INTO `tipo_calzado` (`id_tipo_calzado`, `nom_tipo_calzado`, `id_modelo`) VALUES
(1, 'OUTDOOR', 1),
(2, 'CASUAL', 3),
(3, 'DEPORTIVO', 7),
(4, 'URBANO', 2);

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `marcas`
--
ALTER TABLE `marcas`
  ADD PRIMARY KEY (`id_marca`);

--
-- Indices de la tabla `modelos`
--
ALTER TABLE `modelos`
  ADD PRIMARY KEY (`id_modelo`),
  ADD KEY `id_marca` (`id_marca`);

--
-- Indices de la tabla `tipo_calzado`
--
ALTER TABLE `tipo_calzado`
  ADD PRIMARY KEY (`id_tipo_calzado`),
  ADD KEY `id_modelo` (`id_modelo`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `marcas`
--
ALTER TABLE `marcas`
  MODIFY `id_marca` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=13;

--
-- AUTO_INCREMENT de la tabla `modelos`
--
ALTER TABLE `modelos`
  MODIFY `id_modelo` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT de la tabla `tipo_calzado`
--
ALTER TABLE `tipo_calzado`
  MODIFY `id_tipo_calzado` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
