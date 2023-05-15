-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Hôte : db
-- Généré le : sam. 13 mai 2023 à 13:00
-- Version du serveur : 8.0.33
-- Version de PHP : 8.1.18

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de données : `binomotron_t2_bdd`
--

-- --------------------------------------------------------

--
-- Structure de la table `apprenants`
--

CREATE TABLE `apprenants` (
  `id_apprenant` int NOT NULL,
  `prenom` varchar(40) NOT NULL,
  `nom` varchar(40) NOT NULL,
  `mail` varchar(80) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Déchargement des données de la table `apprenants`
--

INSERT INTO `apprenants` (`id_apprenant`, `prenom`, `nom`, `mail`) VALUES
(1, 'Morgan', 'COULM', 'morgan.coulm@isen-ouest.yncrea.fr'),
(2, 'Camille', 'ULVOAS', 'camille.ulvoas@isen-ouest.yncrea.fr'),
(3, 'Yves', 'PAUL', 'yves.paul@isen-ouest.yncrea.fr'),
(4, 'Laura', 'PERTRON', 'laura.pertron@isen-ouest.yncrea.fr'),
(5, 'Frédéric', 'BOIREAU', 'frederic.boireau@isen-ouest.yncrea.fr'),
(6, 'Guillaume', 'CARDON', 'guillaume.cardon@isen-ouest.yncrea.fr'),
(7, 'Jonathan', 'NEEDHAM', 'jonathan.needham@isen-ouest.yncrea.fr'),
(8, 'Jérémy', 'LARDIC', 'jeremy.lardic@isen-ouest.yncrea.fr'),
(9, 'Mickaël', 'RENNARD', 'mickael.rennard@isen-ouest.yncrea.fr'),
(10, 'Ibrahim', 'MOHAMMAD', 'ibrahim.mohammad@isen-ouest.yncrea.fr'),
(11, 'Andy', 'DUBIGNY', 'andy.dubigny@isen-ouest.yncrea.fr'),
(12, 'Pierre-Marie', 'GUEVEL', 'pierre-marie.guevel@isen-ouest.yncrea.fr'),
(13, 'Youenn', 'FEULVARC’H', 'youenn.feulvarc-h@isen-ouest.yncrea.fr'),
(14, 'Gwendal', 'QUENET', 'gwendal.quenet@isen-ouest.yncrea.fr'),
(15, 'Alexandre', 'CARAES', 'alexandre.caraes@isen-ouest.yncrea.fr'),
(16, 'Bastien', 'SUCHY-REINARD', 'bastien.suchy-reinard@isen-ouest.yncrea.fr');

-- --------------------------------------------------------

--
-- Structure de la table `groupes`
--

CREATE TABLE `groupes` (
  `id_groupes` int NOT NULL,
  `libelle_groupe` varchar(60) NOT NULL,
  `date_creation_groupe` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Structure de la table `hub`
--

CREATE TABLE `hub` (
  `id_apprenant` int NOT NULL,
  `id_groupe` int NOT NULL,
  `id_projet` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Structure de la table `projets`
--

CREATE TABLE `projets` (
  `id_projet` int NOT NULL,
  `libelle_projet` varchar(60) NOT NULL,
  `debut_projet` date NOT NULL,
  `fin_projet` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Index pour les tables déchargées
--

--
-- Index pour la table `apprenants`
--
ALTER TABLE `apprenants`
  ADD PRIMARY KEY (`id_apprenant`);

--
-- Index pour la table `groupes`
--
ALTER TABLE `groupes`
  ADD PRIMARY KEY (`id_groupes`);

--
-- Index pour la table `projets`
--
ALTER TABLE `projets`
  ADD PRIMARY KEY (`id_projet`);

--
-- AUTO_INCREMENT pour les tables déchargées
--

--
-- AUTO_INCREMENT pour la table `apprenants`
--
ALTER TABLE `apprenants`
  MODIFY `id_apprenant` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=17;

--
-- AUTO_INCREMENT pour la table `groupes`
--
ALTER TABLE `groupes`
  MODIFY `id_groupes` int NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT pour la table `projets`
--
ALTER TABLE `projets`
  MODIFY `id_projet` int NOT NULL AUTO_INCREMENT;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
