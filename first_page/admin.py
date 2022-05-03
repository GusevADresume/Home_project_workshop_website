from django.contrib import admin
from first_page.models import Article

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['id','title', 'text', 'img']
