from django.shortcuts import render
from .models import Traiteur
# Create your views here.
def liste_traiteurs(request):
    """Retrieve all traiteurs"""
    context = {}
    context["traiteurs"] = Traiteur.objects.all()

    return render(request,"liste.html", context = context)


def detail_traiteur(request, id):
    """Show details of a traiteur"""
    context = {}

    context["traiteur"] = Traiteur.objects.get(id = id)
    return render(request, "detail.html", context=context)