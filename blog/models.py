from django.db import models
from django.conf import settings

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    photo = models.URLField()
    def __str__(self):
        return self.user.username
        
class Post(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    categories = models.ManyToManyField('Category', related_name='posts')
    slug = models.SlugField(null=True, unique=True)
    user = models.ForeignKey('Profile', related_name = 'posts' , on_delete=models.CASCADE)
    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('article_detail', kwargs={'slug': self.slug})

class Category(models.Model):
    name = models.CharField(max_length=20)
    def __str__(self):
        return self.name

class Comment(models.Model):
    author = models.CharField(max_length=60)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey('Post', related_name='comments',on_delete=models.CASCADE)
    def __str__(self):
        return self.body
