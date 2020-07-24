from django.contrib.auth import get_user_model
from django.db import models
from django.utils.text import slugify

USER = get_user_model()


class Author(models.Model):
    name = models.OneToOneField(USER, on_delete=models.CASCADE)
    bio = models.CharField(max_length=120, blank=True)
    created_at = models.DateField(auto_now=False, auto_now_add=True)
    thumbnail = models.ImageField(blank=True, null=True)

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=80)
    slug = models.SlugField(unique=True, null=True, blank=True, max_length=90, editable=False)
    description = models.TextField(blank=False)
    image = models.ImageField(upload_to='articles/%Y/%m/%d/', null=True, blank=True)
    created_at = models.DateField(auto_now=False, auto_now_add=True)
    updated_at = models.DateField(auto_now_add=True, auto_now=False)
    email = models.ForeignKey(USER, on_delete=models.CASCADE)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    class Meta:
        ordering = ['-updated_at']

    def __str__(self):
        return self.title

    def _get_unique_slug(self):
        slug = slugify(self.title)
        unique_slug = slug
        num = 1
        while Post.objects.filter(slug=unique_slug).exists():
            unique_slug = '{}-{}'.format(slug, num)
            num += 1
        return unique_slug

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = self._get_unique_slug()
        super().save(*args, **kwargs)
