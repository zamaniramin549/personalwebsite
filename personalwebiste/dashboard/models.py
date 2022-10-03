from distutils.command.upload import upload
from tabnanny import verbose
from tkinter.tix import Balloon
from turtle import back, title
from django.db import models
from django.urls import reverse
from django.template.defaultfilters import slugify
from urllib.parse import urlparse
from django_cryptography.fields import encrypt
from io import BytesIO
from django.core.files import File
from PIL import Image, ImageDraw
import qrcode

# Create your models here.
class About(models.Model):
    full_name = models.CharField(max_length=50)
    position = models.CharField(max_length=50)
    about = models.TextField()
    image = models.FileField(upload_to='images/')
    date_update = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'About'

    def __str__(self):
        return self.full_name

class WhatIdoSettings(models.Model):
    description = models.TextField()
    date_update = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'What I do setting'

    def __str__(self):
        return self.description

class Skill(models.Model):
    skill = models.CharField(max_length=50)
    description = models.TextField()
    level = models.IntegerField()
    image = models.FileField(upload_to='skills/')
    slug = models.SlugField(null=False, unique=True)
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-pk',)
        verbose_name_plural = 'Skills'
        

    def __str__(self):
        return self.skill

    def get_absolute_url(self):
        return reverse('skill_detail', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.skill)
        return super().save(*args, **kwargs)


class Projects(models.Model):
    project_name = models.CharField(max_length=100)
    client = models.CharField(max_length=100, blank=True, null=True)
    industry = models.CharField(max_length=100)
    image = models.FileField(upload_to='projects/')
    website = models.URLField(blank=True, null=True)
    short_description = models.CharField(max_length=255)
    description = models.TextField()
    slug = models.SlugField(null=False, unique=True)
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-pk',)
        verbose_name_plural = "Projects"

    def get_absolute_url(self):
        return reverse('projectdetail', kwargs={'slug':self.slug})


    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.project_name)
        return super().save(*args, **kwargs)

    def url_text(self):
        parsed_url = urlparse(self.website)
        return parsed_url.hostname.replace("www.", "")

    def __str__(self):
        return self.project_name


class ProjectSetting(models.Model):
    description = models.TextField(blank= True, null= True)
    last_update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.description

    class Meta:
        verbose_name_plural = "project page setting"


class Categories(models.Model):
    category_name = models.CharField(max_length=30)
    date_added = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    slug = models.SlugField(null=False, unique=True)

    class Meta:
        ordering = ('-pk',)
        verbose_name_plural = "Categories"


    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.category_name)
        return super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("allblogsbycategory", kwargs={"slug":self.slug})

    def __str__(self):
        return self.category_name



class Blog(models.Model):
    title = models.CharField(max_length=255)
    image = models.FileField(upload_to="blog/")
    short_content = models.CharField(max_length=255)
    content = models.TextField()
    category = models.ForeignKey(Categories, on_delete=models.CASCADE)
    status = models.BooleanField(default=False)
    date_added = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    slug = models.SlugField(null=False, unique=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('-pk',)
        verbose_name_plural = "Blog"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('blogdetail', kwargs={"slug":self.slug})


class NavbarSetting(models.Model):
    about = models.CharField(max_length=500)
    fb = models.URLField(blank=True, null=True)
    lin = models.URLField(blank=True, null=True)
    insta = models.URLField(blank=True, null=True)
    tw = models.URLField(blank=True, null=True)
    git = models.URLField(blank=True, null=True)
    image = models.FileField(upload_to='images/', null=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.about

    class Meta:
        verbose_name_plural = "Navbar setting"



class SeoSettings(models.Model):
    description = models.TextField(blank=True)
    keywords = models.TextField(blank=True)
    sitename = models.CharField(max_length=255, blank=True)
    image = models.FileField(blank=True, upload_to="images/")
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.sitename

    class Meta:
        verbose_name_plural = "SEO setting"




class EmailSetting(models.Model):
    email_host = models.CharField(max_length=500, blank=True, null=True)
    email_port = models.IntegerField(blank=True, null=True)
    email_use_tls = models.BooleanField(blank=True, null=True)
    email_host_user = models.EmailField(blank=True, null=True)
    email_host_password = encrypt(models.CharField(max_length=1000,blank=True, null=True))
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.email_host_user)

    class Meta:
        verbose_name_plural = "Email setting"



class QrCode(models.Model):
    website = models.URLField(blank=True)
    qr_code = models.ImageField(upload_to = "QrCode/", blank = True,null=True)

    def __str__(self):
        return str(self.website)

    def save(self, *args, **kwargs):
        qrcode_img = qrcode.make(self.website)
        canvas = Image.new("RGB",(400, 400), "white")
        drow = ImageDraw.Draw(canvas)
        canvas.paste(qrcode_img)
        fname = f'qr_code.png'
        buffer = BytesIO()
        canvas.save(buffer, "PNG")
        self.qr_code.save(fname, File(buffer),save = False)
        canvas.close()
        super().save(*args, **kwargs)