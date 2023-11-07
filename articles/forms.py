from django import forms
from .models import Ariticle

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Ariticle
        # fields = '__all__'
        exclude = ('user', )
        # fields = ('title', 'content', )