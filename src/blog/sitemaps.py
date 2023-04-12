from django.contrib.sitemaps import Sitemap
from .models import BlogPost


class BlogArticleSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.9

    def items(self):
        return BlogPost.objects.all()

    def location(self, obj):
        return "/blog/%s/" % obj.slug


class IndexSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.9

    def items(self):
        return ['index']

    def location(self, obj):
        return "/"


class AboutSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.9

    def items(self):
        return ['about']

    def location(self, obj):
        return "/about/"

class BlogSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.9

    def items(self):
        return ['blog']

    def location(self, obj):
        return "/blog/"