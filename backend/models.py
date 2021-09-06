from django.db import models
from django.urls import reverse

class Post(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    slug = models.SlugField(max_length=50)
    image = models.ImageField(upload_to="images/", default="images/default.jpg")

    def get_absolute_url(self):
        return reverse("blog:single", args=[self.slug])

    def __str__(self):
        return self.slug
