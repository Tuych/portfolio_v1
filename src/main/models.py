from django.db import models


class Projects(models.Model):
    title = models.CharField(max_length=30)
    image = models.ImageField(upload_to='main/images')
    url = models.URLField(blank=True)
    date = models.DateField()

    def __str__(self):
        return self.title
