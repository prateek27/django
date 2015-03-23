from django import forms
from rango.models import Page,Category

class CategoryForm(forms.ModelForm):
	name = forms.CharField(max_length=128)
	views = forms.IntegerField(widget=forms.HiddenInput(),initial=0)
	likes = forms.IntegerField(widget=forms.HiddenInput(),initial=0)

	class Meta:
		model = Category
		fields = ('name',)


class PageForm(forms.ModelForm):
	title = forms.CharField(max_length=100)
	url = forms.URLField()
	views = forms.IntegerField(widget=forms.HiddenInput(),initial
	=0)
	likes = forms.IntegerField(widget=forms.HiddenInput(),initial=0)

	class Meta:
		model = Page
		fields=('title','url','views')

