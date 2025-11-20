# 1) Image de base
FROM python:3.11-slim

# 2) Répertoire de travail
WORKDIR /app

# 3) Copier les fichiers de dépendances
COPY requirements.txt .

# 4) Installer les dépendances
RUN pip install --no-cache-dir -r requirements.txt

# 5) Copier le reste des fichiers (API + modèle)
COPY app.py .
COPY model.joblib .

# 6) Exposer le port
# Render utilise la variable d'env PORT (par défaut 10000) :contentReference[oaicite:1]{index=1}
ENV PORT=10000
EXPOSE 10000

# 7) Commande de démarrage
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "10000"]
