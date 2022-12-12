from django.shortcuts import render
from django.views import View
from blogApps.models import *

# index view------------------------


class IndexView(View):
    # method get--------------------------
    def get(self, request):
        context = {}
        return render(request, 'index.html', context)

    # method post--------------------------
    def post(self, request):
        return 0

# about view------------------------


class AboutView(View):
    # method get--------------------------
    def get(self, request):
        return render(request, 'about.html', {})

    # method post--------------------------
    def post(self, request):
        return 0

# gallery view------------------------


class GalleryView(View):
    # method get--------------------------
    def get(self, request):
        model = Gallery.objects.all()
        context = {
            'model': model,
        }
        return render(request, 'gallery.html', context)

    # method post--------------------------
    def post(self, request):
        return 0

# contact view------------------------


class ContactView(View):
    # method get--------------------------
    def get(self, request):
        return render(request, 'contact.html', {})

    # method post--------------------------
    def post(self, request):
        return 0


# blog view------------------------


class BlogView(View):
    # method get--------------------------
    def get(self, request):
        model = Artikel.objects.all()
        context = {
            'model': model,
        }
        return render(request, 'blog.html', context)

    # method post--------------------------
    def post(self, request):
        return 0

# blog detail view------------------------


class BlogDetailView(View):
    # method get--------------------------
    def get(self, request, id_art):
        model = Artikel.objects.get(id_art=id_art)
        modelKat = Kategori.objects.all()
        context = {
            'model': model,
            'modelKat': modelKat,
        }
        return render(request, 'blog_detail/detail.html', context)

    # method post--------------------------
    def post(self, request):
        return 0
