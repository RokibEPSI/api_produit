# Mon api_produit
# API Produits - Paye Ton Kawa

## Description

Cette API gère les produits de l'application *Paye Ton Kawa*.

Fonctionnalités principales :
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

##  Installation

### 1 Prérequis

- Docker
- Docker Compose

###  Cloner le dépôt

```bash
git clone https://github.com/RokibEPSI/api_produit.git
cd api_produit
