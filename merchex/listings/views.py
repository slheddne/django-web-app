from django.http import HttpResponse
from django.shortcuts import render


def hello(request):
    return HttpResponse("<h1>Hello Django!")

def about(request):
    return HttpResponse("<h1>À propos</h1> <p>Nous adorons merch !</p>")

def listings(request):
    return HttpResponse("<h1>Nos annonces</h1> <ul><li>Annonce 1</li><li>Annonce 2</li><li>Annonce 3</li></ul>")

def contact(request):
    return HttpResponse("<h1>Contactez-nous !</h1> <p>Envoyez-nous un e-mail à l'adresse suivante : x@y.z")