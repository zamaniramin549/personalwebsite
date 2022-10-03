import email
from tabnanny import verbose
from django.db import models
from urllib.parse import urlparse

# Create your models here.
class ResumeHeader(models.Model):
    full_name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    phone = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    website = models.URLField(blank=True, null=True)
    last_update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.full_name + " " + self.position

    class Meta:
        verbose_name_plural = 'Resume Header'

    def url_text(self):
        parsed_url = urlparse(self.website)
        return parsed_url.hostname.replace("www.", "")

class ResumeAbout(models.Model):
    about = models.TextField()
    image = models.FileField(upload_to='resume/')
    last_update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.about

    class Meta:
        verbose_name_plural = 'Resume About'


class ResumeTechnicalSkill(models.Model):
    skills = models.TextField(blank=True, null=True)
    last_update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.skills

    class Meta:
        verbose_name_plural = 'Resume Technical Skills'


class ResumeProfessionalSkill(models.Model):
    skills = models.TextField(blank=True, null=True)
    last_update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.skills

    class Meta:
        verbose_name_plural = 'Resume Professional Skills'


class ResumeWorkExpe(models.Model):
    title = models.CharField(max_length=255)
    company_name = models.CharField(max_length=100)
    duration = models.CharField(max_length=100)
    content = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
     
    class Meta:
        verbose_name_plural = "Resume work experience"



class ResumeProject(models.Model):
    project_name = models.CharField(max_length=100)
    website = models.URLField(blank=True, null=True)
    content = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.project_name
     
    class Meta:
        verbose_name_plural = "Resume project"

    def url_text(self):
        parsed_url = urlparse(self.website)
        return parsed_url.hostname.replace("www.", "")


class ResumeEducation(models.Model):
    subject = models.CharField(max_length=100)
    university = models.CharField(max_length=100)
    year = models.CharField(max_length=100)
    date_added = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.subject
     
    class Meta:
        verbose_name_plural = "Resume education"



class ResumeAwards(models.Model):
    award = models.CharField(max_length=100)
    award_title = models.CharField(max_length=100)
    date_added = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.subject
     
    class Meta:
        verbose_name_plural = "Resume awards"


class ResumeLang(models.Model):
    language= models.CharField(max_length=100)
    language_level = models.CharField(max_length=100)
    date_added = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.language
     
    class Meta:
        verbose_name_plural = "Resume language"


class ResumeInterests(models.Model):
    interests = models.TextField(blank=True, null=True)
    date_added = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.interests
     
    class Meta:
        verbose_name_plural = "Resume interest"

    def splits(self):
        if self.interests:
            return self.interests.split(",")
        else:
            return None


