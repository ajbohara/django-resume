from django.contrib import admin

# Register your models here.
from .models import School, Company, Education, Experience, UserProfile, Address, Skill, SchoolProject


admin.site.register(School, list_display=['name'])
admin.site.register(Company)
admin.site.register(Education)
admin.site.register(Experience)
admin.site.register(UserProfile)
admin.site.register(Address)
admin.site.register(Skill)
admin.site.register(SchoolProject)
