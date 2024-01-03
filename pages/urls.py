from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('register_app/', views.register_app, name='register_app'),
    path('register_rec/', views.register_rec, name='register_rec'),
    path('login/', views.pagelogin, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('', views.proxy, name='proxy'),
    path('app-dash/', views.app_dash, name='app-dash'),
    path('rec-dash/', views.rec_dash, name='rec-dash'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('company/', views.company, name='company'),
    path('company-details/<int:pk>/', views.company_details, name='company-details'),
    path('resume/', views.resume, name='resume'),
    path('resume_details/', views.resum_details, name='resume_details'),
    path('create-job/', views.create_job, name='create-job'),
    path('update-job/<int:pk>/', views.update_job, name='update-job'),
    path('job_listing/', views.listen_job, name='job_listing'),
    path('job_details/<int:pk>/', views.job_details, name='job_details'),
    path('manage_jobs/', views.manage_jobs, name='manage_jobs'),
    path('apply/<int:pk>/', views.apply, name='apply'),
    path('all_applicants/<int:pk>/', views.all_applicants, name='all_applicants'),
    path('alljobs/', views.alljobs, name='alljobs'),
    path('applied_jobs/', views.applied_jobs, name='applied_jobs'),


    
    ]