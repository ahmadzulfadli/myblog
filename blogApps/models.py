from django.db import models
from django.db.models.deletion import CASCADE


# ---------------------------------------------------------------
# DB Blog


class Kategori(models.Model):
    id_kat = models.AutoField(primary_key=True)
    kategori = models.CharField(max_length=20)

    def __str__(self):
        return self.kategori


class Artikel(models.Model):
    id_art = models.AutoField(primary_key=True)
    penulis = models.CharField(max_length=20)
    kategori = models.ForeignKey(Kategori, on_delete=models.CASCADE)
    judul = models.CharField(max_length=50)
    isi_artikel = models.CharField(max_length=2000)
    keterangan = models.CharField(max_length=100)
    gambar = models.FileField(blank=True, upload_to='gambar')
    published = models.DateField(auto_now_add=True)
    updated = models.TimeField(auto_now=True)

    def __str__(self):
        return self.judul


# ---------------------------------------------------------------
# DB Galery


class KategoriGallery(models.Model):
    id_katGal = models.AutoField(primary_key=True)
    kategoriGal = models.CharField(max_length=50)

    def __str__(self):
        return self.kategoriGal


class Gallery(models.Model):
    id_gal = models.AutoField(primary_key=True)
    keterangan = models.CharField(max_length=500)
    gallery = models.FileField(blank=True, upload_to='gallery')
    kategoriGal = models.ForeignKey(KategoriGallery, on_delete=models.CASCADE)
