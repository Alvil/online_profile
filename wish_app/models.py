from django.db import models
# Create your models here.


class Wish(models.Model):
    wisher = models.CharField(max_length=50)
    wish = models.CharField(max_length=100)
    wish_check = models.CharField(max_length=100, blank=True, null=True)
    instances = models.IntegerField(default=1)

    def __str__(self):
        return str(self.wish)

    def save(self, *args, **kwargs):
        self.wish_check = self.wish.lower()
        super(Wish, self).save(*args, **kwargs)
