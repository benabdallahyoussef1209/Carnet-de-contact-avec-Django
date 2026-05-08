from django.urls import path
from . import views

urlpatterns = [
    # Liste + recherche
    path('', views.liste_contacts, name='liste_contacts'),

    # Détail d'un contact (pk = clé primaire)
    path('contact/<int:pk>/', views.detail_contact, name='detail_contact'),

    # Ajouter
    path('ajouter/', views.ajouter_contact, name='ajouter_contact'),

    # Modifier
    path('contact/<int:pk>/modifier/', views.modifier_contact, name='modifier_contact'),

    # Supprimer
    path('contact/<int:pk>/supprimer/', views.supprimer_contact, name='supprimer_contact'),
]
