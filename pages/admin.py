from django.contrib import admin

from .models import (ApplyJob, Company, Industry, Job, Resume, State, User,
                     review)

# Register your models here.
admin.site.register(Resume)
admin.site.register(Company)
admin.site.register(User)
admin.site.register(Job)
admin.site.register(ApplyJob)
admin.site.register(Industry)
admin.site.register(State)
admin.site.register(review)
