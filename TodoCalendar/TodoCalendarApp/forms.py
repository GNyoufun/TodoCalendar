from django import forms
from . import models

class Todo(forms.ModelForm):
    class Meta:
        model = models.Todo
        fields = ["taskName", "taskDescription", "dueDate", "label"]
        exclude = ["openDate", "owner", "completed"]

    # name = forms.CharField()
    # taskDescription = forms.Textarea()
    # dueDate = forms.DateTimeField(
    #     widget=forms.DateTimeInput(format='%d/%m/%Y %H:%M:%S')
    # )
        
    

    label = forms.ModelMultipleChoiceField(
        queryset=models.Labels.objects.all(),
        # widget=forms.ModelMultipleChoiceField,
        widget=forms.CheckboxSelectMultiple
    )
