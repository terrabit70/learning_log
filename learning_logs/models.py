from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Topic(models.Model):
    """Topic, wich user learning"""
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.PROTECT)

    def __str__(self):
        return self.text


class Entry(models.Model):
    """Information, which user has learned by the topic"""
    topic = models.ForeignKey(Topic, on_delete=models.PROTECT)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'entries'

    def __str__(self):
        if len(self.text) > 49:
            return self.text[:50] + "..."
        else:
            return self.text
