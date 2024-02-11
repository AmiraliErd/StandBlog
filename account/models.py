from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile (models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    fathers_name = models.CharField(max_length=25)
    melli_code = models.CharField(max_length=10)
    image = models.ImageField(upload_to="profiles", null=True, blank=True)

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = 'حساب کاربری'
        verbose_name_plural = 'حساب های کاربری'