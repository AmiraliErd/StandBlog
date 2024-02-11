from blog.models import Article, Category

def recent_posts(request):
    recent_posts = Article.objects.order_by('-Created')
    categories = Category.objects.all()
    return {'recent':recent_posts, 'categories':categories}