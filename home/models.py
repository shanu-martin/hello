from django.db import models

# Create your models here......
class Contact(models.Model):
    name=models.CharField(max_length=70)
    email=models.CharField(max_length=122)
    complaint=models.TextField()
    
    def __str__(self):
        return self.name