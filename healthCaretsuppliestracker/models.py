from django.db import models

# Create your models here.


class Donor(models.Model):
    name = models.CharField(max_length=30, default='no name')
    email = models.EmailField(max_length=60, default=0)
    phone_number = models.IntegerField(default=0)
    location = models.CharField(max_length=60, default='no location')

class Hospital(models.Model):
    name = models.CharField(max_length=30, default='no name')
    email = models.EmailField(max_length=60, default=0)
    phone_number = models.IntegerField(default=0)
    location = models.CharField(max_length=60, default='no location')

class Status(models.Model):
    status=models.CharField(max_length=10, default='no status')
    def __str__(self):
        return self.status

class Item(models.Model):
    item_name=models.CharField(max_length=30, default='no data')
    quantity=models.IntegerField( default=0)
    description=models.TextField(max_length=255, default='no data')
    order_status=models.ForeignKey(Status, max_length=10, default='no status', on_delete=models.CASCADE)
    donor=models.ForeignKey(Donor, max_length=10, default=1, on_delete=models.CASCADE)
    hospital=models.ForeignKey(Hospital, max_length=10, default=0, on_delete=models.CASCADE)