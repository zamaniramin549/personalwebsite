from multiprocessing import context
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login
from urllib import request
from .models import *
from django.shortcuts import render, get_object_or_404, redirect
from django.template.loader import get_template, render_to_string
from django.views import View
from dashboard.models import *
from resume.models import *
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .recaptcha import FormWithCaptcha
from .email import sendemail
from .generatepdf import render_to_pdf
from .userdata import getip
import datetime



#robot.txt
from django.http import HttpResponse
from django.views.decorators.http import require_GET
@require_GET
def robots_txt(request):
    lines = [
        "User-Agent: *",
        "Disallow: /dashboard/",
        "Disallow: /dashboard-login/",
        "Disallow: /testimonials/",
    ]
    return HttpResponse("\n".join(lines), content_type="text/plain")

    

class IndexView(View):
    def get(self, request):
        getip(request, url = request.path)
        about = get_object_or_404(About, pk=1)
        whatido_setting = get_object_or_404(WhatIdoSettings, pk = 1)
        skills = Skill.objects.all().order_by('-level')
        projects = Projects.objects.all().order_by('-pk')[:4]
        blogs = Blog.objects.all().exclude(status = False).order_by('-pk')[:3]
        navbar_settings = NavbarSetting.objects.get(pk = 1)
        seo = get_object_or_404(SeoSettings, pk = 1)
        testimonials = Testimonials.objects.all().exclude(status = False).order_by('-pk')
        return render(request, 'home/index.html',{
            'about':about,
            'whatido_setting':whatido_setting,
            'skills':skills,
            'projects':projects,
            'blogs':blogs,
            'navbar_settings':navbar_settings,
            'seo':seo,"testimonials":testimonials,
        })


class SkillDeatils(View):
    def get(self, request, slug):
        getip(request, url = request.path)
        skill = get_object_or_404(Skill,slug = slug)
        navbar_settings = NavbarSetting.objects.get(pk = 1)
        seo = get_object_or_404(SeoSettings, pk = 1)
        return render(request, 'home/skill_detail.html',{
            'skill':skill, 'navbar_settings':navbar_settings,'seo':seo,
        })

class ProjectDeatils(View):
    def get(self, request, slug):
        getip(request, url = request.path)
        project = get_object_or_404(Projects ,slug = slug)
        navbar_settings = NavbarSetting.objects.get(pk = 1)
        seo = get_object_or_404(SeoSettings, pk = 1)
        return render(request, 'home/project_detail.html',{
            'project':project, 'navbar_settings':navbar_settings, 'seo':seo,
        })

class AllProjectsView(View):
    def get(self, request):
        getip(request, url = request.path)
        projects_list = Projects.objects.all().order_by('-pk')
        get_page_setting = get_object_or_404(ProjectSetting, pk=1)
        navbar_settings = NavbarSetting.objects.get(pk = 1)
        seo = get_object_or_404(SeoSettings, pk = 1)
        page = request.GET.get('page', 1)
        paginator = Paginator(projects_list, 2)
        try:
            projects = paginator.page(page)
        except PageNotAnInteger:
            projects = paginator.page(1)
        except EmptyPage:
            projects = paginator.page(paginator.num_pages)
        return render(request, 'home/all_projects.html',{
            'projects':projects,'navbar_settings':navbar_settings,
            'get_page_setting':get_page_setting,'seo':seo,
        })

class AllBlogsView(View):
    def get(self, request):
        getip(request, url = request.path)
        categories = Categories.objects.all().order_by('-pk')
        blogs_list = Blog.objects.all().exclude(status = False).order_by('-pk')
        navbar_settings = NavbarSetting.objects.get(pk = 1)
        seo = get_object_or_404(SeoSettings, pk = 1)
        page = request.GET.get('page', 1)
        paginator = Paginator(blogs_list, 1)
        try:
            blogs = paginator.page(page)
        except PageNotAnInteger:
            blogs = paginator.page(1)
        except EmptyPage:
            blogs = paginator.page(paginator.num_pages)
        return render(request, 'home/all_blogs.html',{'categories':categories,'blogs':blogs, 'navbar_settings':navbar_settings
        ,'seo':seo,})


