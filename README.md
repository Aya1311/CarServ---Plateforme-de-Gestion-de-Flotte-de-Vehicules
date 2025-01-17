# CarServ - Gestion Intelligente de Flotte de Véhicules de Remplacement

CarServ est une application web innovante développée avec Django pour simplifier la gestion des flottes de véhicules de remplacement. Conçue pour répondre aux besoins des clients, employés et administrateurs, elle offre une solution intuitive, performante et sécurisée. Grâce à ses fonctionnalités avancées et son architecture robuste, CarServ optimise les processus de gestion et améliore l’expérience utilisateur.

## Table des Matières

- [Fonctionnalités](#fonctionnalités)
- [Architecture Technique](#architecture-technique)
- [Installation](#installation)
- [Utilisation](#utilisation)
- [Contributions](#contributions)
- [Auteurs](#auteurs)
- [Licence](#licence)

---

## Fonctionnalités

### Principales

- **Système de recommandation intelligent** :
  - Suggère des véhicules adaptés en fonction de l'âge du véhicule en panne, de la disponibilité et des préférences du client.
- **Gestion des utilisateurs et des accès** :
  - Espaces personnalisés et sécurisés pour clients, employés et administrateurs.
  - Système d'authentification robuste avec récupération de mot de passe.
- **Tableaux de bord dynamiques** :
  - Statistiques détaillées pour suivre les performances et optimiser la gestion de la flotte.
- **Mode sombre intuitif** :
  - Amélioration du confort visuel grâce à une conception moderne et personnalisable.

### Par rôle

- **Clients** :
  - Accès à une vue complète de leur parc de véhicules loués.
  - Demandes simplifiées de remplacement ou de services spécifiques.
  - Suivi détaillé de l'historique des demandes.

- **Employés** :
  - Gestion centralisée des demandes clients.
  - Visualisation et attribution rapide des véhicules disponibles.
  - Suivi efficace des véhicules assignés.

- **Administrateurs** :
  - Contrôle complet des comptes utilisateurs.
  - Accès aux statistiques clés via un tableau de bord interactif.

---

## Architecture Technique

CarServ repose sur Django et suit l’architecture MVC (Modèle-Vue-Contrôleur) pour une séparation claire des responsabilités :

- **Modèle (Model)** : Gestion des données (véhicules, utilisateurs, demandes).
- **Vue (View)** : Présentation des données et interaction utilisateur.
- **Contrôleur (Controller)** : Logique métier et coordination entre modèle et vue.

### Technologies Utilisées

- Backend : Django (Python)
- Base de données : SQLite
- Frontend : HTML, CSS, Bootstrap

---

## Installation

### Prérequis

- Python 3.8+
- pip (Gestionnaire de paquets Python)

### Étapes

1. Clonez le dépôt :

   ```bash
   git clone https://github.com/Aya1311/CarServ---Plateforme-de-Gestion-de-Flotte-de-Vehicules/
   cd CarServ
   ```

2. Installez les dépendances :

   ```bash
   pip install -r requirements.txt
   ```

3. Appliquez les migrations :

   ```bash
   python manage.py migrate
   ```

4. Lancez le serveur de développement :

   ```bash
   python manage.py runserver
   ```

5. Accédez à l'application dans votre navigateur à l'adresse suivante :

   ```
   http://127.0.0.1:8000
   ```

---

## Utilisation

- Créez un compte administrateur :
  ```bash
  python manage.py createsuperuser
  ```
  Accédez à l'interface d'administration via `/admin` pour configurer les utilisateurs et les véhicules.

- Connectez-vous en tant que client ou employé pour explorer les fonctionnalités spécifiques à chaque rôle.

---
## Auteurs

- Aya Laadaili
