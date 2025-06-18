

---

## Objectif du projet

L’API Produits permet de gérer les opérations CRUD sur les produits dans le cadre du projet *Paye Ton Kawa*.
Elle intègre :

* Une base de données PostgreSQL.
* Une API REST développée en FastAPI.
* Une sécurité basée sur des tokens JWT.
* Un déploiement via Docker.

---

## Architecture technique

### Stack technique

| Composant         | Technologie                  |
| ----------------- | ---------------------------- |
| API               | FastAPI                      |
| ORM               | SQLAlchemy                   |
| Schéma de données | Pydantic                     |
| Authentification  | OAuth2 (Password Flow) + JWT |
| DB                | PostgreSQL 15                |
| Containerisation  | Docker & Docker Compose      |

### Organisation du code

```bash
app/
|
├── main.py          # Lancement de l'API FastAPI
├── routes.py        # Routes de l'API REST
├── auth.py          # Authentification et génération des tokens JWT
├── crud.py          # Logique métier (Create, Read, Update, Delete)
├── models.py        # Modèles de données SQLAlchemy
├── schemas.py       # Schémas de validation Pydantic
└── database.py      # Connexion à la base de données
```

---

## Base de données

### Tables principales

#### Table `products`

| Champ | Type  | Description        |
| ----- | ----- | ------------------ |
| id    | int   | Identifiant unique |
| name  | str   | Nom du produit     |
| price | float | Prix du produit    |

#### Table `users`

| Champ            | Type | Description        |
| ---------------- | ---- | ------------------ |
| id               | int  | Identifiant unique |
| username         | str  | Nom d’utilisateur  |
| hashed\_password | str  | Mot de passe hashé |

---

## Sécurité

L’API est sécurisée via OAuth2 Password avec des tokens JWT.

* **Connexion :**

  * Endpoint `/produits/login` permet d’obtenir un token JWT.

* **Accès aux endpoints protégés :**

  * Les endpoints nécessitant une authentification utilisent un `Bearer Token` via Swagger UI ou les headers HTTP.

* **Vérification des tokens :**

  * Le fichier `auth.py` contient la logique de génération et vérification des JWT.

### Exemples :

#### Générer un token :

```json
POST /produits/login
{
  "username": "admin",
  "password": "password123"
}
```

#### Utiliser le token dans les appels API protégés :

Header :

```
Authorization: Bearer <token>
```

---

## Endpoints principaux

| Méthode | Endpoint                       | Description                                |
| ------- | ------------------------------ | ------------------------------------------ |
| POST    | `/produits/`                   | Créer un produit                           |
| GET     | `/produits/`                   | Lister les produits                        |
| GET     | `/produits/{product_id}`       | Récupérer un produit                       |
| PUT     | `/produits/{product_id}`       | Mettre à jour un produit                   |
| DELETE  | `/produits/{product_id}`       | Supprimer un produit                       |
| POST    | `/produits/login`              | Authentification et génération du JWT      |
| GET     | `/produits/produits-proteges/` | Accès protégé nécessitant authentification |

---

## Déploiement

### Docker

#### Démarrage

```bash
docker-compose up --build
```

#### Composition des services

* **api-produit** : expose FastAPI sur `http://localhost:8001`
* **db** : expose PostgreSQL sur `localhost:5440`

---

## Améliorations possibles

* Gestion des rôles et permissions
* Endpoint d’inscription utilisateur
* Logging centralisé
* Tests automatisés
* CI/CD (GitHub Actions)

---
