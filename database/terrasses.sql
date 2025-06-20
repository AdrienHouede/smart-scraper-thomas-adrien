CREATE DATABASE IF NOT EXISTS paris_scraping;
USE paris_scraping;

CREATE TABLE IF NOT EXISTS terrasses (
    id INT AUTO_INCREMENT PRIMARY KEY,
    typologie VARCHAR(255),
    adresse VARCHAR(255),
    arrondissement VARCHAR(50),
    nom_enseigne VARCHAR(255),
    longueur FLOAT,
    largeur FLOAT,
    lien_affichette TEXT,
    UNIQUE (nom_enseigne, adresse, arrondissement)
);