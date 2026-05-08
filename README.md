#  Gestion de Contacts — Django

Un projet Django simple et complet pour gérer vos contacts.

##  Lancer le projet

### 1. Installer Django
```bash
pip install -r requirements.txt
```

### 2. Créer la base de données
```bash
python manage.py migrate
```

### 3. (Optionnel) Créer un compte admin
```bash
python manage.py createsuperuser
```

### 4. Lancer le serveur
```bash
python manage.py runserver
```

### 5. Ouvrir dans le navigateur
- Application : http://127.0.0.1:8000/
- Admin Django : http://127.0.0.1:8000/admin/

---

##  Structure du projet

```
contacts_project/
│
├── manage.py                    ← Point d'entrée Django
├── requirements.txt             ← Dépendances (Django)
│
├── contacts_project/            ← Configuration du projet
│   ├── settings.py              ← Paramètres (DB, apps installées...)
│   └── urls.py                  ← URLs principales
│
└── contacts/                    ← Notre application
    ├── models.py                ← Modèle Contact (table BDD)
    ├── views.py                 ← Logique (liste, ajout, modif, suppression)
    ├── forms.py                 ← Formulaire Django
    ├── urls.py                  ← URLs de l'app
    ├── admin.py                 ← Config panneau admin
    └── templates/contacts/
        ├── base.html            ← Template parent (navbar, messages)
        ├── liste.html           ← Liste + recherche
        ├── detail.html          ← Fiche contact
        ├── formulaire.html      ← Ajout / Modification
        └── confirmer_suppression.html
```

---

##  Fonctionnalités

| Fonctionnalité | URL |
|---|---|
| Liste des contacts | `/` |
| Ajouter un contact | `/ajouter/` |
| Voir un contact | `/contact/<id>/` |
| Modifier un contact | `/contact/<id>/modifier/` |
| Supprimer un contact | `/contact/<id>/supprimer/` |
| Recherche | `/?q=terme` |

---

##  Concepts Django utilisés

- **Model** : définit la structure des données (Contact)
- **View** : contient la logique métier (CRUD)
- **Template** : affiche le HTML avec les données
- **Form** : valide les données soumises par l'utilisateur
- **URL** : connecte les URLs aux vues
- **Admin** : interface d'administration automatique
- **Messages** : notifications flash (succès/erreur)
- **CSRF** : protection des formulaires
