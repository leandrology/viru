from django.db import models
from datetime import datetime

# Create your models here.
class Response(models.Model):
    intent = models.CharField(max_length=100, default='intent name', primary_key=True, verbose_name='Intent')
    message = models.CharField(max_length=1000, default = 'your message', verbose_name='User Message')
    response = models.CharField(max_length=1000, default='new response', verbose_name='AI Response')
    createdate = models.DateTimeField(default=datetime.now, blank=True, verbose_name='Created Date')
    status = models.CharField(max_length=100, choices=[('Waiting for Approval', 'Waiting for Approval'), ('On Hold', 'On Hold'), ('Approved', 'Approved'), ('Rejected', 'Rejected')], default='W')

    def __str__(self):
        return self.intent
