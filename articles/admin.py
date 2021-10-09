from django.contrib import admin

from .models import Article

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'body',)
    prepopulated_fields = {'slug': ('title',)} # allows the slug to be prepopulated with title field

admin.site.register(Article, ArticleAdmin)