class AllBlogsCategoryView(View):
    def get(self, request, slug):
        getip(request, url = request.path)
        categories = Categories.objects.all().order_by('-pk')
        get_category = get_object_or_404(Categories, slug = slug)
        blogs_list = Blog.objects.filter(category = get_category, status = True).order_by('-pk')
        navbar_settings = NavbarSetting.objects.get(pk = 1)
        seo = get_object_or_404(SeoSettings, pk = 1)
        page = request.GET.get('page', 1)
        paginator = Paginator(blogs_list, 3)
        try:
            blogs = paginator.page(page)
        except PageNotAnInteger:
            blogs = paginator.page(1)
        except EmptyPage:
            blogs = paginator.page(paginator.num_pages)
        return render(request, 'home/all_blogs.html',{
            'categories':categories,'blogs':blogs,"get_category":get_category, 'navbar_settings':navbar_settings
            ,'seo':seo,})


class BlogDetailView(View):
    def get(self, request, slug):
        getip(request, url = request.path)
        get_blog = get_object_or_404(Blog, slug = slug)
        get_blog_comment = Comments.objects.filter(
            blog_pk = get_blog, status = True).order_by('-pk')
        navbar_settings = NavbarSetting.objects.get(pk = 1)
        seo = get_object_or_404(SeoSettings, pk = 1)
        get_blog_comment_count = get_blog_comment.count
        recaptcha = FormWithCaptcha
        if request.session.get('email'):
            session_email = request.session.get('email')
        else:
            session_email = ""
        if request.session.get('full_name'):
            session_full_name = request.session.get('full_name')
        else:
            session_full_name =  ""
        return render(request, 'home/blog_detail.html',{
            'get_blog':get_blog,'get_blog_comment':get_blog_comment,'navbar_settings':navbar_settings,
            'seo':seo,"recaptcha":recaptcha,"get_blog_comment_count":get_blog_comment_count,"session_email":session_email,
        "session_full_name":session_full_name})

    def post(self, request, slug):
        get_blog = get_object_or_404(Blog, slug = slug)
        get_blog_comment = Comments.objects.filter(
            blog_pk = get_blog, status = True).order_by('-pk')
        navbar_settings = NavbarSetting.objects.get(pk = 1)
        seo = get_object_or_404(SeoSettings, pk = 1)
        get_blog_comment_count = get_blog_comment.count
        full_name = request.POST.get('full_name').capitalize()
        email = request.POST.get('email').lower()
        content = request.POST.get('content')
        recaptcha = FormWithCaptcha
        recaptchacheck = request.POST.get('g-recaptcha-response')
        if recaptchacheck:
            if content and email and full_name != "":
                save_comment = Comments(
                    full_name = full_name,
                    email = email,
                    comment = content,
                    blog_pk = Blog.objects.get(slug = slug)
                )
                save_comment.save()
                msgs = True
                request.session['email'] = email
                request.session['full_name'] = full_name
                return render(request, 'home/blog_detail.html',{
            'get_blog':get_blog,'get_blog_comment':get_blog_comment,'navbar_settings':navbar_settings,
            'seo':seo,"recaptcha":recaptcha,"msgs":msgs,"get_blog_comment_count":get_blog_comment_count
        })
            else:
                return HttpResponseRedirect(request.path_info)
        else:
            msgw = True
            return render(request, 'home/blog_detail.html',{
            'get_blog':get_blog,'get_blog_comment':get_blog_comment,'navbar_settings':navbar_settings,
            'seo':seo,"recaptcha":recaptcha,"msgw":msgw,"full_name":full_name,"email":email,"content":content
        ,"get_blog_comment_count":get_blog_comment_count})


