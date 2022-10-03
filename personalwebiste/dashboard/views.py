from importlib.resources import read_binary
import os
from re import L
from django.contrib.auth import logout
from tkinter.messagebox import NO
from unicodedata import category
from urllib import request
from django.urls import reverse_lazy
from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.models import User
from django.views import View
from django.http import HttpResponseRedirect
import datetime
from home.models import *
from .models import *

countmsgs = Messages.objects.filter(status = False).count


# Create your views here.
class DashboardView(View):
    def get(self, request):
        if request.user.is_authenticated:
            navbat_setting = get_object_or_404(NavbarSetting, pk = 1)

            blog = Blog.objects.all()
            blog_count = blog.count
            blog_active_count = blog.exclude(status = False).count
            blog_deactive_count = blog.exclude(status = True).count

            project = Projects.objects.all()
            project_count = project.count

            skill = Skill.objects.all()
            skill_count = skill.count

            message = Messages.objects.all()
            message_count = message.count
            message_read = message.exclude(status = False).count
            message_unread = message.exclude(status = True).count

            testimonial = Testimonials.objects.all()
            testimonial_count = testimonial.count
            testimonial_publish_count = testimonial.exclude(status = False).count
            testimonial_unpublish_count = testimonial.exclude(status = True).count

            today = datetime.datetime.now()
            last_7_days = today - datetime.timedelta(days=7)

            user_data = UserData.objects.all()
            user_data_count = user_data.count
            user_data_count_last_7_day = user_data.filter(onlydate__range=[last_7_days, today]).count
            user_data_count_today = user_data.filter(onlydate = today).count

            date1 = request.GET.get('date1')
            date2 = request.GET.get('date2')
            if date1 and date2:
                user_data_mobile = user_data.filter(onlydate__range=[date1, date2], device = "Mobile").count
                user_data_tablet = user_data.filter(onlydate__range=[date1, date2], device = "Tablet").count
                user_data_touch_capable = user_data.filter(onlydate__range=[date1, date2], device = "Touch Capable").count
                user_data_pc = user_data.filter(onlydate__range=[date1, date2], device = "PC").count
                user_data_bot = user_data.filter(onlydate__range=[date1, date2], device = "Bot").count
            else:
                user_data_mobile = user_data.filter(onlydate__range=[last_7_days, today], device = "Mobile").count
                user_data_tablet = user_data.filter(onlydate__range=[last_7_days, today], device = "Tablet").count
                user_data_touch_capable = user_data.filter(onlydate__range=[last_7_days, today], device = "Touch Capable").count
                user_data_pc = user_data.filter(onlydate__range=[last_7_days, today], device = "PC").count
                user_data_bot = user_data.filter(onlydate__range=[last_7_days, today], device = "Bot").count

            
            
            page_visited = UserUrlData.objects.filter(onlydate = today).order_by("-pk")

            return render(request, 'dashboard/index.html',{'countmsgs':countmsgs,'navbat_setting':navbat_setting,"blog_count":blog_count,
            "blog_active_count":blog_active_count,"blog_deactive_count":blog_deactive_count,"project_count":project_count,
            "skill_count":skill_count,"message_count":message_count,"message_read":message_read,"message_unread":message_unread,
            "testimonial_count":testimonial_count,"testimonial_publish_count":testimonial_publish_count,"testimonial_unpublish_count":testimonial_unpublish_count,
            "user_data_count":user_data_count,"user_data_count_last_7_day":user_data_count_last_7_day,"user_data_count_today":user_data_count_today,
            "page_visited":page_visited,"user_data_mobile":user_data_mobile,"user_data_tablet":user_data_tablet,"user_data_touch_capable":user_data_touch_capable,
            "user_data_pc":user_data_pc,"user_data_bot":user_data_bot,"date1":date1, "date2":date2})
        else:
            return redirect('home')

