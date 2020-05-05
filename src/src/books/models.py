from django.db import models
from django.urls import reverse

LOCATIONS = (
    ('a', 'A'),
    ('b', 'B'),
    ('c', 'C'),
    ('d', 'D'),
    ('e', 'E'),
    ('f', 'F'),
    ('g', 'G'),
)


class Book(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    author = models.CharField(max_length=100)
    published_year = models.CharField(max_length=4, default=2000)
    image = models.ImageField(upload_to="book/images")
    location = models.CharField(max_length=2, choices=LOCATIONS, default='a')

    def get_absolute_url(self):
        return reverse("book-detail", kwargs={"id": self.id})

    def __str__(self):
        return self.name
