from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User)
    bio = models.CharField(max_length=500,blank=True)
    total_score = models.IntegerField(blank=True)

    def __str__(self):
        return "%s %s" %(self.id,self.user)