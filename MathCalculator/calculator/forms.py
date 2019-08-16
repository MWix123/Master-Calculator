from django import forms
from .models import Post

class MathForm(forms.ModelForm):
	class Meta:
		model = Post
		fields = ('textarea',)
		#fields = ('text','textarea')	
		#fields = ('textarea',) 

class DerivativeForm(forms.ModelForm):
	class Meta:
		model = Post
		fields = ('textarea','text')
		#fields = ('text','textarea')	
