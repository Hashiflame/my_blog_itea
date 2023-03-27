from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    content = models.CharField(max_length=120)
    image = models.ImageField(upload_to='posts')
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.content.split()[0]
