from django.contrib import admin
from . models import NewsCategori, NewsDetails, NewsAbout, Details, Contact, Info
from .models import GeeksModel

class CategoriAdmin(admin.ModelAdmin):
    model= NewsCategori
    list_display = ['categori_name']

admin.site.register(NewsCategori, CategoriAdmin)


class NewsDetailAdmin(admin.ModelAdmin):
    model= NewsDetails
    list_display =['title','image','categori']
admin.site.register(NewsDetails, NewsDetailAdmin)

class AboutAdmin(admin.ModelAdmin):
    model= NewsAbout
    list_display = ['categori_name']

admin.site.register(NewsAbout,AboutAdmin)

class DetailAdmin(admin.ModelAdmin):
    model= Details
    list_display =['title','image',]
admin.site.register(Details,DetailAdmin)

class ContactAdmin(admin.ModelAdmin):
    model= Contact
    list_display= ['name','email','message','subject']
admin.site.register(Contact,ContactAdmin)

class InfoAdmin(admin.ModelAdmin):
    model= Info
    list_display= ['location','contact','email']
admin.site.register(Info,InfoAdmin)


# class NewDetailsAdmin(admin.TabularInline):
#     model = NewsDetails

# class CategoriNewAdmin(admin.ModelAdmin):
#     inlines =[NewDetailsAdmin,]
#     list_display = ['categori_name']
# admin.site.register(NewsCategori,CategoriNewAdmin)

admin.site.register(GeeksModel)