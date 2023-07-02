from django.db import models
from ckeditor.fields import RichTextField
    



class BLog(models.Model):
    title = models.CharField(max_length=255)
    content =RichTextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    thumbnail = models.ImageField(upload_to='')

    def __str__(self):
        return self.title
