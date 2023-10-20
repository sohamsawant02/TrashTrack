from django.db import models
from zoneinfo import ZoneInfo
from datetime import datetime
import os
# Create your models here.


class trashData(models.Model):
    last_time = models.DateTimeField(null=True)
    dustbin_id= models.CharField(null=True, max_length=10)
    is_sent  = models.BooleanField(blank=False, default=False)
    perc = models.IntegerField(null=True ,max_length=5)

    
    def _str_(self):
        return self.dustbin_id