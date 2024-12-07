from django.db import models

class User(models.Model):
    email = models.EmailField(unique=True)
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.firstname} {self.lastname} <{self.email}>"


class EmailMessage(models.Model):
    subject = models.CharField(max_length=255)
    message = models.TextField()
    recipients = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Email: {self.subject} (to {self.recipients})"
