from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class Article(models.Model):
   # STATUS_CHOICES = ( ('draft', 'Draft'), ('published', 'Published'),)
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique_for_date = 'created')
    author = models.ForeignKey(User, on_delete = models.CASCADE, related_name = 'articles')
    body = models.TextField()
    created = models.DateTimeField(auto_now_add = True)
    #publish = models.DateTimeField(default = timezone.now)
    updated = models.DateTimeField(auto_now = True)
    #status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')

    class Meta :
        ordering = ('-updated',)
    def __str__ (self):
        return self.title
    
    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('article-detail', kwargs={'year':self.created.year, 'month':self.created.month, 'day':self.created.day, 'post':self.slug})



