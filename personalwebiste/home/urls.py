from django.urls import path
from .views import *
urlpatterns = [
    path('', IndexView.as_view(), name='home'),
    path('skill-detail/<slug:slug>/', SkillDeatils.as_view(), name='skill_detail'), 
    path('project-detail/<slug:slug>/', ProjectDeatils.as_view(), name='projectdetail'),
    path('all-projects/', AllProjectsView.as_view(), name='allprojects'),
    path('all-blogs/', AllBlogsView.as_view(), name="allblogs"),
    path('all-blogs/<slug:slug>/', AllBlogsCategoryView.as_view(), name="allblogsbycategory"),
    path('blog-detail/<slug:slug>/', BlogDetailView.as_view(), name='blogdetail'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('resume/', ResumeView.as_view(), name='resume'),
    path('dashboard-login/', DashboardLoginView.as_view(), name='dashbaordlogin'),
    path('testimonials/', TestimonialsView.as_view(), name='testimonials'),
    path('resume-pdf-generate/', GeneratePDF.as_view(), name='resumepdfgenerate')
]