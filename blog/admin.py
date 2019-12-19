from django.contrib import admin
from .models import Post, Category ,Comment,Profile


class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user']

admin.site.register(Profile, ProfileAdmin)
admin.site.register(Post)
admin.site.register(Category)
admin.site.register(Comment)