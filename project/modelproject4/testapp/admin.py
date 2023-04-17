from django.contrib import admin
from testapp.models import Customer
# Register your models here.


class CustomerAdmin(admin.ModelAdmin):
    list_display=['id','ename','ephone','eaccount','eage']


admin.site.register(Customer,CustomerAdmin)
# Register your models here.
# Register your models here.
