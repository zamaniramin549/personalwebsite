from django.contrib import admin
from django.urls import path, include, re_path
# from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve
from django.contrib.sitemaps.views import sitemap
from home.views import robots_txt
from .sitemaps import StaticSitemap, SkillSitemap, ProjectsSitemap, CategoriesSitemap, BlogSitemap


sitemaps = {
    'static': StaticSitemap(),
    'skill': SkillSitemap(),
    'project': ProjectsSitemap(),
    'category': CategoriesSitemap(),
    'blog': BlogSitemap(),
}

urlpatterns = [
    path('admin/', admin.site.urls),
    path("robots.txt", robots_txt),
    path('', include('home.urls')),
    path('dashboard/', include('dashboard.urls')),
    path('resume/', include('resume.urls')),
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root':settings.MEDIA_ROOT}),
    re_path(r'^static/(?P<path>.*)$', serve, {'document_root':settings.STATIC_ROOT}),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps},name='django.contrib.sitemaps.views.sitemap'),
]

handler404 = 'home.views.error_404_view'
handler500 = 'home.views.error_500_view'

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
