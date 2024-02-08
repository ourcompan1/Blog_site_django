from django.shortcuts import render, redirect
from .models import *
from django.http import Http404, HttpResponseNotFound


def index_page(request):
    article = Article.objects.all()
    return render(request, 'index.html', {'articles': article, 'page': 'index'})


def about_page(request):
    return render(request, "about.html", {'page': 'about'})


def contact_page(request):
    if request.method == 'GET':
        return render(request, 'contact.html', {'page': 'contact'})
    else:
        print(request.POST)
        return redirect(contact_page)


def article_page(request, article_id):
    article = Article.objects.filter(id=article_id).first()
    if article:
        comments = Comment.objects.filter(article=article).all()
        return render(request, 'article.html', {'article': article, 'comments': comments})
    return Http404('article not found')


def commentpost(request, article_id):
    if request.method == 'POST':
        article = Article.objects.filter(id=article_id).first()
        if 'name' in request.POST and 'email' in request.POST and 'message' in request.POST:
            article.new_comment(request.POST)
            return redirect(article_page, article_id)
    return HttpResponseNotFound()
