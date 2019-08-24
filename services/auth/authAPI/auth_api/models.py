from django.db import models

class Auth(models.Model):
    email = models.EmailField(blank=False, null=False)
    password = models.CharField(max_length=128)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.email
