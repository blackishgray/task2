from django import forms
from .models import PostModel 

class PostForm(forms.ModelForm):
	class Meta:
		model = PostModel 
		fields = ['content']
		widgets = {
			'content': forms.TextInput(attrs={'id':'content', 'class':'form-control'}),
		}