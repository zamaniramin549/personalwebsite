from django.contrib import admin
from .models import *

class AboutAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'position', 'date_update')

class WhatIDoSettingsAdmin(admin.ModelAdmin):
    list_display = ('description', 'date_update')

class SkillAdmin(admin.ModelAdmin):
    list_display = ('skill', 'level', 'date_update', 'date_add')
    list_filter = ('skill', 'level','date_update', 'date_add')


class ProjectsAdmin(admin.ModelAdmin):
    list_display = ('project_name', 'client', 'industry', 'website', 'date_update', 'date_add')
    list_filter = ('project_name', 'client', 'industry', 'date_update', 'date_add')


class ProjectSettingAdmin(admin.ModelAdmin):
    list_display = ('description', 'last_update')


class CategoriesAdmin(admin.ModelAdmin):
    list_display = ('category_name', 'date_added', 'date_updated')
    list_filter = ('date_added', 'date_updated')


class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'short_content','date_added', 'date_updated')
    list_filter = ('date_added', 'date_updated')


class NavbarSettingAdmin(admin.ModelAdmin):
    list_display = ('about', 'fb','lin', 'insta', 'tw', 'git', 'date_updated')

class SeoSettingAdmin(admin.ModelAdmin):
    list_display = ('sitename', 'date_updated')


class EmailSettingAdmin(admin.ModelAdmin):
    list_display = ('email_host_user', 'date_updated')

class QrCodeAdmin(admin.ModelAdmin):
    list_display = ('website',)

admin.site.register(About, AboutAdmin)
admin.site.register(WhatIdoSettings, WhatIDoSettingsAdmin)
admin.site.register(Skill, SkillAdmin)
admin.site.register(Projects, ProjectsAdmin)
admin.site.register(ProjectSetting, ProjectSettingAdmin)
admin.site.register(Categories, CategoriesAdmin)
admin.site.register(Blog, BlogAdmin)
admin.site.register(NavbarSetting, NavbarSettingAdmin)
admin.site.register(SeoSettings, SeoSettingAdmin)
admin.site.register(EmailSetting, EmailSettingAdmin)
admin.site.register(QrCode, QrCodeAdmin)