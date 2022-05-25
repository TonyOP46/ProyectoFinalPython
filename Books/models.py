from django.db import models
from core.models import User
# Create your models here.

class books(models.Model):

    BOOKS_CHOICES =[
        ("C", "CIENCIAS"),
        ("M", "MATEMATICAS"),
        ("B", "BIOLOGIA")
    ]

    TYPE_CHOICES =[
        ("A", "ACTUAL"),
        ("V", "VIEJO")
    ]

    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    libro = models.CharField(
        choices=BOOKS_CHOICES, max_length=1
    )
    type = models.CharField(
        choices=TYPE_CHOICES, max_length=1
    )
    plate = models.CharField(max_length=6)
    color = models.CharField(max_length=25)


    def __str__(self) -> str:
        return f"{self.plate} | {self.libro} | {self.owner.email}"