class AboutView(View):
    def get(self, request):
        if request.user.is_authenticated:
            about = About.objects.get(pk = 1)
            navbat_setting = get_object_or_404(NavbarSetting, pk = 1)
            return render(request, 'dashboard/about.html',{
                'about':about,'countmsgs':countmsgs, 'navbat_setting':navbat_setting
            })
        else:
            return redirect('home')

    def post(self, request):
        if request.user.is_authenticated:
            try:
                full_name = request.POST.get('full_name')
                position = request.POST.get('position')
                about = request.POST.get('about')
                image = request.FILES['image']
                if full_name and position and about != '':
                    update_about = About.objects.get(pk = 1)
                    update_about.full_name = full_name
                    update_about.position = position
                    update_about.about = about
                    os.remove(update_about.image.path)
                    update_about.image = image
                    update_about.save()
                    return HttpResponseRedirect(request.path_info)
                else:
                    return HttpResponseRedirect(request.path_info)
            except:
                full_name = request.POST.get('full_name')
                position = request.POST.get('position')
                about = request.POST.get('about')
                if full_name and position and about != '':
                    update_about = About.objects.get(pk = 1)
                    update_about.full_name = full_name
                    update_about.position = position
                    update_about.about = about
                    update_about.save()
                    return HttpResponseRedirect(request.path_info) 
                else:
                    return HttpResponseRedirect(request.path_info) 
        else:
            return redirect('home')

class WhatIdoView(View):
    def get(self, request):
        if request.user.is_authenticated:
            skills = Skill.objects.all().order_by('-pk')
            navbat_setting = get_object_or_404(NavbarSetting, pk = 1)
            return render(request, 'dashboard/what_i_do.html',{'skills':skills,'countmsgs':countmsgs, 'navbat_setting':navbat_setting})
        else:
            return redirect('/')

class WhatIdoAddView(View):
    msgs = None
    msgw = None
    def get(self, request):
        if request.user.is_authenticated:
            navbat_setting = get_object_or_404(NavbarSetting, pk = 1)
            return render(request, 'dashboard/add_what_i_do.html',{'countmsgs':countmsgs, 'navbat_setting':navbat_setting})
        else:
            return redirect('/')

    def post(self, request):
        if request.user.is_authenticated:
            navbat_setting = get_object_or_404(NavbarSetting, pk = 1)
            skill = request.POST.get('skill')
            description = request.POST.get('description')
            level = request.POST.get('level')
            image = request.FILES['image']
            if skill and description and level and image != '':
                if len(Skill.objects.filter(skill = skill)) == 0:
                    save_skill = Skill(
                        skill = skill,
                        description = description,
                        level = level,
                        image = image
                    )
                    save_skill.save()
                    msgs = "Skill added"
                    return render(request, 'dashboard/add_what_i_do.html',{
                        'msgs':msgs,'countmsgs':countmsgs
                    })
                else:
                    return HttpResponseRedirect(request.path_info) 
            else:
                return HttpResponseRedirect(request.path_info) 
        else:
            return redirect('/')

class EditSkill(View):
    def get(self, request, slug):
        if request.user.is_authenticated:
            skill = Skill.objects.get(slug = slug)
            navbat_setting = get_object_or_404(NavbarSetting, pk = 1)
            return render(request, 'dashboard/what_i_do_edit.html',{
                'skill':skill,'countmsgs':countmsgs,'navbat_setting':navbat_setting
            })
        else:
            return redirect('/')

    def post(self, request, slug):
        if request.user.is_authenticated:
            try:
                skill = request.POST.get('skill')
                description = request.POST.get('description')
                level = request.POST.get('level')
                image = request.FILES['image']
                if skill and description and level!= '':
                    save_skill = Skill.objects.get(slug = slug)
                    save_skill.skill = skill
                    save_skill.description = description
                    save_skill.level = level
                    os.remove(save_skill.image.path)
                    save_skill.image = image
                    save_skill.save()
                    return HttpResponseRedirect(request.path_info) 
                else:
                    return HttpResponseRedirect(request.path_info) 
            except:
                skill = request.POST.get('skill')
                description = request.POST.get('description')
                level = request.POST.get('level')
                if skill and description and level!= '':
                    save_skill = Skill.objects.get(slug = slug)
                    save_skill.skill = skill
                    save_skill.description = description
                    save_skill.level = level
                    save_skill.save()
                    return HttpResponseRedirect(request.path_info) 
                else:
                    return HttpResponseRedirect(request.path_info) 
        else:
            return redirect('/')

class DeleteSkill(View):
    def post(self, request):
        if request.user.is_authenticated:
            skill_id = request.POST.get('skill_id')
            skill = Skill.objects.filter(id = skill_id)
            os.remove(Skill.objects.get(id = skill_id).image.path)
            skill.delete()
            return redirect('whatido')  
        else:
            return redirect('/')         

