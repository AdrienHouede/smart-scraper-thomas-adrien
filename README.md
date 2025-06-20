# 📊 Terrasses à Paris - Scraping OpenData

Projet full-stack de collecte et visualisation de données issues de l’Open Data de la Ville de Paris, avec un backend en Flask, une base MySQL, et une interface React.

---

## 🧠 Objectif du projet

Développer une application complète permettant de :

- Collecter automatiquement des données publiques depuis le site [https://opendata.paris.fr](https://opendata.paris.fr),
- Les stocker dans une base de données relationnelle,
- Les exposer via une API REST,
- Les afficher et filtrer sur une interface web responsive.

---

## 🛠️ Technologies utilisées

- **Python 3**, **Flask**, **SQLAlchemy**
- **MySQL** via **Docker**
- **React.js** pour le frontend
- **Docker & Docker Compose** pour le déploiement
- **API OpenData Paris**

---

## 🗂️ Arborescence du projet

terrasses-paris/
├── backend/
│ ├── scraper.py
│ ├── app.py
│ ├── models.py
│ ├── requirements.txt
│ └── Dockerfile
├── frontend/
│ ├── public/
│ ├── src/
│ ├── package.json
│ └── Dockerfile
├── docker-compose.yml
└── README.md


---

## 🚀 Fonctionnalités

### ✅ Backend (Flask + MySQL)

- Scraping automatique via l’API OpenData Paris
- ORM avec SQLAlchemy
- API REST :
  - `GET /api/data` – liste complète
  - `GET /api/data/<filtre>?value=xxx` – filtrage dynamique
  - `POST /api/scrape` – relance manuelle du scraper
- Gestion des erreurs + CORS

### ✅ Frontend (React)

- Affichage sous forme de tableau responsive
- Filtre par arrondissement
- Requête fetch vers l’API Flask
- Design minimaliste adapté au mobile

### ✅ Dockerisation

- Conteneurisation du backend, frontend et base de données
- Lancement complet via Docker Compose

---

## ⚙️ Installation

### Prérequis

- [Docker](https://www.docker.com/)
- [Docker Compose](https://docs.docker.com/compose/)

### Étapes

1. Cloner le projet :
```bash
git clone https://github.com/AdrienHouede/smart-scraper-thomas-adrien.git
```

2. Lancer l'infrastructure :
```bash
docker-compose up -d --build
```

## 📦 Exemple de requêtes

### GET /api/data
➤ Retourne toutes les terrasses enregistrées.

### GET /api/data/arrondissement?value=75018
➤ Retourne les terrasses dans le 18e arrondissement.

### POST /api/scrape
➤ Déclenche le scraping (à utiliser avec précaution).

## 📄 Licence et données
Les données utilisées proviennent du portail OpenData Paris.
Licence : Licence Ouverte 2.0 – Etalab
➡️ [Consulter la licence](https://www.etalab.gouv.fr/licence-ouverte-open-licence)

## 📸 Captures d’écran
![Capture d'écran de l'interface](/screenshots/react.png)
![Capture d'écran de l'API](/screenshots/flask.png)

## ✨ Auteurs
- Adrien HOUEDE
- Thomas BIZET