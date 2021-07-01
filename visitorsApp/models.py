from django.core.validators import RegexValidator
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
# Create your models here.

class VisitInfo(models.Model):
    daytime = models.DateTimeField()
    vname = models.CharField(max_length=20)
    address = models.CharField(max_length=100)
    purpose = models.CharField(max_length=20)
    whom = models.CharField(max_length=20)
    department = models.CharField(max_length=20)
    mobile1 = models.CharField(max_length=11)
    #mobile2 = models.CharField(max_length=5, default='null')

    class Meta:
        db_table = 'VisitInfo'

    def __str__(self):
        return self.vname;

class MeetingInfo(models.Model):
    daytime = models.DateTimeField()
    depart = models.CharField(max_length=20)
    organiser = models.CharField(max_length=20)
    summary = models.CharField(max_length=100)
    purpose = models.CharField(max_length=50)
    attendee = models.CharField(max_length=200)
    feedback = models.CharField(max_length=70)


    class Meta:
        db_table = 'MeetingInfo'

    def __str__(self):
        return self.depart;