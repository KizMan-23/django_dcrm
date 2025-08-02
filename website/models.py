from django.db import models

# Create your models here.
class Record(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    phone = models.CharField(max_length=12)
    state = models.CharField(max_length=50)
    city =  models.CharField(max_length=40)
    address = models.CharField(max_length=50)
    zipcode = models.CharField(max_length=15)

    def __str__(self):
        return (f"{self.first_name} {self.last_name}")


