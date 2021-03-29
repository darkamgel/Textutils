from django.db import models

# Create your models here.

class Contact(models.Model):
    sno=models.AutoField(primary_key = True)
    name=models.CharField(max_length=255)
    phone=models.CharField(max_length=13)
    content=models.TextField()
    email=models.CharField(max_length=30)
    timeStamp=models.DateTimeField(auto_now_add=True , blank=True)
    
    def __str__(self):
        return 'Message by ' + self.name + ' - ' + self.email