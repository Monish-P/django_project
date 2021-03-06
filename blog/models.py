from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.
class post(models.Model):
    title=models.CharField(max_length=100)
    content=models.TextField()
    date=models.DateTimeField(auto_now_add=True)
    author=models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('Blog-post_detail', kwargs = {'pk':self.pk})