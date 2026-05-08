from django.db import models


class Contact(models.Model):
    """
    Modèle représentant un contact.
    Chaque contact a un nom, prénom, email, téléphone et une date de création.
    """
    prenom = models.CharField(max_length=100, verbose_name="Prénom")
    nom = models.CharField(max_length=100, verbose_name="Nom")
    email = models.EmailField(unique=True, verbose_name="Email")
    telephone = models.CharField(max_length=20, blank=True, verbose_name="Téléphone")
    adresse = models.TextField(blank=True, verbose_name="Adresse")
    date_creation = models.DateTimeField(auto_now_add=True, verbose_name="Ajouté le")

    class Meta:
        ordering = ['nom', 'prenom']  # Tri alphabétique par défaut
        verbose_name = "Contact"
        verbose_name_plural = "Contacts"

    def __str__(self):
        return f"{self.prenom} {self.nom}"

    def nom_complet(self):
        return f"{self.prenom} {self.nom}"
