from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class User(AbstractUser):
 email=models.EmailField(unique=True) 
 is_recruiter =models.BooleanField(default=False)
 is_applicant =models.BooleanField(default=False)
 has_resume =models.BooleanField(default=False)
 has_company =models.BooleanField(default=False)
 def __str__(self):
      	return self.email
class Resume(models.Model):
  user=models.OneToOneField(User,on_delete=models.CASCADE)
  first_name=models.CharField(max_length=100,null=True,blank=True)
  last_name=  models.CharField(max_length=100,null=True,blank=True)
  job_title=models.CharField(max_length=100)
  location=models.CharField(max_length=100)
  upload_resume=models.FileField(upload_to='resume',null=True,blank=True)
  def __str__(self):
      return f'{self.first_name}{self.last_name}'

class Company(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    name=models.CharField(max_length=100,null=True,blank=True)
    date=models.PositiveIntegerField(null=True,blank=True)
    city=models.CharField(max_length=100,null=True,blank=True)
    country=models.CharField(max_length=100,null=True,blank=True)
    def __str__(self):
      return str(self.name)

class State(models.Model):
  name=models.CharField(max_length=100)  
  def __str__(self):
    return str(self.name)


class Industry(models.Model):
  name=models.CharField(max_length=100)  
  def __str__(self):
    return str(self.name)
class Job(models.Model):
    job_type_choices=(
      ('Remote','Remote'),
      ('onSite','onSite'),

    )
    
    country=models.CharField(max_length=100)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    company=models.ForeignKey(Company,on_delete=models.CASCADE)
    title=models.CharField(max_length=100)
    salary=models.PositiveIntegerField(default=30000)
    requirements=models.TextField()
    ideal_candidate=models.TextField()
    is_available=models.BooleanField(default=True)
    timestamp=models.DateTimeField(auto_now_add=True)
    industry=models.ForeignKey(Industry,on_delete=models.DO_NOTHING,null=True,blank=True)
    city=models.ForeignKey(State,on_delete=models.DO_NOTHING,null=True,blank=True)
    job_type=models.CharField(max_length=100,choices=job_type_choices)

    def __str__(self):
      return self.title
       
class ApplyJob(models.Model):
  status=(
    ('Accepted','Accepted'),
    ('Declined','Declined'),
    ('pendin','pending'),

  )
  user=models.ForeignKey(User,on_delete=models.CASCADE)
  job=models.ForeignKey(Job,on_delete=models.CASCADE)
  timestamp=models.DateTimeField(auto_now_add=True)
  status=models.CharField(max_length=100,choices=status)


class review(models.Model):
			text= models.TextField(max_length=300)
			# customer=models.ForeignKey(Company,on_delete=models.SET_NULL,null=True)
			resume=models.ForeignKey(Resume,on_delete=models.SET_NULL,null=True)
			created=models.DateTimeField(auto_now_add=True)

			def __str__(self):
      				return self.text