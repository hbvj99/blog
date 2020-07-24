from django.contrib.auth import get_user_model
from django.db import models
from django.utils.text import slugify
from django.core.files.uploadedfile import InMemoryUploadedFile

import sys
from PIL import Image
from io import BytesIO


USER = get_user_model()


def compress_image(img):
    size = 1080, 960
    image_temporary = Image.open(img).convert('RGB')
    output_io_stream = BytesIO()
    image_temporary.thumbnail(size, Image.ANTIALIAS)
    image_temporary.save(output_io_stream, format='JPEG', quality=75)
    output_io_stream.seek(0)
    img = InMemoryUploadedFile(output_io_stream, 'ImageField', "%s.jpg" % img.name.split('.')[0], 'image/jpeg',
                               sys.getsizeof(output_io_stream), None)
    return img


class Post(models.Model):
    title = models.CharField(max_length=80)
    slug = models.SlugField(unique=True, null=True, blank=True, max_length=90, editable=False)
    description = models.TextField(blank=False)
    image = models.ImageField(upload_to='articles/%Y/%m/%d/', null=True, blank=True)
    created_at = models.DateField(auto_now=False, auto_now_add=True)
    updated_at = models.DateField(auto_now_add=True, auto_now=False)
    user = models.ForeignKey(USER, on_delete=models.CASCADE)

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
        if self.image:
            self.image = compress_image(self.image)
        super().save(*args, **kwargs)
