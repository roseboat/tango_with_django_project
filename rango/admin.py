from django.contrib import admin
from rango.models import Category, Page

# Add in this class to customise the Admin Interface
class CategoryAdmin(admin.ModelAdmin):
    prepopulates_fields = {'slug':('name',)}

class PageAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'url')


# Update the registration to include this customise interface
admin.site.register(Category, CategoryAdmin)
admin.site.register(Page, PageAdmin)

