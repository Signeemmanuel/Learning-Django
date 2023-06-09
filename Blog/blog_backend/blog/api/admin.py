from django.contrib import admin
from .models import Articles


# admin.site.register(Articles)

@admin.register(Articles)
class ArticlesAdmin(admin.ModelAdmin):
    list_filter = ('title', 'description')
    list_display = ('title', 'description') 