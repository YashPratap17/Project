from django.db import models

class User(models.Model):
    username = models.CharField(max_length=50,unique=True)
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    dob = models.DateField()

    def __str__(self):
        return f"{self.username}-{self.name}"

class Posts(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField(max_length=5000)
    pub_date = models.DateTimeField("date published")
    modified_date = models.DateTimeField("date modified")
    
    def __str__(self):
        return f"{self.title} - {self.user}"