from django import forms
from .models import Post

class quoteForm(forms.ModelForm):
	class Meta:
		model = Post
		fields = ['title', 'body', 'author']

