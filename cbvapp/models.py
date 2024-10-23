from django.db import models

# Create your models here.
from django.db import models
from django.urls import reverse
class Student(models.Model):
    firstName = models.CharField(max_length=20)
    lastName = models.CharField(max_length=20)
    testScore = models.FloatField()


    def get_absolute_url(self):
        return reverse('student-detail', kwargs={'pk': self.pk})
