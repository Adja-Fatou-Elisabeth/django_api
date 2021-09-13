from django.db import models

# Create your models here.
class Departement(models.Model):
    nom_dep = models.CharField(max_length=50)
    service = models.CharField(max_length= 500)

    def __str__(self):
        return nom_dep