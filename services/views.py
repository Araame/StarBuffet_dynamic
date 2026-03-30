from django.shortcuts import render
from .models import Traiteur
# Create your views here.
def liste_traiteurs(request):
    """Retrieve all traiteurs"""
    context = {}
    context["traiteurs"] = Traiteur.objects.all()

    return render(request,"liste.html", context = context)