from django import forms
from django.utils.translation import gettext_lazy as _

from .models import Article

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ('subject', 'body')
        
        labels = {
            'subject': _('タイトル'),
            'body':_('本文'),
        }
        widgets = {
            'subject': forms.TextInput(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'})
        }
