![python](https://img.shields.io/badge/Python_3.10.5-14354C?style=for-the-badge&logo=python&logoColor=yellow "Python version") 
![django](https://img.shields.io/badge/Django_3.0-092E20?style=for-the-badge&logo=django&logoColor=white "Django version")  
![CircleCI](https://img.shields.io/badge/circle%20ci-%23161616.svg?style=for-the-badge&logo=circleci&logoColor=white) ![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white)
![Heroku](https://img.shields.io/badge/heroku-%23430098.svg?style=for-the-badge&logo=heroku&logoColor=white)  
![SQLite](https://img.shields.io/badge/sqlite-%2307405e.svg?style=for-the-badge&logo=sqlite&logoColor=white)  
![tests](https://img.shields.io/badge/passed%20tests-6-success "tests passed")  
# Projet 13 - Mettez à l'échelle une application Django en utilisant une architecture modulaire


![Logo](src_readme/logoOCL.png)
  
## Résumé

Site web d'Orange County Lettings

## Développement local

### Prérequis

- Compte GitHub avec accès en lecture à ce repository
- Git CLI
- SQLite3 CLI
- Interpréteur Python, version 3.6 ou supérieure

Dans le reste de la documentation sur le développement local, il est supposé que la commande `python` de votre OS shell exécute l'interpréteur Python ci-dessus (à moins qu'un environnement virtuel ne soit activé).

### macOS / Linux

#### Cloner le repository

- `cd /path/to/put/project/in`
- `git clone https://github.com/OpenClassrooms-Student-Center/Python-OC-Lettings-FR.git`

#### Créer l'environnement virtuel

- `cd /path/to/Python-OC-Lettings-FR`
- `python -m venv venv`
- `apt-get install python3-venv` (Si l'étape précédente comporte des erreurs avec un paquet non trouvé sur Ubuntu)
- Activer l'environnement `source venv/bin/activate`
- Confirmer que la commande `python` exécute l'interpréteur Python dans l'environnement virtuel
`which python`
- Confirmer que la version de l'interpréteur Python est la version 3.6 ou supérieure `python --version`
- Confirmer que la commande `pip` exécute l'exécutable pip dans l'environnement virtuel, `which pip`
- Pour désactiver l'environnement, `deactivate`

#### Exécuter le site

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `pip install --requirement requirements.txt`
- `python manage.py runserver`
- Aller sur `http://localhost:8000` dans un navigateur.
- Confirmer que le site fonctionne et qu'il est possible de naviguer (vous devriez voir plusieurs profils et locations).

#### Linting

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `flake8`

#### Tests unitaires

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `pytest`

#### Base de données

- `cd /path/to/Python-OC-Lettings-FR`
- Ouvrir une session shell `sqlite3`
- Se connecter à la base de données `.open oc-lettings-site.sqlite3`
- Afficher les tables dans la base de données `.tables`
- Afficher les colonnes dans le tableau des profils, `pragma table_info(Python-OC-Lettings-FR_profile);`
- Lancer une requête sur la table des profils, `select user_id, favorite_city from
  Python-OC-Lettings-FR_profile where favorite_city like 'B%';`
- `.quit` pour quitter

#### Panel d'administration

- Aller sur `http://localhost:8000/admin`
- Connectez-vous avec l'utilisateur `admin`, mot de passe `Abc1234!`

### Windows

Utilisation de PowerShell, comme ci-dessus sauf :

- Pour activer l'environnement virtuel, `.\venv\Scripts\Activate.ps1` 
- Remplacer `which <my-command>` par `(Get-Command <my-command>).Path`

  
    
## Déploiement

Pour déployer notre code en production nous utilisons les technologies suivantes :
>[CircleCI](https://circleci.com/)  
Pour automatiser l’intégration et le déploiement du code de github vers l'hébergeur.

>[Heroku](https://www.heroku.com/)  
L’hébergeur choisit pour noter site.

>[Sentry](https://sentry.io/welcome/)  
Pour logger et effectuer un suivit des éventuelles erreurs pendant la production.  
    
### Principe

Lorsque le code de la branche **main** est **modifié** et ***pushé*** vers le repository Github,  
```shell
git push -u origin main
```

Le déploiement se décompose en 3 étapes :  
1. [Vérification des tests du code](#principe1) 
2. [Construction de l'image Docker](#principe2)
3. [Déploiement du site via l'image Docker](#principe3)

Pour des raisons pratiques et/ou de **sécurités**, certaines variables d'environnement doivent être renseignées dans **CircleCi** rubrique **Project Settings** et **Environment Variables** du projet:
>DEVELOP_SETTINGS  
Fichier settings à utiliser lors du développement ou des tests.  
Ici **oc_lettings_site.settings.develop** .  

>PROD_SETTINGS  
Fichier settings à utiliser lors de la production.  
Ici **oc_lettings_site.settings.production_settings** .  

>DOCKER_HUB_PROJECT  
Nom du projet (du repository) sur dockerub.

>DOCKER_PASS  
Mot de passe **dockerhub** du compte.

>DOCKER_USERNAME  
Nom d'utilisateur **dockerhub**.

>HEROKU_API_KEY  
Token d'identification du compte **Heroku**.

>HEROKU_APP_NAME
Nom de l'application sur **Heroku**.

>SECRET_KEY  
Clef de sécurité de l'application **Django**.  

- Pour en générer une nouvelle SECRET_KEY aléatoire et conforme aux recommandations Django de différentes manières :  
#### *1. Vous pouvez dans un programme rentrer le code suivant et récupérer la sortie (si Django est installé dans votre projet):*
```python
from django.core.management.utils import get_random_secret_key

print(get_random_secret_key())
```
#### *2. Vous pouvez dans un programme rentrer le code suivant et récupérer la sortie (pas besoin de dépendances):*
```python
import secrets

print(secrets.token_urlsafe())
```

#### *3. Le programme suivant peut-être effectué simplement en une seule ligne de commande :*
```shell
python -c "import secrets; print(secrets.token_urlsafe())"
``` 

>SENTRY_DSN  
Clef DSN de l'application sur Sentry. 

### Vérification des tests du code <a id="principe1"></a>
CircleCI détecte le changement et vérifie les tests configurés dans le fichier **<code> [.circleci/config.yml](https://github.com/Deadjuju/P13_OC/blob/main/.circleci/config.yml)</code>**.
Les tests effectués ici sont  
- tests des vues (views) avec **Pytest**  
- linter avec **Flake8**

**Si** les tests sont validés CircleCi passe à la construction de l'image Docker.

### 2. Construction de l'image Docker <a id="principe2">
  
L'image docker est construite grâce au fichier **[Dockerfile](https://github.com/Deadjuju/P13_OC/blob/main/Dockerfile)**, elle permet ici de d'utiliser une version de python 3.10, d'installer les dépendances du projet et de démarrer le serveur en utilisant le fichier de ***[settings](https://github.com/Deadjuju/P13_OC/blob/main/oc_lettings_site/settings/production_settings.py)*** correspondant à la production. 
L'image est également **pushée** vers le repo **dockerhub** du projet avec un ***tag*** de commit généré par CircleCI et un ***tag*** **latest** représentant la version la plus à jour de l'image Docker.  
L'image *latest* pourra ainsi être utilisé lors du développement.  

### 3. Déploiement du site <a id=principe3></a> 
Une fois l'image **Docker** construite elle est automatiquement pushée sur **Heroku** (voir partie **heroku_deploy** du fichier **<code> [.circleci/config.yml](https://github.com/Deadjuju/P13_OC/blob/main/.circleci/config.yml) </code>**).  
Une fois déployé, les erreurs éventuelles pourront être suivies via **Sentry**. 
