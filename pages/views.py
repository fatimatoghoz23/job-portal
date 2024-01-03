from urllib import request

from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
# from rest_framework.response import Response
# from rest_framework.views import APIView

from .form import (CompanyForm, JobFilter, JobForm, RegisterUserForm,
                   ResumeForm, UpdateJobForm, reviewss)
from .models import ApplyJob, Company, Job, Resume, User, review


# Create your views here.
def index(request):
  filter=JobFilter(request.GET, queryset=Job.objects.filter(is_available=True).order_by('-timestamp'))
  technology=Job.objects.filter(industry=1).count()
  industry=Job.objects.filter(industry=2).count()
  educational=Job.objects.filter(industry=3).count()

  return render(request,'index.html',{'filter':filter,'reviews':review.objects.all(),'jobs':Job.objects.all(),'technology':technology
  ,'industry':industry,'educational':educational})
def alljobs(request):
  filter=JobFilter(request.GET, queryset=Job.objects.filter(is_available=True).order_by('-timestamp'))

  return render(request,'alljobs.html',{'filter':filter})
def listen_job(request):
 filter=JobFilter(request.GET, queryset=Job.objects.filter(is_available=True).order_by('-timestamp'))

 jobs=Job.objects.filter(is_available=True).order_by('-timestamp')
 return render(request,'job_listing.html',{'jobs':jobs,'filter':filter})

def pagelogin(request):
       if request.method == 'POST':
            email= request.POST.get('email')
            password= request.POST.get('password')
            user =authenticate(request, username= email, password= password)  
            if user is not None and user.is_active:
                login(request , user)
                if request.user.is_applicant:
                  return render(request,'app-dash.html')            
                elif request.user.is_recruiter:
                  return render(request,'rec-dash.html')            
                else:
                   return redirect('login')
            else:
            
                messages.info(request,'Username OR password is incorrect')
                return redirect('login')
       else:
         return render(request,'login.html',{})        
def logoutUser(request):
    logout(request)
    return redirect('login')  

def register_app(request):
                if request.method == "POST":
                  form=RegisterUserForm(request.POST)
                  if form.is_valid():
                      u= form.save(commit=False)
                      u.is_applicant =True
                      u.username=u.email
                      u.save()
                      Resume.objects.create(
                        user = u 
                    )
                      messages.info(request,'Your account has be created')
                      return redirect('login')
                  else:
                      messages.warning(request,'somthing went wrong')
                      return redirect('register_app')
                else:
                  form=RegisterUserForm()
                  return render(request,'register-app.html',{'form':form})            

def register_rec(request):
         if request.method == "POST":
                  form=RegisterUserForm(request.POST)
                  if form.is_valid():
                      u= form.save(commit=False)
                      u.is_recruiter =True
                      u.username=u.email
                      u.save()
                      Company.objects.create(
                        user = u 
                    )
                      messages.info(request,'Your account has be created')
                      return redirect('login')
                  else:
                      messages.warning(request,'somthing went wrong')
                      return redirect('register_rec')
         else:
                  form=RegisterUserForm()
                  return render(request,'register-rec.html',{'form':form})            
def proxy(request):
  if request.user.is_applicant:
    return redirect('app-dash')
  elif request.user.is_recruiter:
    return redirect('rec-dash')
  else:
     return redirect('login')
def dashboard(request):
  return render(request,'dashboard.html')     

def app_dash(request):
  return render(request,'app-dash.html')     
def rec_dash(request):
  return render(request,'rec-dash.html')  

def company(request):
 if request.user.is_recruiter: 
   company=Company.objects.get(user=request.user)
   if request.method == "POST":
       form=CompanyForm(request.POST,instance=company)
       if form.is_valid():
         v= form.save(commit=False)
         user =User.objects.get(id=request.user.id)
         user.has_company =True
         v.save()
         user.save()
         
         messages.info(request,'Your company is now active,you can creating job')
         return redirect('dashboard')
       else:
           messages.warning(request,'somthing went wrong')
   else:
    form=CompanyForm(instance=company)
    return render(request,'company.html',{'form':form})
 else:
  return redirect('dashboard')

