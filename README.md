# 🚀 AI vs Human Text Detection API

API REST développée avec **FastAPI** permettant de prédire si un texte a été rédigé
par un **humain** ou généré par une **IA**, à l’aide d’un modèle de Machine Learning
pré-entraîné.

Ce projet illustre la **mise en production d’un modèle ML** sous forme d’API,
avec une attention portée à la clarté, la reproductibilité et l’exploitation des données.

---

## 🎯 Objectif du projet

- Servir un modèle de Machine Learning via une API REST
- Gérer des entrées structurées et des sorties interprétables
- Fournir une base exploitable pour un déploiement en environnement cloud
- Illustrer des compétences Data / ML orientées production

---

## 🏗 Architecture
Client
↓
FastAPI (API REST)
↓
Validation Pydantic
↓
Transformation Pandas (DataFrame)
↓
Modèle ML (joblib)
↓
Prédiction + probabilités
↓
Réponse JSON


### Diagramme d’architecture

```mermaid
flowchart LR
  A[Client\nBrowser / Postman / Script] -->|POST /predict| B[FastAPI]
  B --> C[Pydantic\nValidation]
  C --> D[Pandas\nDataFrame]
  D --> E[ML Model\nmodel.joblib]
  E -->|predict| F[Classe 0/1]
  E -->|predict_proba| G[Probabilités]
  F --> H[Réponse JSON]
  G --> H
  H --> A