class WhatIdoSettingsView(View):
    def get(self, request):
        if request.user.is_authenticated:
            what_i_do = WhatIdoSettings.objects.get(pk = 1)
            navbat_setting = get_object_or_404(NavbarSetting, pk = 1)
            return render(request, 'dashboard/what_i_do_settings.html',{
                'what_i_do':what_i_do,'countmsgs':countmsgs, 'navbat_setting':navbat_setting
            })
        else:
            return redirect('/')

    def post(self, request):
        if request.user.is_authenticated:
            description = request.POST.get('whatido')
            if description != '':
                what_i_do_settings = WhatIdoSettings.objects.get(pk = 1)
                what_i_do_settings.description = description
                what_i_do_settings.save()
                return HttpResponseRedirect(request.path_info) 
        else:
            return redirect('/')

class ViewProjectView(View):
    def get(self, request):
        if request.user.is_authenticated:
            projects = Projects.objects.all().order_by('-pk')
            navbat_setting = get_object_or_404(NavbarSetting, pk = 1)
            return render(request, 'dashboard/view_project.html',{'projects':projects,'countmsgs':countmsgs, 'navbat_setting':navbat_setting})
        else:
            return redirect('/')

class AddProjectView(View):
    def get(self, request):
        if request.user.is_authenticated:
            navbat_setting = get_object_or_404(NavbarSetting, pk = 1)
            return render(request, 'dashboard/add_project.html',{'countmsgs':countmsgs, 'navbat_setting':navbat_setting})
        else:
            return redirect('/')
    def post(self, request):
        if request.user.is_authenticated:
            project_name = request.POST.get('project_name')
            industry = request.POST.get('industry')
            website = request.POST.get('website')
            short_description = request.POST.get('short_description')
            client = request.POST.get('client')
            description = request.POST.get('description')
            image = request.FILES['image']
            if project_name and industry and short_description and description and image != '':
                if len(Projects.objects.filter(project_name = project_name)) == 0:
                    save_project = Projects(
                        project_name = project_name,
                        client = client,
                        industry = industry,
                        image = image,
                        website = website,
                        short_description = short_description,
                        description = description
                    )
                    save_project.save()
                    return HttpResponseRedirect(request.path_info)
                else:
                    return HttpResponseRedirect(request.path_info) 
        else:
            return redirect('/')

class DeleteProjectView(View):
    def post(self, request):
        if request.user.is_authenticated:
            project_id = request.POST.get('project_id')
            project = Projects.objects.filter(id = project_id)
            os.remove(Projects.objects.get(id = project_id).image.path)
            project.delete()
            return redirect('viewproject')  
        else:
            return redirect('/')


class ProjectEditView(View):
    def get(self, request, slug):
        if request.user.is_authenticated:
            get_project = Projects.objects.get(slug = slug)
            navbat_setting = get_object_or_404(NavbarSetting, pk = 1)
            return render(request, 'dashboard/edit_project.html',{'get_project':get_project,'countmsgs':countmsgs, 'navbat_setting':navbat_setting})
        else:
            return redirect('/')

    def post(self, request, slug):
        if request.user.is_authenticated:
            project_name = request.POST.get('project_name')
            industry = request.POST.get('industry')
            website = request.POST.get('website')
            short_description = request.POST.get('short_description')
            client = request.POST.get('client')
            description = request.POST.get('description')
            if project_name and industry and short_description and description:
                try:
                    image = request.FILES['image']
                    get_project = Projects.objects.get(slug = slug)
                    get_project.project_name = project_name
                    get_project.client = client
                    get_project.industry = industry
                    os.remove(get_project.image.path)
                    get_project.image = image
                    get_project.website = website
                    get_project.short_description = short_description
                    get_project.description = description
                    get_project.save()
                    return HttpResponseRedirect(request.path_info)
                except:
                    get_project = Projects.objects.get(slug = slug)
                    get_project.project_name = project_name
                    get_project.client = client
                    get_project.industry = industry
                    get_project.website = website
                    get_project.short_description = short_description
                    get_project.description = description
                    get_project.save()
                    return HttpResponseRedirect(request.path_info)
            else:
                return HttpResponseRedirect(request.path_info)
        else:
            return redirect('/')

