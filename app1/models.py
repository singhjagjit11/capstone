from django.db import models

# Create your models here.

class Patches(models.Model):
    PatcheId = models.AutoField(primary_key=True)
    col0 = models.CharField(max_length=500)
    col1 = models.CharField(max_length=500)
    col2 = models.CharField(max_length=500)
    col3 = models.CharField(max_length=500)
    col4 = models.CharField(max_length=500)
    col5 = models.CharField(max_length=500)
    col6 = models.CharField(max_length=500)
    col7 = models.CharField(max_length=500)
    col8 = models.CharField(max_length=500)
    col9 = models.CharField(max_length=500)
    col10 = models.CharField(max_length=500)
    col11= models.CharField(max_length=500) 
    col12 = models.CharField(max_length=500)
    col13= models.CharField(max_length=500)
    col14 = models.CharField(max_length=500)
    #col15= models.CharField(max_length=500)

