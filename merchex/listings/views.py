from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from listings.models import Band, Listing
from listings.forms import ContactUsForm, BandForm, ListingForm
from django.core.mail import send_mail


# Liste des groupes de musique
def band_list(request):
    bands = Band.objects.all()
    return render(request, 'listings/band_list.html', {'bands': bands})


# Détails d'un groupe de musique
def band_detail(request, id):
    band = get_object_or_404(Band, id=id)
    return render(request, 'listings/band_detail.html', {'band': band})


# Création d'un nouveau groupe de musique
def band_create(request):
    if request.method == 'POST':
        form = BandForm(request.POST)

        if form.is_valid():
            band = form.save()
            return redirect('band-detail', band.id)
    else:
        form = BandForm()
    return render(request, 'listings/band_create.html', {'form': form})


# Mise à jour d'un groupe de musique
def band_update(request, id):
    band = get_object_or_404(Band, id=id)
    if request.method == 'POST':
        form = BandForm(request.POST, instance=band)

        if form.is_valid():
            band = form.save()
            return redirect('band-detail', band.id)
    else:
        form = BandForm(instance=band)

    return render(request, 'listings/band_update.html', {'form': form})


# Page "À propos de nous"
def about(request):
    return render(request, 'listings/about_us.html')


# Liste des annonces
def listings(request):
    listings = Listing.objects.all()
    return render(request, 'listings/listing_list.html', {'listings': listings})


# Détails d'une annonce
def listing_detail(request, id):
    listing = get_object_or_404(Listing, id=id)
    return render(request, 'listings/listing_detail.html', {'listing': listing})


# Création d'une nouvelle annonce
def listing_create(request):
    if request.method == 'POST':
        form = ListingForm(request.POST)

        if form.is_valid():
            listing = form.save()
            return redirect('listing-detail', listing.id)
    else:
        form = ListingForm()
    return render(request, 'listings/listing_create.html', {'form': form})


# Mise à jour d'une annonce
def listing_update(request, id):
    listing = get_object_or_404(Listing, id=id)
    if request.method == 'POST':
        form = ListingForm(request.POST, instance=listing)

        if form.is_valid():
            listing = form.save()
            return redirect('listing-detail', listing.id)
    else:
        form = ListingForm(instance=listing)

    return render(request, 'listings/listing_update.html', {'form': form})


# Page de contact
def contact(request):
    if request.method == 'POST':
        form = ContactUsForm(request.POST)

        if form.is_valid():
            send_mail(
                subject=f'Message from {form.cleaned_data["name"] or "anonyme"} via MerchEx - Contact Us form',
                message=form.cleaned_data['message'],
                from_email=form.cleaned_data['email'],
                recipient_list=['31400rng@gmail.com'],
            )
            return redirect('email-sent')
    else:
        form = ContactUsForm()
    return render(request, 'listings/contact_us.html', {'form': form})


# Vue personnalisée pour la gestion des erreurs 404
def custom_404(request, exception):
    return render(request, 'listings/404.html', {'exception': exception}, status=404)


# Page indiquant que l'e-mail a été envoyé avec succès
def email_sent(request):
    return render(request, 'listings/email_sent.html')
