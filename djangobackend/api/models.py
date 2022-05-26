from django.db import models

class User(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class UserImages(models.Model):
    user = models.ForeignKey(User, default=None, on_delete=models.CASCADE)
    item_id = models.IntegerField()
    img_src = models.CharField(max_length=200,default=None)

    def __str__(self):
        return self.user.name