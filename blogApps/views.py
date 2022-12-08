from django.shortcuts import render
from django.views import View

# index view------------------------


class IndexView(View):
    # method get--------------------------
    def get(self, request):
        return render(request, 'index.html', {})

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
        return render(request, 'gallery.html', {})

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
        return render(request, 'blog.html', {})

    # method post--------------------------
    def post(self, request):
        return 0

# blog detail view------------------------


class BlogDetailView(View):
    # method get--------------------------
    def get(self, request):
        return render(request, 'blog_detail/detail.html', {})

    # method post--------------------------
    def post(self, request):
        return 0
