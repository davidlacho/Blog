from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from django.core.validators import MinLengthValidator


class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email_address = models.EmailField()

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return self.full_name()


class Tag(models.Model):
    caption = models.CharField(max_length=20)

    def __str__(self):
        return self.caption


class Post(models.Model):
    title = models.CharField(max_length=200)
    excerpt = models.CharField(max_length=200)
    image_name = models.CharField(max_length=100)
    content = models.TextField(validators=[MinLengthValidator(10)])
    date = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(
        Author, on_delete=models.SET_NULL, null=True, related_name="posts"
    )
    tags = models.ManyToManyField(Tag, related_name="posts")
    slug = models.SlugField(unique=True, db_index=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("post-detail-page", args=[str(self.slug)])

    def save(self, *args, **kwargs):
        self.slug = self.slug or slugify(self.title)
        super().save(*args, **kwargs)

    @property
    def url(self):
        return self.get_absolute_url()