class ProjectSettingView(View):
    def get(self, request):
        if request.user.is_authenticated:
            get_project_page_setting = ProjectSetting.objects.get(pk = 1)
            navbat_setting = get_object_or_404(NavbarSetting, pk = 1)
            return render(request, 'dashboard/project_page_setting.html',{
                'get_project_page_setting':get_project_page_setting,'countmsgs':countmsgs, 'navbat_setting':navbat_setting})
        else:
            return redirect('/')

    def post(self, request):
        if request.user.is_authenticated:
            description = request.POST.get('setting')
            save_description = ProjectSetting.objects.get(pk = 1)
            save_description.description = description
            save_description.save()
            return redirect('projectsetting')
        else:
            return redirect('/')



class CategoriesView(View):
    def get(self, request):
        if request.user.is_authenticated:
            categories = Categories.objects.all().order_by('-pk')
            navbat_setting = get_object_or_404(NavbarSetting, pk = 1)
            return render(request, 'dashboard/categories.html',{
                'categories':categories,'countmsgs':countmsgs, 'navbat_setting':navbat_setting})
        else:
            return redirect('/')

    def post(self, request):
        if request.user.is_authenticated:
            get_category_name = request.POST.get('category_name').capitalize()
            if get_category_name != '':
                if len(Categories.objects.filter(category_name = get_category_name)) == 0:
                    save_category = Categories(
                        category_name = get_category_name
                    )
                    save_category.save()
                    return HttpResponseRedirect(request.path_info)
                else:
                    return HttpResponseRedirect(request.path_info)
        else:
            return redirect('/')

class DeleteCategoryView(View):
    def post(self, request):
        if request.user.is_authenticated:
            get_category_pk = request.POST.get('ategory_id')
            get_category = Categories.objects.filter(pk = get_category_pk)
            get_category.delete()
            return redirect('categories')
        else:
            return redirect('/')


class AddBlogView(View):
    def get(self, request):
        if request.user.is_authenticated:
            navbat_setting = get_object_or_404(NavbarSetting, pk = 1)
            categories = Categories.objects.all().order_by('-category_name')
            return render(request, 'dashboard/add_blog.html',{'categories':categories,'countmsgs':countmsgs, 'navbat_setting':navbat_setting})
        else:
            return redirect('/')

    def post(self, request):
        if request.user.is_authenticated:
            title = request.POST.get('title')
            short_description = request.POST.get('short_description')
            description = request.POST.get('description')
            category = request.POST.get('category')
            status = request.POST.get('active')
            if status:
                status = True
            else:
                status = False
            image = request.FILES['image']
            if title and short_description and description and category and image != "":
                save_blog = Blog(
                    title = title,
                    image = image,
                    short_content = short_description,
                    content = description,
                    status = status,
                    category = Categories.objects.get(pk = category)
                )
                save_blog.save()
                return redirect('addblog')
            else:
                return redirect('addblog')
        else:
            return redirect('/')


class ViewBlogView(View):
    def get(self, request):
        if request.user.is_authenticated:
            blogs = Blog.objects.all().order_by('-pk')
            navbat_setting = get_object_or_404(NavbarSetting, pk = 1)
            return render(request, 'dashboard/view_blog.html',{'blogs':blogs, 'countmsgs':countmsgs, 'navbat_setting':navbat_setting})
        else:
            return redirect('/')

    def post(self, request):
        if request.user.is_authenticated:
            blog_id = request.POST.get('blog_id')
            get_blog = Blog.objects.filter(pk = blog_id)
            os.remove(Blog.objects.get(pk = blog_id).image.path)
            get_blog.delete()
            return redirect('viewblog')

class EditBlogView(View):
    def get(self, request, slug):
        if request.user.is_authenticated:
            blog = get_object_or_404(Blog, slug = slug)
            categories = Categories.objects.all().order_by('-category_name')
            navbat_setting = get_object_or_404(NavbarSetting, pk = 1)
            return render(request, 'dashboard/edit_blog.html',{
                'blog':blog, 'categories':categories,'countmsgs':countmsgs, 'navbat_setting':navbat_setting})
        else:
            return redirect('/')


    def post(self, request, slug):
        if request.user.is_authenticated:
            title = request.POST.get('title')
            short_description = request.POST.get('short_description')
            description = request.POST.get('description')
            category = request.POST.get('category')
            status = request.POST.get('active')
            if status:
                status = True
            else:
                status = False
            if title and short_description and description and category != "":
                try:
                    image = request.FILES['image']
                    get_blog = get_object_or_404(Blog, slug = slug)
                    get_blog.title = title
                    get_blog.short_content = short_description
                    get_blog.content = description
                    os.remove(get_blog.image.path)
                    get_blog.image = image
                    get_blog.status = status
                    get_blog.category = Categories.objects.get(pk = category)
                    get_blog.save()
                    return HttpResponseRedirect(request.path_info)
                except:
                    get_blog = get_object_or_404(Blog, slug = slug)
                    get_blog.title = title
                    get_blog.short_content = short_description
                    get_blog.content = description
                    get_blog.category = Categories.objects.get(pk = category)
                    get_blog.status = status
                    get_blog.save()
                    return HttpResponseRedirect(request.path_info)
            else:
                return HttpResponseRedirect(request.path_info)
        else:
            return redirect('/')


