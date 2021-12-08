from django.db import models

# Create your models here.
class Bookmark(models.Model):
    site_name = models.TextField(max_length=200)
    url = models.URLField("Site URL")
    published = models.BooleanField(default=False)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    # __str__ method
    def __str__(self) -> str:
        return "name : " + self.site_name + ", adress : " + self.url