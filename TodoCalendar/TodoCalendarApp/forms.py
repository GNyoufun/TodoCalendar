from django import forms
from . import models

class Todo(forms.ModelForm):
    class Meta:
        model = models.Todo
        fields = ["taskName", "taskDescription", "label"]
        exclude = ["openDate", "dueDate", "owner", "completed"]

