from django.db import models 
from django.contrib.auth.models import AbstractBaseUser

from django.conf import settings

class User(AbstractBaseUser):
    email = models.EmailField(
        verbose_name="email address",
        max_length=255,
        unique=True, # a primary key
    )
    is_active = models.BooleanField(default=True)
    # is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    
    USERNAME_FIELD = "email"

    def __str__(self):
        return self.email
    
    def has_perm(self, perm, obj=None):
        return self.is_staff




# User created label for todo items 
class Labels(models.Model):
    labels = models.CharField(max_length=30)

    def __str__(self):
        return self.labels

# DB for the todo items
class Todo(models.Model):
    taskName = models.CharField(max_length=30)
    taskDescription = models.TextField()
    openDate = models.DateTimeField(auto_now_add=True)
    dueDate = models.DateTimeField(blank=False, null=False)
    completed = models.BooleanField(default=False)
    owner = models.ManyToManyField(User)
    label = models.ManyToManyField(Labels)

    def __str__(self):
        return self.taskName

