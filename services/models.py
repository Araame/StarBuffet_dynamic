from django.db import models

# Create your models here.
class Traiteur(models.Model):
    nomcomplet = models.CharField(max_length=200)
    specialites = models.TextField()
    description = models.TextField()
    adresse = models.CharField(max_length=150)
    est_actif = models.BooleanField(default=True)
    email = models.EmailField()
    datedecreation = models.DateField()
    telephone = models.CharField()
    image = models.URLField()