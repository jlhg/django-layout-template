from django.db import models
from django.utils import timezone


class PostMessage(models.Model):
    name = models.CharField(max_length=15)
    message = models.TextField()
    upload_file = models.TextField()
    post_date = models.DateTimeField(default=timezone.now)

    class Meta:
        app_label = 'example_app'