class MessagesDashboardView(View):
    def get(self, request):
        if request.user.is_authenticated:
            messages = Messages.objects.all().order_by('-pk')
            navbat_setting = get_object_or_404(NavbarSetting, pk = 1)
            return render(request, 'dashboard/messages.html',{'messages':messages,'countmsgs':countmsgs, 'navbat_setting':navbat_setting})
        else:
            return redirect('/')

    def post(self, request):
        if request.user.is_authenticated:
            message_id = request.POST.get("message_id")
            message = Messages.objects.filter(pk = message_id)
            message.delete()
            return redirect("messagesdashboard")
        else:
             return redirect('home')


class NavbarDashboardView(View):
    def get(self, request):
        if request.user.is_authenticated:
            navbat_setting = get_object_or_404(NavbarSetting, pk = 1)
            navbat_setting = get_object_or_404(NavbarSetting, pk = 1)
            return render(request, 'dashboard/setting.html',{'countmsgs':countmsgs,'navbat_setting':navbat_setting, 'navbat_setting':navbat_setting})
        else:
            return redirect('/')

    def post(self, request):
        if request.user.is_authenticated:
            try:
                fb = request.POST.get('fb')
                lin = request.POST.get('lin')
                insta = request.POST.get('in')
                tw = request.POST.get('tw')
                git = request.POST.get('git')
                about = request.POST.get('about')
                image = request.FILES['image']
                if about != "":
                    get_navbar = NavbarSetting.objects.get(pk = 1)
                    get_navbar.about = about
                    get_navbar.fb = fb
                    get_navbar.lin = lin
                    get_navbar.insta = insta
                    get_navbar.tw = tw
                    get_navbar.git = git
                    os.remove(get_navbar.image.path)
                    get_navbar.image = image
                    get_navbar.save()
                    return HttpResponseRedirect(request.path_info)
                else:
                    return HttpResponseRedirect(request.path_info)
            except:
                if about != "":
                    get_navbar = NavbarSetting.objects.get(pk = 1)
                    get_navbar.about = about
                    get_navbar.fb = fb
                    get_navbar.lin = lin
                    get_navbar.insta = insta
                    get_navbar.tw = tw
                    get_navbar.git = git
                    get_navbar.save()
                    return HttpResponseRedirect(request.path_info)
                else:
                    return HttpResponseRedirect(request.path_info)
        else:
            return redirect('/')



class ReadMessageDashboardView(View):
    def get(self, request, pk):
        if request.user.is_authenticated:
            get_message = get_object_or_404(Messages, pk = pk)
            navbat_setting = get_object_or_404(NavbarSetting, pk = 1)
            get_message.status = True
            get_message.save()
            return render(request, 'dashboard/read-message.html',{'countmsgs':countmsgs,'get_message':get_message, 'navbat_setting':navbat_setting})
        else:
            return redirect('home')



class SeoSettingDashboardView(View):
    def get(self, request):
        if request.user.is_authenticated:
            seo = SeoSettings.objects.get(pk = 1)
            navbat_setting = get_object_or_404(NavbarSetting, pk = 1)
            return render(request, 'dashboard/seo.html',{'countmsgs':countmsgs,'seo':seo, 'navbat_setting':navbat_setting})
        else:
            return redirect('home')

    def post(self, request):
        if request.user.is_authenticated:
            try:
                description = request.POST.get('description')
                keywords = request.POST.get('keywords')
                sitename = request.POST.get('sitename')
                image = request.FILES['image']
                seo = SeoSettings.objects.get(pk = 1)
                seo.description = description
                seo.keywords = keywords
                seo.sitename = sitename
                os.remove(seo.image.path)
                seo.image = image
                seo.save()
                return HttpResponseRedirect(request.path_info)
            except:
                description = request.POST.get('description')
                keywords = request.POST.get('keywords')
                sitename = request.POST.get('sitename')
                seo = SeoSettings.objects.get(pk = 1)
                seo.description = description
                seo.keywords = keywords
                seo.sitename = sitename
                seo.save()
                return HttpResponseRedirect(request.path_info)
        else:
            return redirect('home')



