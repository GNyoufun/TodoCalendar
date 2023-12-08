from django import forms
from . import models

class Todo(forms.ModelForm):
    class Meta:
        model = models.todo
        exclude = ["openDate"]
        # exclude = ('owner') #! add on after user login 