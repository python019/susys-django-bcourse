from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    slug = models.SlugField(max_length=50)
    image = models.ImageField(upload_to="images/", default="images/default.jpg")

    def __str__(self):
        return self.slug
