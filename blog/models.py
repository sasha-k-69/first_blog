from django.db import models
from django.shortcuts import reverse


class Post(models.Model):  # title , text , author , date , status
    STATUS_CHOICES = (
        ('pub', 'Published'),
        ('drf', 'Draft'),
    )

    title = models.CharField(max_length=100)
    text = models.TextField()
    datetime_created = models.DateTimeField(auto_now_add=True)
    datetime_modify = models.DateTimeField(auto_now=True)
    # status : published, draft
    status = models.CharField(choices=STATUS_CHOICES, max_length=6)
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post_detail', args=[self.id])

