import os
import random
import string
from django.db import models
from django.contrib.auth.models import User
from PIL import Image
import uuid

def get_save_path(instance, filename):
    _, ext = os.path.splitext(filename)
    return 'profile_pics/' + uuid.uuid4().hex + ext

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to=get_save_path)

    def __str__(self) -> str:
        return f'{self.user.username} Profile'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.image.path)

        if(img.height > 300 or img.width > 300):
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)