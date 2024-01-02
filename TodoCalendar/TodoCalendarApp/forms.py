from django import forms
from . import models

class Todo(forms.ModelForm):
    class Meta:
        model = models.Todo
        fields = ["taskName", "taskDescription", "dueDate", "label"]
        exclude = ["openDate", "owner", "completed"]

    # label = forms.ModelMultipleChoiceField(
    #     queryset=models.Labels.objects.all(),
    #     # widget=forms.ModelMultipleChoiceField,
    #     widget=forms.CheckboxSelectMultiple
    # )