class ContactView(View):
    def get(self, request):
        getip(request, url = request.path)
        navbar_settings = NavbarSetting.objects.get(pk = 1)
        seo = get_object_or_404(SeoSettings, pk = 1)
        email_setting = get_object_or_404(EmailSetting, pk = 1)
        recaptcha = FormWithCaptcha
        if request.session.get('email'):
            session_email = request.session.get('email')
        else:
            session_email =  ""
        if request.session.get('full_name'):
            session_full_name = request.session.get('full_name')
        else:
            session_full_name =  ""
        return render(request, 'home/contact.html', {'navbar_settings':navbar_settings, 'seo':seo,'email_setting':email_setting,
        'recaptcha':recaptcha,"session_email":session_email,"session_full_name":session_full_name})

    def post(self, request):
        msgs = None
        navbar_settings = NavbarSetting.objects.get(pk = 1)
        seo = get_object_or_404(SeoSettings, pk = 1)
        email_setting = get_object_or_404(EmailSetting, pk = 1)
        recaptcha = FormWithCaptcha
        full_name = request.POST.get('full_name').capitalize()
        email = request.POST.get('email').lower()
        content = request.POST.get('content')
        recapthchacheck = request.POST.get('g-recaptcha-response')
        if recapthchacheck:
            if full_name and email and content != "":
                save_msg = Messages(
                    full_name = full_name,
                    email = email,
                    content = content
                )
                save_msg.save()
                request.session['email'] = email
                request.session['full_name'] = full_name
                # Email send
                sendemail(full_name = full_name, email = email, content = content)
                msgs = f"Thank you {full_name} for contacting me. I'll respond as soon as possible."
                return render(request, 'home/contact.html', {'navbar_settings':navbar_settings, 'seo':seo,'email_setting':email_setting,"msgs":msgs,
                'recaptcha':recaptcha})
        else:
            msgw = True
            return render(request, 'home/contact.html', {'navbar_settings':navbar_settings, 'seo':seo,'email_setting':email_setting,"msgs":msgs,
            'recaptcha':recaptcha,"msgw":msgw, "full_name":full_name,"email":email,"content":content})


class ResumeView(View):
    def get(self, request):
        getip(request, url = request.path)
        resume_header = get_object_or_404(ResumeHeader, pk=1)
        resume_about = get_object_or_404(ResumeAbout, pk=1)
        resume_technical_skills = get_object_or_404(ResumeTechnicalSkill, pk=1)
        resume_professional_skills = get_object_or_404(ResumeProfessionalSkill, pk=1)
        resume_interest = get_object_or_404(ResumeInterests, pk=1)
        work_exper = ResumeWorkExpe.objects.all().order_by('-pk')
        projects = ResumeProject.objects.all().order_by('-pk')
        resume_educations = ResumeEducation.objects.all().order_by('-pk')
        resume_awards = ResumeAwards.objects.all().order_by('-pk')
        resume_langs = ResumeLang.objects.all().order_by('-pk')
        navbar_settings = NavbarSetting.objects.get(pk = 1)
        seo = get_object_or_404(SeoSettings, pk = 1)
        return render(request, 'home/resume.html',{
            'resume_header':resume_header,'resume_about':resume_about,
            'resume_technical_skills':resume_technical_skills,
            'resume_professional_skills':resume_professional_skills,
            'work_exper':work_exper,'projects':projects,'resume_educations':resume_educations,
            'resume_awards':resume_awards,'resume_langs':resume_langs,'resume_interest':resume_interest, 'navbar_settings':navbar_settings,'seo':seo,})



class TestimonialsView(View):
    def get(self, request):
        getip(request, url = request.path)
        navbar_settings = NavbarSetting.objects.get(pk = 1)
        seo = get_object_or_404(SeoSettings, pk = 1)
        return render(request, 'home/testimonials.html',{'navbar_settings':navbar_settings,"seo":seo,
        })

    def post(self, request):
        msgs = None
        msg = None
        navbar_settings = NavbarSetting.objects.get(pk = 1)
        seo = get_object_or_404(SeoSettings, pk = 1)
        full_name = request.POST.get("fullname")
        content = request.POST.get("content")
        if full_name and content != "":
            try:
                image = request.FILES["image"]
                save_testimonial = Testimonials(
                    full_name = full_name,
                    content = content,
                    image = image
                )
                save_testimonial.save()
            except:
                save_testimonial = Testimonials(
                    full_name = full_name,
                    content = content,
                )
                save_testimonial.save()
            msgs = f"thank you {full_name} for your feedback."
            return render(request, 'home/testimonials.html',{'navbar_settings':navbar_settings,"seo":seo,
        "msgs":msgs})
        else:
            msg = f"Name and Content are needed."
            return render(request, 'home/testimonials.html',{'navbar_settings':navbar_settings,"seo":seo,
        "msg":msg})


