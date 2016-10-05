from django.contrib import admin
from .models import Blog


class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'owner', 'updateDateTime',)
    list_editable = ('title',)
    list_display_links = ('updateDateTime', 'owner')
    list_filter = ('updateDateTime','createDateTime')
    search_fields = ('title', 'image', 'content', 'createDateTime', 'updateDateTime')


admin.site.register(Blog, BlogAdmin)