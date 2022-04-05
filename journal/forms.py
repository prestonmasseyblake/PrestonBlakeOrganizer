from django import forms
from journal.models import JournalEntry, JournalCategory

class JournalEntryForm(forms.ModelForm):
	description = forms.CharField(widget=forms.TextInput(attrs={'size': '80'}))
	category = forms.ModelChoiceField(queryset=JournalCategory.objects.all())
	entry = forms.CharField(widget=forms.Textarea(
		attrs={'rows': '8', 'cols': '80'}))

	class Meta():
		model = JournalEntry
		fields = ('description', 'entry', 'category')
