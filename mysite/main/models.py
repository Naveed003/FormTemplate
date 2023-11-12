from django.db import models

# Create your models here.

class admin(models.Model):
    emplid=models.IntegerField()
    pwd=models.CharField(max_length=255)

    def __str__(self):
        return self.pwd


class contracts(models.Model):
    name=models.CharField(max_length=255)
    file=models.FileField(upload_to='',max_length=255,null=True,default=True)
    url=models.URLField()
    formid=models.CharField(max_length=255,null=True,default=True)