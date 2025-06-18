L’instance PostgreSQL est exposée sur le port 5440.

 Authentification
L’API utilise une authentification OAuth2 avec JWT.

Endpoints :
POST /produits/login : obtention du token JWT

GET /produits/produits-proteges/ : endpoint protégé nécessitant un token JWT valide

Exemple de connexion :
username : (à créer via la table users)

password : (hashé avec passlib)


Tests de l’API
Une interface Swagger est disponible ici :
http://localhost:8001/docs

Pour tester les endpoints sécurisés :

Cliquer sur Authorize en haut de Swagger.

Entrer username et password.

Swagger va récupérer un token JWT et l’utiliser automatiquement.

api_produit/
│
├── app/
│   ├── main.py          # Entrée FastAPI
│   ├── routes.py        # Routes API
│   ├── auth.py          # Authentification
│   ├── crud.py          # Logique métier
│   ├── schemas.py       # Schémas Pydantic
│   ├── models.py        # Modèles SQLAlchemy
│   └── database.py      # Connexion DB
│
├── Dockerfile
├── docker-compose.yml
└── requirements.txt
