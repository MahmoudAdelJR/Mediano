from django.contrib import admin
from .models import Article

# Register your models here.

#admin.site.register(Article)
@admin.register(Article)
class Article_reg(admin.ModelAdmin):
    list_display = ['title', 'slug', 'author']
    list_filter = ['title', 'slug', 'author', 'created']
    search_fields = ['title', 'body']
    date_hierarchy = 'created'
    ordering = ('created',)
    prepopulated_fields = {'slug':('title',)}
    raw_id_fields = ('author', )
