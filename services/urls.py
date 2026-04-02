from django.urls import path
from . import views
urlpatterns = [
    path('', views.accueil, name="index"),
    path('liste_traiteurs', views.liste_traiteurs, name = 'liste_traiteurs'),
    path('<int:id>/detail/', views.detail_traiteur, name = 'detail_traiteur'),
    path('contact', views.contact, name = 'contact'),
    path('ajouter', views.ajouter_traiteur, name = 'ajout'),

]