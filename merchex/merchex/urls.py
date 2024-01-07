"""
URL configuration for merchex project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from listings import views

urlpatterns = [
    # Admin endpoints
    path('admin/', admin.site.urls),

    # Bands endpoints
    path('bands/', views.band_list, name='band-list'),
    path('bands/<int:id>/', views.band_detail, name='band-detail'),
    path('bands/add/', views.band_create, name='band-create'),
    path('bands/<int:id>/change/', views.band_update, name='band-update'),
    path('bands/<int:id>/delete/', views.band_delete, name='band-delete'),

    # About us endpoints
    path('about_us/', views.about, name='about-us'),

    # Listings endpoints
    path('listings/', views.listings, name='listing-list'),
    path('listings/<int:id>/', views.listing_detail, name='listing-detail'),
    path('listings/add', views.listing_create, name='listing-create'),
    path('listings/<int:id>/change/', views.listing_update, name='listing-update'),
    path('listings/<int:id>/delete/', views.listing_delete, name='listing-delete'),

    # Contact us endpoints
    path('contact_us/', views.contact, name='contact-us'),

    # Email sent endpoints
    path('email_sent/', views.email_sent, name='email-sent'),
]

# Custom 404 page
handler404 = 'listings.views.custom_404'
