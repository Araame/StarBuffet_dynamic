from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from .models import Traiteur



# Create your views here.
def accueil(request):
    """Show index.html"""
    context = {}
    return render(request, "index.html", context =  context)

def contact(request):
    """Show index.html"""
    context = {}
    return render(request, "contact.html", context =  context)

def liste_traiteurs(request):
    """Retrieve all traiteurs"""
    traiteurs = Traiteur.objects.all()
    contexte = {"traiteurs" : traiteurs}
    return render(request,"liste.html", contexte)


def detail_traiteur(request, id):
    """Show details of a traiteur"""
    context = {}

    context["traiteur"] = Traiteur.objects.get(id = id)
    return render(request, "detail.html", context=context)

@login_required
def ajouter_traiteur(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            nomcomplet = request.POST.get("nomcomplet")
            description = request.POST.get("description")
            specialites = request.POST.get("specialites")
            adresse = request.POST.get("adresse")
            email = request.POST.get("email")
            telephone = request.POST.get("telephone")
            datedecreation = request.POST.get("datedecreation")
            image = request.FILES.get("image")

            Traiteur.objects.create(nomcomplet = nomcomplet,description = description,specialites = specialites,adresse = adresse,image = image,email = email,telephone = telephone,datedecreation = datedecreation)
            return redirect('liste_traiteurs')
        else:
            print("ERREUR")





        return HttpResponse(f"Connecté en tant que : {request.user.username}")
    
    else:
        return HttpResponse("Etrange : le décorateur a laissé passer un utilisateur anonyme.")


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home') 
    else:
        form = AuthenticationForm()
    return render(request, 'registration/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')

