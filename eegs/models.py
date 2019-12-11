from django.db import models

# Create your models here.


class Patient(models.Model):

    id = models.IntegerField(
        primary_key=True
    )
    state = models.CharField(
        max_length=64,
        null=False
    )

    def __str__(self):
       return f"{self.id} - {self.state}"


class Trial(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='trials')


class Channel(models.Model):
    label = models.CharField(
        max_length=64,
        null=False
    )
    values = models.TextField(
        null=False
    )
    trial = models.ForeignKey(Trial, on_delete=models.CASCADE, related_name='channels')
  