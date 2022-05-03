from django.shortcuts import render
from first_page.models import Article

def first_page_view(request):
    content = Article.objects.all()
    template = 'first_page/pm.html'
    context = {'content':content}
    return render(request,template,context)
