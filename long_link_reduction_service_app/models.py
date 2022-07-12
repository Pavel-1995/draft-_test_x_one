from django.contrib.auth.models import User
from django.db import models
from .utils import create_reducer_url
from urllib import request


class Reducer(models.Model):
    time_created = models.DateTimeField(auto_now_add=True)

    origin_url = models.URLField()

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # user = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)

    modified_url = models.CharField(max_length=15, unique=True, blank=True)

    class Meta:
        ordering = ["-time_created"]

    def __str__(self):
        return f"origin- {self.origin_url} and modified- {self.modified_url}"

    def save(self, *args, **kwargs):


        #user_id = request.user
        # If the modified_url wasn't specified
        if not self.modified_url:
            # We pass the model instance that is being saved
            self.modified_url = create_reducer_url(self)

        super().save(*args, **kwargs)
        print(super().save(*args, **kwargs))
