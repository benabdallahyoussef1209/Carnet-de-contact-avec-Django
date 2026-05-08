from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.db.models import Q
from .models import Contact
from .forms import ContactForm


def liste_contacts(request):
    """
    Vue principale : affiche la liste de tous les contacts.
    Supporte aussi la recherche via le paramètre GET 'q'.
    """
    query = request.GET.get('q', '')  # Récupère le terme de recherche
    contacts = Contact.objects.all()

    if query:
        # Filtre sur le nom, prénom ou email
        contacts = contacts.filter(
            Q(nom__icontains=query) |
            Q(prenom__icontains=query) |
            Q(email__icontains=query)
        )

    return render(request, 'contacts/liste.html', {
        'contacts': contacts,
        'query': query,
        'total': contacts.count(),
    })


def detail_contact(request, pk):
    """
    Vue détail : affiche les informations complètes d'un contact.
    get_object_or_404 retourne une erreur 404 si le contact n'existe pas.
    """
    contact = get_object_or_404(Contact, pk=pk)
    return render(request, 'contacts/detail.html', {'contact': contact})


def ajouter_contact(request):
    """
    Vue d'ajout : affiche et traite le formulaire de création.
    GET  → affiche le formulaire vide
    POST → valide et enregistre le contact
    """
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            contact = form.save()
            messages.success(request, f'✅ Contact "{contact}" ajouté avec succès !')
            return redirect('liste_contacts')
        else:
            messages.error(request, '❌ Veuillez corriger les erreurs ci-dessous.')
    else:
        form = ContactForm()

    return render(request, 'contacts/formulaire.html', {
        'form': form,
        'titre': 'Ajouter un contact',
        'bouton': 'Ajouter',
    })


def modifier_contact(request, pk):
    """
    Vue de modification : pré-remplit le formulaire avec les données existantes.
    """
    contact = get_object_or_404(Contact, pk=pk)

    if request.method == 'POST':
        form = ContactForm(request.POST, instance=contact)  # instance = données existantes
        if form.is_valid():
            form.save()
            messages.success(request, f'✅ Contact "{contact}" modifié avec succès !')
            return redirect('detail_contact', pk=contact.pk)
        else:
            messages.error(request, '❌ Veuillez corriger les erreurs ci-dessous.')
    else:
        form = ContactForm(instance=contact)

    return render(request, 'contacts/formulaire.html', {
        'form': form,
        'contact': contact,
        'titre': f'Modifier {contact}',
        'bouton': 'Enregistrer',
    })


def supprimer_contact(request, pk):
    """
    Vue de suppression : demande confirmation avant de supprimer.
    GET  → affiche la page de confirmation
    POST → supprime le contact
    """
    contact = get_object_or_404(Contact, pk=pk)

    if request.method == 'POST':
        nom = str(contact)
        contact.delete()
        messages.success(request, f'🗑️ Contact "{nom}" supprimé.')
        return redirect('liste_contacts')

    return render(request, 'contacts/confirmer_suppression.html', {'contact': contact})
