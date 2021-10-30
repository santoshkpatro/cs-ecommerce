from django.db import models


class Contact(models.Model):
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=20)
    subject = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.email
