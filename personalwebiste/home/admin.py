from django.contrib import admin
from .models import *
# Register your models here.
class CommentAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'comment', 'status', 'blog_pk')
    list_filter = ('date', 'status')

class MessagesAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'status' ,'date')
    list_filter = ('date','status')


class TestimonialsAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'status' ,'date')
    list_filter = ('date','status')

class UserDataAdmin(admin.ModelAdmin):
    list_display = ('country', 'city' ,'date')
    list_filter = ('date','city', 'country')
    
class UserUrlDataAdmin(admin.ModelAdmin):
    list_display = ('url', 'date')
    list_filter = ('date',)
    

admin.site.register(Comments, CommentAdmin)
admin.site.register(Testimonials, TestimonialsAdmin)
admin.site.register(UserData, UserDataAdmin)
admin.site.register(UserUrlData, UserUrlDataAdmin)
admin.site.register(UserDataSeen)