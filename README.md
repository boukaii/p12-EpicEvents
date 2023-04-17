# Projet 12: Développez une architecture back-end sécurisée en utilisant Django ORM

# Description :
Projet consistant à créer une API CRM avec Django REST Framwork et PostgreSQL à l'aide d'un diagramme entité-relation.


L'API doit respecter les directives suivantes :

* L'accès à la base de données doit être sécurisé.
* Une interface d'administration Django doit également être créée.



 Client :
   * Un client peut avoir plusieurs contrats
   * Un client a un contact commercial

 Contrat :
   * Un contrat a un client
   * Un contrat a un contact commercial

 Evénement :
   * Un événement a un contrat
   * Un événement a un contact support



# Documentation :
###  **_Pour plus de détails sur le fonctionnement de cette API, se référer à sa documentation (Postman)._**

# Installation :

### **_Cloner le référentiel :_**
`https://github.com/boukaii/p12-EpicEvents.git`

###  **_Déplacer vers le nouveau dossier :_**
`cd pythonProject12`

### **_Créez l'environnement virtuel :_**
`python -m venv env`

### _**Activez l'environnement virtuel :**_
Pour macOS et Linux: `env/bin/activate`

Pour Windows: `env\Scripts\activate`

### **_Installez les packages :_**
`pip install -r requirements.txt`


### **_Effectuez les migrations :_**

`python manage.py makemigrations`

### **_Puis :_** 

`python manage.py migrate`

### **_Il ne vous reste plus qu'à lancer le serveur :_**

`python manage.py runserver`