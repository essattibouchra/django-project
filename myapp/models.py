from django.db import models
from django.apps import AppConfig

class Client(models.Model):
    class Meta:
        app_label = 'myapp'
    full_name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    cin = models.CharField(max_length=20)

    def __str__(self):
        return self.full_name
    
class MyAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'myapp'   

