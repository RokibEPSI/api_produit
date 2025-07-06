FROM python:3.11-slim

# Crée un dossier de travail
WORKDIR /code

# Installe les dépendances
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copie le code source dans /code/app
COPY ./app /code/app
COPY ./tests /code/tests

ENV PYTHONPATH=/code
# Démarre l'application avec uvicorn
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
