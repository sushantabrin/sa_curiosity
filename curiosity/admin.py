from django.contrib import admin
# from tinymce import TinyMCE
from .models import Category, Post

# Register your models here.

# for configuration of category admin

# class TinyMCEWidget(TinyMCE):
#     def use_required_attribute(self, *args):
#         return False

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('image_tag','title','description','date_added',)
    search_fields = ('title',)
    list_per_page = 10

class PostAdmin(admin.ModelAdmin):
    list_display = ('title','date_added')
    search_fields = ('title',)
    list_filter = ('cat',)
    list_per_page = 20

admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)


# This was written by Sushant Abrin
