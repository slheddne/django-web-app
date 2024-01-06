from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from listings.models import Band, Listing
from listings.forms import ContactUsForm
from django.core.mail import send_mail


def band_list(request):
    bands = Band.objects.all()
    return render(request, 'listings/band_list.html', {'bands': bands})


def band_detail(request, id):
    band = get_object_or_404(Band, id=id)
    return render(request,
                  'listings/band_detail.html',
                  {'band': band})


def about(request):
    return render(request, 'listings/about_us.html')


def listings(request):
    listings = Listing.objects.all()
    return render(request, 'listings/listing_list.html', {'listings': listings})


def listing_detail(request, id):
    listing = get_object_or_404(Listing, id=id)
    return render(request,
                  'listings/listing_detail.html',
                  {'listing': listing})


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


def custom_404(request, exception):
    return render(request, 'listings/404.html', {'exception': exception}, status=404)


def email_sent(request):
    return render(request, 'listings/email_sent.html')
