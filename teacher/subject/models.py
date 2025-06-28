from django.db import models


class Teacher(models.Model):
    title = models.CharField(max_length=50)
    
    def __str__(self):
      return self.title 


class Subject(models.Model):
    name = models.CharField(max_length=25, unique=True)
    email = models.EmailField()
    Teacher = models.ForeignKey(Teacher, related_name="Subject", on_delete=models.CASCADE, default=None)
    def __str__(self):
        return f"Aty:> {self.name}: Pochtasy:> {self.email}"