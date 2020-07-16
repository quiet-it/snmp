from django.db import models
from django.utils import timezone

# Create your models here.
class Hosts(models.Model):
    host_location = models.CharField(max_length=100)
    host_ip = models.CharField(max_length=100)
    host_type = models.CharField(max_length=100)
    host_name = models.CharField(max_length=100)
    host_active = models.BooleanField()


class Host_status(models.Model):
    Host_status = models.CharField(max_length=100)
    host_last_check = models.DateTimeFiels(default=timezone.now)
    # host_last_time_active = models.DateTimeFiels(default=timezone.now)

class Old_hosts(model.Model):
    host_name = models.CharField(max_length=100)
    host_location = models.CharField(max_length=100)
    host_ip = models.CharField(max_length=100)
    host_type = models.CharField(max_length=100)
    # host_active = models.BooleanField()
