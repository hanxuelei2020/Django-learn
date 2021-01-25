from django.contrib import admin
from HelloWorld.models import *
# Register your models here.

class BookInfoAdmin(admin.ModelAdmin):
    list_display = ['id', 'book_name', 'book_privce', 'book_date']

class HeroInfoAdmin(admin.ModelAdmin):
    list_display = ['id', 'hname', 'hgender', 'hcomment', 'hbook']


admin.site.register(HeroInfo, HeroInfoAdmin)
admin.site.register(BookInfo, BookInfoAdmin)

