from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from dashboard.models import Skill, Projects, Categories, Blog
from home.views import IndexView, ContactView, ResumeView

class StaticSitemap(Sitemap):
    priority = 1.0
    changefreq = 'daily'

    home = IndexView.as_view()
    contact = ContactView.as_view()
    resume = ResumeView.as_view()

    def items(self):
        return ['home', 'contact', 'resume']

    def location(self, item):
        return reverse(item)



class SkillSitemap(Sitemap):
    changefreq = "daily"
    priority = 0.7

    def items(self):
        return Skill.objects.all()


    def lastmod(self, obj): 
        return obj.date_add



class ProjectsSitemap(Sitemap):
    changefreq = "daily"
    priority = 0.7

    def items(self):
        return Projects.objects.all()

    def lastmod(self, obj): 
        return obj.date_add


class CategoriesSitemap(Sitemap):
    changefreq = "daily"
    priority = 0.7

    def items(self):
        return Categories.objects.all()

    def lastmod(self, obj): 
        return obj.date_added



class BlogSitemap(Sitemap):
    changefreq = "daily"
    priority = 0.7

    def items(self):
        return Blog.objects.filter(status = True)

    def lastmod(self, obj): 
        return obj.date_added

