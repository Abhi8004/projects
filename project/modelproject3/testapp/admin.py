from django.contrib import admin
from testapp.models import Book
# Register your models here.


class BookAdmin(admin.ModelAdmin):
    list_display=['id','eno','etitle','eaut','edate']


admin.site.register(Book,BookAdmin)
# Register your models here.
