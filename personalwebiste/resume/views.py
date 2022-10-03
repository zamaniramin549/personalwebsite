import os
from ast import Return
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.http import HttpResponseRedirect
from home.models import Messages
from resume.models import *
from dashboard.models import NavbarSetting

# Create your views here.
countmsgs = Messages.objects.filter(status = False).count
class ResumeDashboardView(View):
    def get(self, request):
        if request.user.is_authenticated:
            navbat_setting = get_object_or_404(NavbarSetting, pk = 1)
            resume_header = get_object_or_404(ResumeHeader, pk=1)
            resume_about = get_object_or_404(ResumeAbout, pk=1)
            resume_technical_skills = get_object_or_404(ResumeTechnicalSkill, pk=1)
            resume_professional_skills = get_object_or_404(ResumeProfessionalSkill, pk=1)
            resume_interest = get_object_or_404(ResumeInterests, pk=1)
            work_exper = ResumeWorkExpe.objects.all().order_by('-pk')
            projects = ResumeProject.objects.all().order_by('-pk')
            resume_education = ResumeEducation.objects.all().order_by('-pk')
            resume_awards = ResumeAwards.objects.all().order_by('-pk')
            resume_langs = ResumeLang.objects.all().order_by('-pk')
            return render(request, 'resume/resume.html',{
                'countmsgs':countmsgs,'resume_header':resume_header,
                'resume_about':resume_about,"resume_technical_skills":resume_technical_skills,
                'resume_professional_skills':resume_professional_skills,'work_exper':work_exper,
                'projects':projects,'resume_education':resume_education,'resume_awards':resume_awards,
                'resume_langs':resume_langs,'resume_interest':resume_interest,'navbat_setting':navbat_setting})
        else:
            return redirect('/')


class ResumeHeaderView(View):
    def post(self, request):
        if request.user.is_authenticated:
            full_name = request.POST.get('full_name')
            position = request.POST.get('position')
            email = request.POST.get('email')
            phone = request.POST.get('phone')
            website = request.POST.get('website')
            if full_name and position != "":
                save_update = ResumeHeader.objects.get(pk=1)
                save_update.full_name = full_name
                save_update.position = position
                save_update.email = email
                save_update.phone = phone
                save_update.website = website
                save_update.save()
                return redirect('resumedashboard')
            else:
                return redirect('resumedashboard')
        else:
            return redirect('/')


class ResumeAboutView(View):
    def post(self, request):
        if request.user.is_authenticated:
            about = request.POST.get('content')
            try:
                image = request.FILES['image']
                if about and image != "":
                    save_update = ResumeAbout.objects.get(pk=1)
                    save_update.about = about
                    os.remove(save_update.image.path)
                    save_update.image = image
                    save_update.save()
                    return redirect('resumedashboard')
                else:
                    return redirect('resumedashboard')
            except:
                if about != "":
                    save_update = ResumeAbout.objects.get(pk=1)
                    save_update.about = about
                    save_update.save()
                    return redirect('resumedashboard')
                else:
                    return redirect('resumedashboard')
        else:
            return redirect('/')


class ResumeTechnicalSkillsView(View):
    def post(self, request):
        if request.user.is_authenticated:
            technical_skill = request.POST.get('technical_skill')
            save_update = ResumeTechnicalSkill.objects.get(pk=1)
            save_update.skills = technical_skill
            save_update.save()
            return redirect('resumedashboard')
        else:
            return redirect('/')


class ResumeProfessionalSkillsView(View):
    def post(self, request):
        if request.user.is_authenticated:
            technical_skill = request.POST.get('professional_skill')
            save_update = ResumeProfessionalSkill.objects.get(pk=1)
            save_update.skills = technical_skill
            save_update.save()
            return redirect('resumedashboard')
        else:
            return redirect('/')


class ResumeWorkExperienceView(View):
    def post(self, request):
        if request.user.is_authenticated:
            title = request.POST.get('title')
            company = request.POST.get('company')
            duration = request.POST.get('duration')
            content = request.POST.get('content')
            if title and company and duration and content != "":
                save_work = ResumeWorkExpe(
                    title = title,
                    company_name = company,
                    duration = duration,
                    content = content
                )
                save_work.save()
                return redirect('resumedashboard')
            else:
                return redirect('resumedashboard')
        else:
            return redirect('/')


