# Shopping-Website

A simple fullstack template for a shopping website. You can add, update and delete persistent items (with a name, price, quantity, picture). Those can be updated via the Django admin website. Front-end and back-end communicate thanks to an API REST (using Django Rest Framework) and Axios is consumming the API.
I might implement the shopping cart in a near future. There is an admin and user account to connect to the Django admin website.

## Stack :
- front-end : HTML, CSS (Bootstrap, Font Awesome), JavaScript (Vue.js), Axios
- back-end : Django (Django Rest Framework)

## Requirements

- Python3+ (https://www.python.org/downloads/)
- Node.js (https://nodejs.org/en/)

## How to use

Cloner le projet : git clone https://github.com/JulienMousset/Shopping-Website.git
Activer l'environnement virtuel à partir de la racine du dossier cloné : source env/bin/activate
Installer les paquets Python nécessaires : pip install -r requirements.txt
Démarrer le serveur : python manage.py runserver
Accéder au site d'administration de Django à cette url : http://127.0.0.1:8000/admin
Se connecter soit en admin (Username : admin - Password : admin), soit en tant qu'utilisateur (Username : codoc - Password : drwarehouse).
Installer les modules Node.js nécessaires : cd vueapp/vuedjangorest/ et npm install
Exécuter le projet : npm run serve
Visualiser le projet à cette url : http://localhost:8080/
Si vous le souhaitez, vous pouvez alors ajouter, modifier et supprimer des produits depuis le site d'administration de Django

## Screenshots

