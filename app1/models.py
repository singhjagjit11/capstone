from django.db import models

# Create your models here.

class Patches(models.Model):
    PatcheId = models.AutoField(primary_key=True)
    Cve = models.CharField(max_length=500)
    Component = models.CharField(max_length=500)
    BaseScore = models.CharField(max_length=500)

