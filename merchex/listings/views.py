from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from listings.models import Band, Listing


def band_list(request):
    bands = Band.objects.all()
    return render(request, 'listings/band_list.html', {'bands': bands})


def band_detail(request, id):
    band = get_object_or_404(Band, id=id)
    return render(request,
                  'listings/band_detail.html',
                  {'band': band})


def about(request):
    return render(request, 'listings/about-us.html')


def listings(request):
    listings = Listing.objects.all()
    return render(request, 'listings/listing_list.html', {'listings': listings})


def listing_detail(request, id):
    listing = get_object_or_404(Listing, id=id)
    return render(request,
                  'listings/listing_detail.html',
                  {'listing': listing})


def contact(request):
    return render(request, 'listings/contact-us.html')


def custom_404(request, exception):
    return render(request, 'listings/404.html', {'exception': exception}, status=404)
