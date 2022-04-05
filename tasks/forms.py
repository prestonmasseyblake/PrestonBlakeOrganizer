from django import forms
from tasks.models import TaskEntry, TaskCategory

class TaskEntryForm(forms.ModelForm):
	description = forms.CharField(widget=forms.TextInput(attrs={'size': '80'}))
	category = forms.ModelChoiceField(queryset=TaskCategory.objects.all())
	completed = forms.BooleanField(required=False)
	class Meta():
		model = TaskEntry
		fields = ('description','category', 'completed')
