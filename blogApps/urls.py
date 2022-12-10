from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('about/', views.AboutView.as_view(), name='about'),
    path('gallery/', views.GalleryView.as_view(), name='gallery'),
    path('contact/', views.ContactView.as_view(), name='contact'),
    path('blog/', views.BlogView.as_view(), name='blog'),
    path('blogdetail/<str:id_art>/',
         views.BlogDetailView.as_view(), name='blogdetail'),
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
