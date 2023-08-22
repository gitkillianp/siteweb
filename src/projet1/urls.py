"""projet1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from .views import index, about

# auto-modif from projet1 import settings = from . import settings (utile pour l'ajout static() après urlpatterns
from . import settings

# sitemaps
from django.contrib.sitemaps.views import sitemap
from .sitemaps import BlogSitemap, IndexSitemap, AboutSitemap, BlogArticleSitemap


sitemaps = {
    'index': IndexSitemap,
    'blog': BlogSitemap,
    'about': AboutSitemap,
    'blog_article': BlogArticleSitemap,
}

# fin du sitemaps


urlpatterns = [
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
    path('', index, name="index"),
    path('blog/', include('blog.urls')),
    path('formulaire/', include('formulaire.urls')),
    path('Sf23ghL250/', admin.site.urls),
    path('about/', about, name="about"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


