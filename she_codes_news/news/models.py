from unicodedata import category
from django.contrib.auth import get_user_model
from django.db import models
from django.utils import timezone

class NewsStory(models.Model):
    title = models.CharField(max_length=200)
    # author = models.CharField(max_length=200)
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE
    )


    pub_date = models.DateTimeField()
    # image_url = models.URLField(default='https://picsum.photos/600')
    content = models.TextField()
    category = models.ForeignKey("news.Category", on_delete=models.CASCADE, null = True, blank = True)
    image=models.URLField(null=True, blank=True)

    class Meta:
        ordering = ['-pub_date']
    
    def __str__ (self):
        return self.title
    
# categories = (
#     ("NEWS", "News"),
#     ("WEATHER", "Weather"),
# )

# category = models.CharField(max_length=200, choices= categories, default="News")


class Category(models.Model):
    name = models.CharField(max_length=50)
    def __str__ (self):
        return self.name 