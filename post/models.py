from django.db import models

# Create your models here.

class Student(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    age = models.IntegerField()
    # create_at = models.DateTimeField(auto_now_add=True)
    # update_at = models.DateTimeField(auto_now=True)

def __str__(self):
    return f'Name: {self.first_name} {self.last_name}. Email: {self.email}. Age: {self.age}' \

class Course(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    student = models.ManyToManyField(Student)
    student = models.ForeignKey(Student, on_delete=models.CASCADE, blank=True, null=True)
def __str__(self):
    return f'Name: {self.name}. Desc: {self.descripition}. Student: {self.student}'