class DashboardLoginView(View):
    def get(self, request):
        getip(request, url = request.path)
        if not request.user.is_authenticated:
            navbar_settings = NavbarSetting.objects.get(pk = 1)
            seo = get_object_or_404(SeoSettings, pk = 1)
            return render(request, 'home/login.html',{"navbar_settings":navbar_settings,"seo":seo})
        else:
            return redirect('dashboard')


    def post(self, request):
        if request.user.is_authenticated:
            return redirect('dashboard')
        else:
            username = request.POST.get('email')        
            password = request.POST.get('password')
            user = authenticate(username=username, password=password)   
            if user is not None:
                login(request, user)
                return redirect('dashboard')
            else:
                return redirect('dashbaordlogin')   


def error_404_view(request, exception):
    navbar_settings = NavbarSetting.objects.get(pk = 1)
    seo = get_object_or_404(SeoSettings, pk = 1)
    return render(request, '404.html',{'navbar_settings':navbar_settings,"seo":seo})

def error_500_view(request):
    navbar_settings = NavbarSetting.objects.get(pk = 1)
    seo = get_object_or_404(SeoSettings, pk = 1)
    return render(request, '500.html',{'navbar_settings':navbar_settings,"seo":seo})


class GeneratePDF(View):
    def get(self, request, *args, **kwargs):
        site_name = request.META['HTTP_HOST']
        today = datetime.datetime.now().date()
        # template = get_template('home/pdf/resume.html')


        resume_header = get_object_or_404(ResumeHeader, pk=1)
        resume_about = get_object_or_404(ResumeAbout, pk=1)
        resume_technical_skills = get_object_or_404(ResumeTechnicalSkill, pk=1)
        resume_professional_skills = get_object_or_404(ResumeProfessionalSkill, pk=1)
        resume_interest = get_object_or_404(ResumeInterests, pk=1)
        work_exper = ResumeWorkExpe.objects.all().order_by('-pk')
        projects = ResumeProject.objects.all().order_by('-pk')
        resume_educations = ResumeEducation.objects.all().order_by('-pk')
        resume_awards = ResumeAwards.objects.all().order_by('-pk')
        resume_langs = ResumeLang.objects.all().order_by('-pk')
        navbar_settings = NavbarSetting.objects.get(pk = 1)
        seo = get_object_or_404(SeoSettings, pk = 1)
        qr_code = get_object_or_404(QrCode, pk = 1)

        context = {
            'resume_header':resume_header,'resume_about':resume_about,
            'resume_technical_skills':resume_technical_skills,"site_name":site_name,
            'resume_professional_skills':resume_professional_skills,
            'work_exper':work_exper,'projects':projects,'resume_educations':resume_educations,
            'resume_awards':resume_awards,'resume_langs':resume_langs,"qr_code":qr_code,
            'resume_interest':resume_interest, 'navbar_settings':navbar_settings,'seo':seo,
            }

        # test = render_to_string('home/pdf/resume.html', context)

        # html = template.render(context)

        pdf = render_to_pdf('home/pdf/resume.html', context)
        if pdf:
            response = HttpResponse(pdf, content_type='application/pdf')
            filename = "Ramin_Resume_%s.pdf" %(today)
            content = "inline; filename='%s'" %(filename)
            download = request.GET.get("download")
            if download:
                content = "attachment; filename='%s'" %(filename)
            response['Content-Disposition'] = content
            return response
        return HttpResponse("Not found")