class ResumeprojectView(View):
    def post(self, request):
        if request.user.is_authenticated:
            project_name = request.POST.get('project_name')
            website = request.POST.get('website')
            content = request.POST.get('content')
            if project_name and content != "":
                save_project = ResumeProject(
                    project_name = project_name,
                    website = website,
                    content = content
                )
                save_project.save()
                return redirect('resumedashboard')
            else:
                return redirect('resumedashboard')
        else:
            return redirect('home')


class DelWorkExp(View):
    def post(self, request):
        if request.user.is_authenticated:
            work_pk = request.POST.get('work_exp_pk')
            get_work = ResumeWorkExpe.objects.filter(pk = work_pk)
            get_work.delete()
            return redirect('resumedashboard')
        else:
             return redirect('home')


class EditWorkExp(View):
    def get(self, request, pk):
        if request.user.is_authenticated:
            navbat_setting = get_object_or_404(NavbarSetting, pk = 1)
            getwork = get_object_or_404(ResumeWorkExpe, pk = pk)
            return render(request, "resume/work_resume_edit.html",{'getwork':getwork,'countmsgs':countmsgs,'navbat_setting':navbat_setting})
        else:
             return redirect('home')


    def post(self, request, pk):
        if request.user.is_authenticated:
            title = request.POST.get('title')
            company = request.POST.get('company')
            duration = request.POST.get('duration')
            content = request.POST.get('content')
            if title and company and duration and content != "":
                save_work = get_object_or_404(ResumeWorkExpe, pk = pk)
                save_work.title = title
                save_work.company_name = company
                save_work.duration = duration
                save_work.content = content
                save_work.save()
                return redirect('resumedashboard')
            return redirect('resumedashboard')
        else:
             return redirect('home')



class DelProject(View):
    def post(self, request):
        if request.user.is_authenticated:
            getproject_pk = request.POST.get('project_pk')
            project = ResumeProject.objects.filter(pk = getproject_pk)
            project.delete()
            return redirect('resumedashboard')
        else:
             return redirect('home')


class EditProject(View):
    def get(self, request, pk):
        if request.user.is_authenticated:
            navbat_setting = get_object_or_404(NavbarSetting, pk = 1)
            getproject = get_object_or_404(ResumeProject, pk = pk)
            return render(request, "resume/project_resume_edit.html",{'getproject':getproject,'countmsgs':countmsgs,'navbat_setting':navbat_setting})
        else:
             return redirect('home')


    def post(self, request, pk):
        if request.user.is_authenticated:
            project_name = request.POST.get('project_name')
            website = request.POST.get('website')
            content = request.POST.get('content')
            if project_name and content != "":
                save_project = get_object_or_404(ResumeProject, pk = pk)
                save_project.project_name = project_name
                save_project.website = website
                save_project.content = content
                save_project.save()
                return redirect('resumedashboard')
            else:
                return redirect('resumedashboard')
        else:
            return redirect('home')

class ResumeAddEducationView(View):
    def post(self, request):
        if request.user.is_authenticated:
            subject = request.POST.get('subject')
            university = request.POST.get('university')
            year = request.POST.get('year')
            if subject and university and year != "":
                save = ResumeEducation(
                    subject = subject,
                    university = university,
                    year = year
                )
                save.save()
                return redirect('resumedashboard')
            else:
                return redirect('resumedashboard')
        else:
            return redirect('home')


class ResumeDeleteEducationView(View):
    def post(self, request):
        if request.user.is_authenticated:
            education_pk = request.POST.get('education_pk')
            get_education = ResumeEducation.objects.filter(pk = education_pk)
            get_education.delete()
            return redirect('resumedashboard')
        else:
            return redirect('home')


