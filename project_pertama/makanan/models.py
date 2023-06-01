from django.db import models

# Create your models here.
class Makanan(models.Model):
    nama = models.Charfield(max_length=30)
    alamat_penjual = models.TextField()