def company_details(request, pk):
  company=Company.objects.get(pk=pk)
  return render(request,'company_details.html',{'company':company})

def resume(request):
 if request.user.is_applicant: 
   resume=Resume.objects.get(user=request.user)
   if request.method == "POST":
       form=ResumeForm(request.POST,request.FILES,instance=resume)
       if form.is_valid():
         v=form.save(commit=False)
         user =User.objects.get(id=request.user.id)
         user.has_resume =True
         v.save()
         user.save()
         messages.info(request,'Your resume updated')
         return redirect('dashboard')
       else:
           messages.warning(request,'somthing went wrong')
   else:
    form=ResumeForm(instance=resume)
    return render(request,'resume.html',{'form':form})
 else:
      return redirect('dashboard')

def resum_details(request, pk):
   resume=Resume.objects.get(pk=pk)
   return render(request,'resume_details.html',{'resume':resume})

def create_job(request):

 if request.user.is_recruiter and request.user.has_company: 
    if request.method == "POST":
       form=JobForm(request.POST)
       if form.is_valid():
         v= form.save(commit=False)
         v.user = request.user
         v.company = request.user.company
         v.save()
         messages.info(request,'new job has been created')
         return redirect('dashboard')
       else:
           messages.warning(request,'somthing went wrong')
           return redirect('create-job')
    else:
     form=JobForm()
     return render(request,'create-job.html',{'form':form})
 else:
    messages.warning(request,'somthing went wrong')
    return redirect('create-job')

def update_job(request, pk):
  job=Job.objects.get(pk=pk)

  if request.method == "POST":
       
       form=UpdateJobForm(request.POST,instance=job)
       if form.is_valid():
         form.save()
         messages.info(request,'your job info is update')
         return redirect('dashboard')
       else:
           messages.warning(request,'somthing went wrong')
  else:
    form=UpdateJobForm(instance=job)
    return render(request,'create-job.html',{'form':form})    
def job_details(request,pk):
  # user=request.user,
  if ApplyJob.objects.filter(job=pk).exists():
    has_applied=True
  else:
    has_applied=False
  # if request.user.is_applicant: 

  #   if request.method == 'POST':
  #        add_comment = reviewss(request.POST)
  #        reviews= add_comment.save(commit=False)
  #        reviews.resume = request.user.resume
  #        reviews.save()
        #  messages.success(request,'your review was successfully submitted!')

  job=Job.objects.get(pk=pk)
  return render(request,'job_details.html',{'jobs':job,'has_applied':has_applied,'reviews':reviewss()}) 

def manage_jobs(request):
  job=Job.objects.filter(user=request.user,company=request.user.company)
  # job=Job.objects.all()

  return render(request,'manage_job.html',{'jobs':job})    
def apply(request,pk):
 if request.user.is_authenticated  and request.user.is_applicant: 
    job=Job.objects.get(pk=pk)
    if ApplyJob.objects.filter(user=request.user,job=pk).exists():
      messages.warning(request,'permission Denied')
      return redirect('dashboard')
    else:
      ApplyJob.objects.create(
        job=job,
        user=request.user,
        status='pending'
      )
      messages.info(request,'applied')
      return redirect('dashboard')
 else:
      messages.info(request,'login to continue')
      return redirect('login')

def all_applicants(request,pk):
    job=Job.objects.get(pk=pk)
    applicants=job.applyjob_set.all()

    return render(request,'all_applicants.html',{'jobs':job,'applicants':applicants})    

def applied_jobs(request):
  job=ApplyJob.objects.filter(user=request.user)   
  return render(request,'applied_jobs.html',{'jobs':job})    
