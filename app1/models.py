from django.db import models

# Create your models here.
class Tweet(models.Model):
    parent_tweet_id = models.SmallIntegerField( null = True)
    name = models.CharField(max_length=100)
    text = models.CharField(max_length=200)
    image_path = models.CharField(max_length=100, null = True)
    created_at = models.DateField(auto_now_add = True)

    def __str__(self):
        return self.name