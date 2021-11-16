from django.contrib import admin
from MUES.models import Tasks,Users,Videos,Projects
# Register your models here.

admin.site.register(Users)
admin.site.register(Projects)
admin.site.register(Tasks)
admin.site.register(Videos)