class ResumeEditEducationView(View):
    def get(self, request, pk):
        if request.user.is_authenticated:
            navbat_setting = get_object_or_404(NavbarSetting, pk = 1)
            get_education = get_object_or_404(ResumeEducation, pk = pk)
            return render(request, 'resume/education_resume_edit.html',{'get_education':get_education,'countmsgs':countmsgs,'navbat_setting':navbat_setting})
        else:
            return redirect('home')


    def post(self, request, pk):
        if request.user.is_authenticated:
            subject = request.POST.get('subject')
            university = request.POST.get('university')
            year = request.POST.get('year')
            if subject and university and year != "":
                get_education = ResumeEducation.objects.get(pk = pk)
                get_education.subject = subject
                get_education.university = university
                get_education.year = year
                get_education.save()
                return redirect('resumedashboard')
            else:
                return redirect('resumedashboard')
        else:
            return redirect('home')



class ResumeAddAwardView(View):
   def post(self, request):
        if request.user.is_authenticated:
            award = request.POST.get('award')
            award_titl = request.POST.get('award-title')
            if award_titl and award != "":
                save = ResumeAwards(
                    award = award,
                    award_title = award_titl
                )
                save.save()
                return redirect('resumedashboard')
            else:
                return redirect('resumedashboard')
        else:
            return redirect('home')


class ResumeDeleteAwardView(View):
    def post(self, request):
        if request.user.is_authenticated:
            award = request.POST.get('award_pk')
            get_award = ResumeAwards.objects.filter(pk = award)
            get_award.delete()
            return redirect('resumedashboard')
        else:
            return redirect('home')


class ResumeEditAwardView(View):
    def get(self, request, pk):
        if request.user.is_authenticated:
            navbat_setting = get_object_or_404(NavbarSetting, pk = 1)
            award = get_object_or_404(ResumeAwards, pk = pk)
            return render(request, 'resume/award_resume_edit.html',{'award':award,'countmsgs':countmsgs, 'navbat_setting':navbat_setting})
        else:
            return redirect('home')

    def post(self, request, pk):
        if request.user.is_authenticated:
            award = request.POST.get('award')
            award_titl = request.POST.get('award-title')
            if award and award_titl != "":
                get_award = ResumeAwards.objects.get(pk = pk)
                get_award.award = award
                get_award.award_title = award_titl
                get_award.save()
                return redirect('resumedashboard')
            else:
                return redirect('resumedashboard')
        else:
            return redirect('home')


class ResumeAddLangView(View):
    def post(self, request):
        if request.user.is_authenticated:
            langname = request.POST.get('language')
            langlevel = request.POST.get('level')
            if langname and langlevel != "":
                save_lang = ResumeLang(
                    language = langname,
                    language_level = langlevel
                )
                save_lang.save()
                return redirect('resumedashboard')
            else:
                return redirect('resumedashboard')
        else:
            return redirect('home')

class ResumeDeleteLangView(View):
    def post(self, request):
        if request.user.is_authenticated:
            get_pk = request.POST.get('lang_pk')
            get_lng = ResumeLang.objects.filter(pk = get_pk)
            get_lng.delete()
            return redirect('resumedashboard')
        else:
            return redirect('home')


class ResumeEditLangView(View):
    def get(self, request, pk):
        if request.user.is_authenticated:
            navbat_setting = get_object_or_404(NavbarSetting, pk = 1)
            lang = get_object_or_404(ResumeLang, pk = pk)
            return render(request, 'resume/lang_resume_edit.html',{'lang':lang,'countmsgs':countmsgs, 'navbat_setting':navbat_setting})
        else:
            return redirect('home')

    def post(self, request, pk):
        if request.user.is_authenticated:
            langname = request.POST.get('language')
            langlevel = request.POST.get('level')
            if langname and langlevel != "":
                lang = ResumeLang.objects.get(pk = pk)
                lang.language = langname
                lang.language_level = langlevel
                lang.save()
                return redirect('resumedashboard')
            else:
                return redirect('resumedashboard')
        else:
            return redirect('home')
            

class ResumeUpdateInterestView(View):
    def post(self, request):
        if request.user.is_authenticated:
            get_content = request.POST.get('interests')
            save_update = ResumeInterests.objects.get(pk = 1)
            save_update.interests = get_content
            save_update.save()
            return redirect('resumedashboard')
        else:
            return redirect('home')