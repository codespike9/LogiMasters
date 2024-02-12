from django.db import models

# Create your models here.

class Notifications(models.Model):

    message=models.CharField(max_length=100)
    license_no=models.CharField(max_length=20)
    seen=models.BooleanField(default=False)


    class Meta:
        verbose_name_plural="Notifications"