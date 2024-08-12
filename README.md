# Projet Pokémon API #

# Description #

Ce projet est une API RESTful pour gérer des utilisateurs, des Pokémon, et des compétences associées. 
L'API a été construite avec Django et Django REST Framework. 
Ce projet est conçu pour permettre de créer, lire, mettre à jour et supprimer (CRUD) des enregistrements de Pokémon,de compétences mais aussi de gérer les utilisateurs.

Table des matières

1. Technologies utilisées
2. Structure du projet
3. Installation et configuration
4. Utilisation
5. Endpoints de l'API

# Configuration du Projet #

# 1. Technologies utilisées
Il y avait plusieurs moyens pour faire ce projet, mais j'ai préféré utiliser Django et SQLite qui en fait parti.

Django : Un framework web Python que j'ai utilisé pour construire l'API. Il est simple d'utilisation et facilement compréhensible.
Django REST Framework (DRF) : Un module de Django qui facilite la création d'APIs RESTful.
SQLite : La base de données par défaut qui est intégrée à Django.

# 2. Structure du projet
Voici un aperçu de la structure des fichiers du projet :

projet-pokemon/
│
├── backend/                 # Contient le code source principal de l'application Django
│   ├── api/                 # Contient les fichiers liés à l'API (modèles, vues, serializers)
│   │   ├── migrations/      # Contient les fichiers de migration de la base de données
│   │   ├── models.py        # Définit les modèles pour les utilisateurs, Pokémon, et compétences
│   │   ├── serializers.py   # Contient les serializers pour transformer les modèles en JSON
│   │   ├── urls.py          # Définit les routes de l'API
│   │   ├── views.py         # Contient la logique des vues (endpoints API)
│   ├── backend/             # Contient les fichiers de configuration principale de Django
│   │   ├── settings.py      # Les paramètres de configuration de l'application
│   │   ├── urls.py          # Les routes principales du projet
│   ├── manage.py            # Commande utilitaire pour gérer l'application Django
│
├── env/                     # Environnement virtuel pour isoler les dépendances Python
│
├── README.md                # Documentation du projet
├── requirements.txt         # Liste des dépendances Python nécessaires au projet



Clonez le projet depuis le dépôt Git :
```bash
git clone https://github.com/votreutilisateur/projet-pokemon.git
cd projet-pokemon
