from django.urls import path
from . import views
urlpatterns = [
    path('', views.liste_traiteurs),
    path('<int:id>/detail/', views.detail_traiteur, name = 'detail_traiteur'),
    path('accounts/ login/', name='login'),
]