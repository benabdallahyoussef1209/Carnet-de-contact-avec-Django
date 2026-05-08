from django import forms
from .models import Contact


class ContactForm(forms.ModelForm):
    """
    Formulaire basé sur le modèle Contact.
    Django génère automatiquement les champs depuis le modèle.
    """
    class Meta:
        model = Contact
        fields = ['prenom', 'nom', 'email', 'telephone', 'adresse']
        widgets = {
            # On personnalise les widgets pour ajouter des classes CSS et des placeholders
            'prenom': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ex: Ahmed'
            }),
            'nom': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ex: Ben Ali'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'ahmed@exemple.com'
            }),
            'telephone': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': '+216 XX XXX XXX'
            }),
            'adresse': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
                'placeholder': 'Adresse complète...'
            }),
        }
