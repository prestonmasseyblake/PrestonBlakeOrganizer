from django import forms
from budget.models import BudgetEntry, BudgetCategory

class BudgetEntryForm(forms.ModelForm):
	description = forms.CharField(widget=forms.TextInput(attrs={'size': '80'}))
	category = forms.ModelChoiceField(queryset=BudgetCategory.objects.all())
	projected = forms.IntegerField(widget=forms.TextInput(attrs={'size': '10'}))
	actual = forms.IntegerField(widget=forms.TextInput(attrs={'size': '10'}))

	class Meta():
		model = BudgetEntry
		fields = ('description','category', 'projected', 'actual')


