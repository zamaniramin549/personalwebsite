from django.urls import path
from .views import *

urlpatterns = [
    path('resume/', ResumeDashboardView.as_view(), name='resumedashboard'),
    path('resume-header/', ResumeHeaderView.as_view(), name='resumeheader'),
    path('resume-about/', ResumeAboutView.as_view(), name='resumeabout'),
    path('resume-technical-skill/', ResumeTechnicalSkillsView.as_view(), name='resumetechnicalskill'),
    path('resume-professional-skill/', ResumeProfessionalSkillsView.as_view(), name='resumeprofessionalskill'),
    path('resume-work-experience/', ResumeWorkExperienceView.as_view(),name='resumeworkex'),
    path('resume-project/', ResumeprojectView.as_view(),name='resumeproject'),
    path('del-work-exp/', DelWorkExp.as_view(), name='delworkexp'),
    path('edit-work-exp/<int:pk>/', EditWorkExp.as_view(), name='editworkexp'),
    path('del-project/', DelProject.as_view(), name='delproject'),
    path('edit-project/<int:pk>/', EditProject.as_view(), name='editproject'),
    path('resume-add-education/', ResumeAddEducationView.as_view(), name='resumeaddeducation'),
    path('resume-delete-education/', ResumeDeleteEducationView.as_view(), name='deleteeducation'),
    path('resume-edit-education/<int:pk>/', ResumeEditEducationView.as_view(), name='resumeediteducation'),
    path('resume-add-award/', ResumeAddAwardView.as_view(), name='resumeaddaward'),
    path('resume-delete-award/', ResumeDeleteAwardView.as_view(), name='deleteaward'),
    path('resume-edit-award/<int:pk>/', ResumeEditAwardView.as_view(), name='resumeeditaward'),
    path('resume-add-lang/', ResumeAddLangView.as_view(), name='resumelanguage'),
    path('resume-delete-lang/', ResumeDeleteLangView.as_view(), name='deletelang'),
    path('resume-edit-lang/<int:pk>/', ResumeEditLangView.as_view(), name='resumeeditlang'),
    path('resume-update-interest/', ResumeUpdateInterestView.as_view(), name='updateresumeinterest'),
]