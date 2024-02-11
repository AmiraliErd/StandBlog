from django.shortcuts import render
from blog.models import Article
# Create your views here.

def home(request):
    articles = Article.objects.published()
    recent = Article.objects.all()[3:] # or .order_by('-Created', '-Updated')
    return render(request, 'home_app/index.html', context={'articles': articles})
