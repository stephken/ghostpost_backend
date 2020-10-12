from django.db import models
from django.utils import timezone
# Create your models here.

class Post(models.Model):
    POST_CHOICE = ((True, "Boast"), (False, "Roast"))

    content = models.CharField(max_length=250)
    up_votes = models.IntegerField(default=0)
    down_votes = models.IntegerField(default=0)
    post_type = models.BooleanField(choices=POST_CHOICE)
    post_date = models.DateTimeField(default=timezone.now)

    @property
    def vote_counter(self):
        return self.up_votes + self.down_votes

