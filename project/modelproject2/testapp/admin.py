from django.contrib import admin
from testapp.models import Job
# Register your models here.


class JobAdmin(admin.ModelAdmin):
    list_display=['id','epost','elocat','esal','equal']


admin.site.register(Job,JobAdmin)
# Register your models here.
