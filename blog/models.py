from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.utils.text import slugify

# Create your models here.


class Category(models.Model):
    Title = models.CharField(max_length=50)
    Created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.Title

    class Meta:
        verbose_name = 'دسته بندی'
        verbose_name_plural = 'دسته بندی ها'


class ArticleManager(models.Manager):
    def counter(self):
        return len(self.all())

    def published(self):
        return self.filter(published=True)


class Article(models.Model):
    Author = models.ForeignKey(User, on_delete=models.CASCADE)
    Title = models.CharField(max_length=70,)
    category = models.ManyToManyField(Category)
    Body = models.TextField()
    Image = models.ImageField(upload_to='articles')
    Created = models.DateTimeField(auto_now_add=True)
    Updated = models.DateTimeField(auto_now=True)
    pub_date = models.DateField(default=timezone.now)
    published = models.BooleanField(default=True)
    objects = ArticleManager()
    slug = models.SlugField(null=True, blank=True, unique=True)

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        self.slug = slugify(self.Title)
        super(Article, self).save()

    def __str__(self):
        return f"{self.Title} - {self.Body[:30]}"

    class Meta:
        ordering = ('-Created',)
        verbose_name = 'مقاله'
        verbose_name_plural = 'مقالات'



class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    parents = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='replies')
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.body[:30]

    class Meta:
        verbose_name = 'کامنت'
        verbose_name_plural = 'کامنت ها'


class Message(models.Model):
    name = models.CharField(max_length=50)
    text = models.TextField()
    email = models.EmailField()
    age = models.IntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'پیام'
        verbose_name_plural = 'پیام ها'


class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='likes', verbose_name='کاربر')
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='likes', verbose_name='مقاله')
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.article.Title}"

    class Meta:
        verbose_name = 'لایک'
        verbose_name_plural = 'لایک ها'
        ordering = ('-created',)
