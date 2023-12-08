from django.db import models

from django.conf import settings

class Labels(models.Model):
    labels = models.CharField(max_length=30)

class todo(models.Model):
    taskName = models.CharField(max_length=30)
    taskDescription = models.TextField()
    openDate = models.DateTimeField(auto_now_add=True)
    dueDate = models.DateTimeField(blank=False, null=False)
    completed = models.BooleanField(default=False)
    # owner = models.ForeignKey(User, on_delete=models.CASCADE) #! will add in later day
    label = models.ManyToManyField(Labels)


