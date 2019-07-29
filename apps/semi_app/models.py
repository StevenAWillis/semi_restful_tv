from __future__ import unicode_literals
from django.db import models

36
class ShowManager(models.Manager):

    def basic_validator(self, postData):
            errors = {}
            # add keys and values to errors dictionary for each invalid field
            if len(postData['title']) < 3:
                print("not long enough")
                errors["title"] = "Show name should be at least 1 character"
            if len(postData['network']) < 1:
                print("not long enough")
                errors["network"] = "Network should be at least 1 character"
            if len(postData['date']) < 1:
                print("no date entered")
                errors["date"] = "Must enter Shows Release Date"            
            if len(postData['description']) < 10:
                print("not long enough")
                errors["description"] = "Blog description should be at least 10 characters"
            return errors

class Show(models.Model):
    title = models.CharField(max_length=45)
    network = models.CharField(max_length=45)
    release_date = models.DateTimeField()
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ShowManager()

