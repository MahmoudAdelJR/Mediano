from django.shortcuts import render, get_object_or_404, redirect
from .models import Article
from django.core.paginator import Paginator, EmptyPage, InvalidPage
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def article_list(request):
    articles_list = Article.objects.all()
    p_list = Paginator(articles_list,2)
    try :
        page = int(request.GET.get('page','1'))
    except :
        page = 1
    try :
        articles = p_list.page(page)
    except (EmptyPage, InvalidPage) :
        articles = p_list.page(1)
    index = p_list.page_range.index(articles.number)
    max_index = len(p_list.page_range)
    start_index = index-3 if index >=3 else 0
    end_index = index+3 if index <= max_index-3 else max_index
    page_range = list(p_list.page_range)[start_index:end_index]

    
    return render(request, 'blog/article_list.html', {'articles':articles, 'page_range':page_range})

def article_detail(request, year, month, day, post):
    article = get_object_or_404(Article, slug=post, created__year=year, created__month=month, created__day=day)
    return render(request, 'blog/article_detail.html', {'article':article})

    