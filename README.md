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


api_produit/
│
├── app/
│   ├── __init__.py           # Fichier d'initialisation du module
│   ├── main.py               # Point d'entrée FastAPI
│   ├── routes.py             # Définition des routes API
│   ├── auth.py               # Gestion de l'authentification
│   ├── crud.py               # Logique métier (CRUD)
│   ├── schemas.py            # Schémas Pydantic (validation)
│   ├── models.py             # Modèles SQLAlchemy (ORM)
│   ├── database.py           # Connexion et configuration DB
│   └── dependencies.py       # Dépendances réutilisables (optionnel)
│   ├── event_bus.py
├── tests/
│   ├── __init__.py           # Initialisation des tests
│   ├── test_main.py          # Tests des endpoints principaux
│   └── test_auth.py          # Tests de l'authentification
│
├── Dockerfile                # Image Docker de l'API
├── docker-compose.yml        # Orchestration des services (API + DB)
├── requirements.txt          # Dépendances Python
├── README.md                 # Documentation du projet
└── .env                      # Variables d'environnement (à ne pas versionner)

## Authentification
=======
```
# Authentification
L’API utilise une authentification OAuth2 avec JWT.

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
