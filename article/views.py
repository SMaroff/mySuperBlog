from django.contrib import auth
from django.core.context_processors import csrf
from django.http.response import HttpResponse, Http404
from django.shortcuts import render_to_response, redirect
from article.models import Article, Comments
from django.core.exceptions import ObjectDoesNotExist
from forms import CommentForm


#//////////////////////////////////////////////////////////////
def articles(request):
    return render_to_response('articles.html', {'articles': Article.objects.all(), 'username': auth.get_user(request).username})

def article(request, article_id=1):
    comment_form = CommentForm
    args = {}
    args.update(csrf(request))
    args['article'] = Article.objects.get(id=article_id)
    args['comments'] = Comments.objects.filter(comments_article_id=article_id)
    args['form'] = comment_form
    args['username'] = auth.get_user(request).username
    return render_to_response('article.html', args)


def addlike(request, article_id):
    try:
        article = Article.objects.get(id=article_id)
        article.article_likes +=1
        article.save()
    except ObjectDoesNotExist:
        raise Http404
    return redirect("/articles/get/%s/" % article_id)

def addcom(request, article_id):
    if request.POST and ('pause' not in request.session):
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.comments_article= Article.objects.get(id=article_id)
            form.save()
            request.session.set_expiry(60)
            request.session['pause'] = True
    return redirect("/articles/get/%s/" % article_id)

def about(request):
    return render_to_response('About.html')