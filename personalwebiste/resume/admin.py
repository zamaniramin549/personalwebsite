from signal import siginterrupt
from django.contrib import admin
from .models import *
# Register your models here.
class ResumeHeaderAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'position','phone', 'email', 'website', 'last_update')

class ResumeAboutAdmin(admin.ModelAdmin):
    list_display = ('about', 'last_update')

class ResumeTechnicalSkillAdmin(admin.ModelAdmin):
    list_display = ('skills', 'last_update')

class ResumeProfessionalSkillAdmin(admin.ModelAdmin):
    list_display = ('skills', 'last_update')

class ResumeWorkExpeAdmin(admin.ModelAdmin):
    list_display = ('title', 'company_name', 'duration', 'date_added', 'last_update')
    list_filter = ('date_added', 'last_update')


class ResumeProjectAdmin(admin.ModelAdmin):
    list_display = ('project_name', 'website', 'date_added', 'last_update')
    list_filter = ('date_added', 'last_update')

class ResumeEducationAdmin(admin.ModelAdmin):
    list_display = ('subject', 'university', 'year', 'last_update')
    list_filter = ('date_added', 'last_update')


class ResumeAwardsAdmin(admin.ModelAdmin):
    list_display = ('award', 'award_title', 'last_update')
    list_filter = ('date_added', 'last_update')

class ResumeLangAdmin(admin.ModelAdmin):
    list_display = ('language', 'language_level', 'last_update')
    list_filter = ('date_added', 'last_update')

class ResumeInterestAdmin(admin.ModelAdmin):
    list_display = ('interests', 'last_update')
    list_filter = ('date_added', 'last_update')


admin.site.register(ResumeHeader, ResumeHeaderAdmin)
admin.site.register(ResumeAbout, ResumeAboutAdmin)
admin.site.register(ResumeTechnicalSkill, ResumeTechnicalSkillAdmin)
admin.site.register(ResumeProfessionalSkill, ResumeProfessionalSkillAdmin)
admin.site.register(ResumeWorkExpe, ResumeWorkExpeAdmin)
admin.site.register(ResumeProject, ResumeProjectAdmin)
admin.site.register(ResumeEducation, ResumeEducationAdmin)
admin.site.register(ResumeAwards, ResumeAwardsAdmin)
admin.site.register(ResumeLang, ResumeLangAdmin)
admin.site.register(ResumeInterests, ResumeInterestAdmin)
