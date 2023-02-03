from django.db import models

# Create your models here.
class Member(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()
    phone = models.CharField(max_length=12)
    admin = models.BooleanField(default=False)

    # returns the full name of the Member
    def __str__(self):
        return self.first_name + " " + self.last_name