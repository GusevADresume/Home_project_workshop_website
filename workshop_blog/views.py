from django.shortcuts import render
from django.core.paginator import Paginator
from workshop_blog.models import Article
from workshop_blog.blog_writer import BolgWriter


def blog_view(request):
    page_num = int(request.GET.get("page", 1))
    template = 'workshop_blog/workshop_blog.html'
    articles = Article.objects.all().order_by('-datetime')
    pagi = Paginator(articles,1)
    page = pagi.get_page(page_num)
    photos = articles[page_num-1].photos.all()
    print(articles)
    context = {
        'page':page,
        'photos':photos
    }
    return render(request,template,context)


