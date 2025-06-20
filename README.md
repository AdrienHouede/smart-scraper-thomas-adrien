# 🎓 Projet de Scraping - Données ouvertes de Paris

## 📌 Source des données

Ce projet utilise les données disponibles sur le portail officiel de l’**Open Data de la Ville de Paris** :  
🔗 [https://opendata.paris.fr](https://opendata.paris.fr)

Le site propose un large éventail de jeux de données publics concernant la ville de Paris (urbanisme, transports, culture, environnement, etc.), accessibles via une interface web ou des API.

---

## 📜 Licence d’utilisation

Les données sont publiées sous la **Licence Ouverte 2.0** d’Etalab.

> **Extrait de la Licence Ouverte 2.0** :
>
> Vous êtes libres de :
> - **Reproduire, copier, adapter, modifier, extraire, réutiliser** et redistribuer les informations,
> - Y compris à des fins **commerciales**.
>
> Sous réserve de :
> - **Mentionner la paternité** de l’information (source, date de dernière mise à jour, etc.),
> - Ne pas induire en erreur les tiers quant au contenu, à la source ou à la date des données.

🔗 [Texte complet de la licence - Licence Ouverte 2.0 (Etalab)](https://www.etalab.gouv.fr/licence-ouverte-open-licence)

---

## ✅ Légalité de la collecte

La collecte de données via scraping ou via les API de [opendata.paris.fr](https://opendata.paris.fr) est **légale**, car :

- Les données sont **publiquement accessibles** et proposées à des fins de réutilisation.
- Le site promeut explicitement leur **réutilisation libre** via la Licence Ouverte.
- Le projet respecte les **conditions d’utilisation**, notamment :
  - La mention de la **source**,
  - L’absence de modification trompeuse du contenu,
  - Une utilisation **responsable** du scraping (pas de surcharge du site, respect des limites d’accès).

---

## Fonctionnalités réalisées

### Backend (Flask + SQLAlchemy + MySQL Docker)

- Mise en place d’une base MySQL dockerisée avec Docker Compose.  
- Création d’un schéma `terrasses` avec les colonnes :  
  `id`, `typologie`, `adresse`, `arrondissement`, `nom_enseigne`, `longueur`, `largeur`, `lien_affichette`.  
- Script de scraping `scraper.py` qui interroge l’API OpenData Paris pour récupérer les données terrasses et créer des objets SQLAlchemy.  
- Insertion des données dans la base via SQLAlchemy.  
- API REST avec Flask proposant :  
  - `GET /api/data` : renvoie toutes les terrasses.  
  - `GET /api/data/<filtre>?value=xxx` : filtre par champ (ex: arrondissement).  
  - `POST /api/scrape` : déclenchement manuel du scraper.  
- Gestion des erreurs et ajout de CORS pour permettre l’accès depuis un front web.

### Frontend (React.js)

- Interface web React minimaliste et responsive.  
- Affichage dynamique des données dans un tableau HTML.  
- Filtrage par arrondissement via un champ de recherche.  
- Requêtes fetch vers l’API Flask pour récupérer les données.  
- Design simple avec styles inline et adaptabilité mobile.

---

## Architecture et lancement

### Docker

- `docker-compose.yml` configure :  
  - MySQL  
  - Backend Flask (à ajouter si dockerisé)  
  - Frontend React (optionnel)

### Lancement manuel

- Lancer MySQL avec Docker :  
  ```bash
  docker-compose up -d mysql