from django.shortcuts import render, get_object_or_404, redirect
from blog.models import Article, Category, Message, Like
from django.core.paginator import Paginator
from .forms import ContactUsForm, MessageForm

# Create your views here.


def article_detail(request, slug):
    article = get_object_or_404(Article, slug=slug)
    if request.user.is_authenticated:
        if request.user.likes.filter(article__slug=slug, user_id=request.user.id).exists():
            is_liked = True
        else:
            is_liked = False
    else:
        return render(request, 'blog/article-details.html', context={'article': article})

    return render(request, 'blog/article-details.html', context={'article': article, 'is_liked': is_liked})


def article_list(request):
    article_list = Article.objects.all()
    page_number = request.GET.get('page')
    paginator = Paginator(article_list, 1)
    page_list = paginator.get_page(page_number)
    return render(request, 'blog/article_list.html', context={'article_list': page_list})


def category_detail(request, pk):
    categories = get_object_or_404(Category, pk=pk)
    articles = categories.article_set.all()
    return render(request, 'blog/article_list.html', context={'article_list': articles})


def search(request):
    q = request.GET.get('q')
    articles = Article.objects.filter(Title__icontains=q)
    page_number = request.GET.get('page')
    paginator = Paginator(articles, 1)
    page_list = paginator.get_page(page_number)
    return render(request, 'blog/article_list.html', {'article_list': page_list})


def contact_us(request):
    if request.method == 'POST':
        form = MessageForm(data=request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            text = form.cleaned_data['text']
            email = form.cleaned_data['email']
            Message.objects.create(name=name, text=text, email=email)

    else:
        form = MessageForm()
    return render(request, 'blog/contact.html', {'form': form})


def like(request, slug, pk):
    if request.user.is_authenticated:
        try:
            like = Like.objects.get(article__slug=slug, user_id=request.user.id)
            like.delete()
        except:
            Like.objects.create(article_id=pk, user_id=request.user.id)

        return redirect("blog:article_detail", slug)
    else:
        return redirect("blog:article_detail", slug)



def about(request):
    return render(request, 'blog/about.html',)