class EmailDashboardView(View):
    def get(self, request):
        if request.user.is_authenticated:
            email_setting = EmailSetting.objects.get(pk = 1)
            navbat_setting = get_object_or_404(NavbarSetting, pk = 1)
            return render(request, 'dashboard/email_setting.html',{'email_setting':email_setting, 'countmsgs':countmsgs,
            'navbat_setting':navbat_setting})
        else:
            return redirect('home')

    def post(self, request):
        if request.user.is_authenticated:
            email_host = request.POST.get("email_host")
            email_use_tls = request.POST.get("email_use_tls")
            email_host_user = request.POST.get("email_host_user")
            email_port = request.POST.get("email_port")
            email_host_password = request.POST.get("email_host_password")
            if email_use_tls:
                email_use_tls = True
            else:
                email_use_tls = False
            email_setting = EmailSetting.objects.get(pk = 1)
            email_setting.email_host = email_host
            email_setting.email_use_tls = email_use_tls
            email_setting.email_host_user = email_host_user
            email_setting.email_port = email_port
            email_setting.email_host_password = email_host_password
            email_setting.save()
            return HttpResponseRedirect(request.path_info)
        else:
            return redirect('home')


class TestimonialsDashboardView(View):
    def get(self, request):
        if request.user.is_authenticated:
            navbat_setting = get_object_or_404(NavbarSetting, pk = 1)
            testimonials = Testimonials.objects.all().order_by('-pk')
            return render(request, 'dashboard/testimonials.html',{'countmsgs':countmsgs,
            'navbat_setting':navbat_setting,'testimonials':testimonials})
        else:
             return redirect('home')

    def post(self, request):
        if request.user.is_authenticated:
            testimonial_id = request.POST.get("testimonial_id")
            testimonial = Testimonials.objects.filter(pk = testimonial_id)
            try:
                os.remove(Testimonials.objects.get(id = testimonial_id).image.path)
            except:
                pass
            testimonial.delete()
            return redirect("testimonialsdashboard")
        else:
             return redirect('home')

def statuschange(request, pk):
    if request.user.is_authenticated:
        testimonials = Testimonials.objects.get(pk = pk)
        if testimonials.status == False:
            testimonials.status = True
            testimonials.save()
            return redirect("testimonialsdashboard")
        else:
            testimonials.status = False
            testimonials.save()
            return redirect("testimonialsdashboard")
    else:
        return redirect('home')


class VisitorsDashboardView(View):
    def get(self, request):
        if request.user.is_authenticated:
            navbat_setting = get_object_or_404(NavbarSetting, pk = 1)
            visitors = UserData.objects.all().order_by('-date_update')
            seen = UserDataSeen.objects.all()

            paginator = Paginator(visitors, 10) # Show 25 contacts per page.
            page_number = request.GET.get('page')
            visitors = paginator.get_page(page_number)

            return render(request, 'dashboard/visitors.html',{'countmsgs':countmsgs,
            'navbat_setting':navbat_setting,"visitors":visitors,"seen":seen})
        else:
            return redirect('home')


class VisitorMoreInfoDashboardView(View):
    def get(self, request, pk):
        if request.user.is_authenticated:
            navbat_setting = get_object_or_404(NavbarSetting, pk = 1)
            visitor = UserData.objects.get(pk = pk)
            info = UserUrlData.objects.filter(userdata = visitor).order_by('-pk')
            seen = UserDataSeen.objects.get(userdata = visitor)
            seen.seen = True
            seen.save()
            return render(request, 'dashboard/visitor_info.html',{'countmsgs':countmsgs,
            'navbat_setting':navbat_setting,"visitor":visitor,"info":info})
        else:
            return redirect('home')


class LogoutDashboardView(View):
    def get(self, request):
        if request.user.is_authenticated:
            logout(request)
            return redirect('home')
        else:
            return redirect('home')
    