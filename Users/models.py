from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission

class FleetManagers(AbstractUser):
    CompanyName = models.CharField(max_length=50)


class Fleets(models.Model):
    companyName = models.ForeignKey(FleetManagers, on_delete=models.CASCADE)
    hardware_id = models.CharField(max_length=100, unique=True)
    license_no = models.CharField(max_length=20, unique=True)
    password = models.CharField(max_length=255)
    mobile_no = models.CharField(max_length=10,null=True)

    def __str__(self):
        return self.license_no
    class Meta:
        verbose_name_plural="Fleet"