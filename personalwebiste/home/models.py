import email
from tabnanny import verbose
from urllib import request
from django.db import models
from dashboard.models import Blog
# Create your models here.
class Comments(models.Model):
    comment = models.TextField()
    full_name = models.CharField(max_length=50)
    email = models.EmailField()
    date = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=True)
    blog_pk = models.ForeignKey(Blog, models.CASCADE)

    def __str__(self):
        return self.comment + " " + self.full_name

    class Meta:
        ordering = ('-pk',)
        verbose_name_plural = "Comments"

class Messages(models.Model):
    full_name = models.CharField(max_length=50)
    email = models.EmailField()
    content = models.TextField()
    status = models.BooleanField(default=False)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_name

    class Meta:
        ordering = ('-date',)
        verbose_name_plural = "Messages"



class Testimonials(models.Model):
    full_name = models.CharField(max_length=50)
    image = models.FileField(upload_to="testimonials/", blank=True)
    content = models.TextField()
    status = models.BooleanField(default=False)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_name

    class Meta:
        ordering = ('-date',)
        verbose_name_plural = "Testimonials"


class UserData(models.Model):
    city = models.CharField(max_length=100, blank=True)
    state = models.CharField(max_length=100, blank=True)
    iso_code = models.CharField(max_length=100, blank=True)
    country = models.CharField(max_length=100, blank=True)
    postalcode = models.CharField(max_length=100, blank=True)
    latitude = models.CharField(max_length=100, blank=True)
    longitude = models.CharField(max_length=100, blank=True)
    ip = models.CharField(max_length=100, blank=True)
    traits_network = models.CharField(max_length=100, blank=True)
    operating_system = models.CharField(max_length=100, blank=True)
    browser = models.CharField(max_length=100, blank=True)
    device  = models.CharField(max_length=100, blank=True)
    device_family  = models.CharField(max_length=100, blank=True)
    host_name = models.CharField(max_length=100, blank=True)
    user_name = models.CharField(max_length=100, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    onlydate = models.DateField(auto_now=True)
    

    def __str__(self):
        return self.city + " " + self.city

    class Meta:
        ordering = ('-date',)
        verbose_name_plural = "Visitors"


class UserUrlData(models.Model):
    userdata = models.ForeignKey(UserData, models.CASCADE)
    url = models.CharField(max_length=100, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    onlydate = models.DateField(auto_now_add=True)


class UserDataSeen(models.Model):
    userdata = models.ForeignKey(UserData, models.CASCADE)
    seen = models.BooleanField(default=True)
    date = models.DateTimeField(auto_now_add=True)