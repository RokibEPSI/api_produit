# Mon api_produit  

## API Produits - *Paye Ton Kawa*

---

## Description

Cette API gère les produits de l'application **Paye Ton Kawa**.

### Fonctionnalités principales

- CRUD complet sur les produits  
- Base de données PostgreSQL  
- Authentification sécurisée via JWT (OAuth2 Password Bearer)  
- Déploiement via Docker et Docker Compose

---

## Architecture

- **Backend :** FastAPI (Python 3.11)  
- **Base de données :** PostgreSQL 15  
- **ORM :** SQLAlchemy  
- **Sécurité :** OAuth2 (JWT) via `python-jose`, `passlib`  
- **Conteneurisation :** Docker

---

## Installation

### 1. Prérequis

- Docker  
- Docker Compose  

### 2. Cloner le dépôt

```bash
git clone https://github.com/RokibEPSI/api_produit.git
cd api_produit
<<<<<<< HEAD
=======


>>>>>>> 82071559bf77a9e956fe16be6ddcc7404a346576

api_produit/
│
├── app/
│   ├── main.py           # Entrée FastAPI
│   ├── routes.py         # Routes API
│   ├── auth.py           # Authentification
│   ├── crud.py           # Logique métier
│   ├── schemas.py        # Schémas Pydantic
│   ├── models.py         # Modèles SQLAlchemy
│   └── database.py       # Connexion DB
│
├── Dockerfile
├── docker-compose.yml
└── requirements.txt
<<<<<<< HEAD

## Authentification
=======
```
# Authentification
L’API utilise une authentification OAuth2 avec JWT.
>>>>>>> 82071559bf77a9e956fe16be6ddcc7404a346576

L’API utilise une authentification **OAuth2 avec JWT**.

### Endpoints :
- `POST /produits/login` : obtention du token JWT  
- `GET /produits/produits-proteges/` : endpoint protégé nécessitant un token JWT valide

---

### Exemple de connexion

- `username` : (à créer via la table `users`)  
- `password` : (hashé avec `passlib`)

---

## Tests de l’API

Une interface Swagger est disponible ici :  
 [http://localhost:8001/docs](http://localhost:8001/docs)

### Pour tester les endpoints sécurisés :

1. Cliquer sur **Authorize** en haut à droite de Swagger.  
2. Entrer vos identifiants `username` et `password`.  
3. Swagger récupérera un **token JWT** et l’utilisera automatiquement pour tester les routes protégées.
