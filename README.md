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
```

### 3. Configurer les variables d'environnement

Les mots de passe et la clé JWT ne sont pas dans le code : ils sont lus depuis un fichier `.env` (non versionné).

```bash
cp .env.example .env
# puis remplir POSTGRES_PASSWORD et SECRET_KEY
python -c "import secrets; print(secrets.token_urlsafe(32))"   # génère une SECRET_KEY
```

### 4. Lancer l'application

```bash
docker compose up --build
```

## Structure du projet

```
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
└── .env.example              # Modèle des variables d'environnement (copier en .env)
```

## Authentification

L’API utilise une authentification **OAuth2 avec JWT**. La création, la modification et la suppression de produits exigent un jeton valide ; la lecture reste publique.

### Endpoints :
- `POST /produits/register` : création d'un utilisateur  
- `POST /produits/produits/login` : obtention du token JWT  
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
