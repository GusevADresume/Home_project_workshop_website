from django.contrib import admin
from django.urls import include, path, re_path
from workshop_blog.models import Article,ArticlePhoto,Vk_data
from django.http import HttpResponseRedirect
from workshop_blog.blog_writer import BolgWriter


class PhotoInLine(admin.StackedInline):
    model = ArticlePhoto

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [PhotoInLine, ]


@admin.register(Vk_data)
class Vk_dataAdmin(admin.ModelAdmin):
    change_list_template = "workshop_blog/model_change_list.html"

    def process_import(self,value):
        print('work func writer')
        bw = BolgWriter()
        bw.writer()
        return HttpResponseRedirect("../")

    def get_urls(self):
        print('work func get urls')
        urls = super(Vk_dataAdmin, self).get_urls()
        custom_urls = [re_path('^import/$', self.process_import, name='process_import'), ]
        return custom_urls + urls


