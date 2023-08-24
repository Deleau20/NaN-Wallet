# NaN-Wallet

Projet de sortie de NaN digital Academy spécialité Python

# Application Web de transanction banquaire (utilisant Django)

## À propos

A des fins de formation, nous avons créé une application web de transaction banquaire. Cette application permet de créer des comptes banquaires, de les créditer et de les débiter à partir d'autre comptes banquaires.

cette application est utilisé avec différent rôle:

- Administrateur:
  - Modifie les informations de comptes d'un utilisateur
  - Créer des gestionnaires
  - Peux modifier les informations des gestionnaires et leurs droits
- Gestionnaire:
  - Créer des comptes banquaires
  - Créditer et débiter des comptes banquaires
  - Peux modifier les informations des comptes banquaires
- Client:
  - Créer un compte
  - Créditer et débiter son compte
  - Peux modifier ses informations personnelles

## Prérequis

- Python 3.x installé localement
- Django installé dans votre environnement Python
- Un navigateur web moderne

## Installation

1. Clonez ou téléchargez ce dépôt.

   ```
   git clone
   ```

2. Accédez au répertoire du projet.
   ```
   cd NaN-Wallet
   ```
3. Créer un environnement virtuel

   ```
   python -m venv env
   ```

4. Activez l'environnement virtuel

sur Windows:

```
env\Scripts\activate
```

sur macOS/Linux:

```
source env/bin/activate
```

5. Installez les dépendances:

   ```
   pip install -r requirements.txt
   ```

6. Créer la base de donnée:
   ```
   python manage.py migrate
   ```

## Mode de déploiemment

1. Lancez le serveur en exécutant la commande suivante :

   ```
   python manage.py runserver
   ```
2. Accédez à l'application dans votre navigateur à l'adresse:
   `http://localhost:8000`.

3. Créez un compte utilisateur en fournissant les informations requises.

4. Connectez-vous avec vos identifiants.

5. Explorez les fonctionnalités

## Contribution

Les contributions à ce projet sont les bienvenues. Voici comment vous pouvez contribuer :

1. Fork ce dépôt.

2. Créez une branche pour votre fonctionnalité ou correction de bug.

    ````
    git checkout -b fonctionnalite-incroyable
    ```
3. Ajoutez vos modifications et faites un commit.

    ```
    git add .
    ```
    ```
    git commit -m 'Fonctionnalité incroyable'
    ```

4. Poussez sur la branche.

   ```
   git push origin fonctionnalite-incroyable
   ```

5. Ouvrez une pull request.

## Construit avec

### Langages & Frameworks

- Python - [Site officiel](https://www.python.org)
- Django - [Documentation](https://docs.djangoproject.com)

#### Déploiement

- Pythonanywhere - [Site officiel](https://www.pythonanywhere.com)