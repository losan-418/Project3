from django.db import models
from django.contrib.auth.models import User


class UserModel(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_type = models.CharField(blank=False,null=False,max_length=10)


    def __str__(self):
        return "{0} {1}".format(self.user.first_name, self.user.last_name)
# Create your models here.
