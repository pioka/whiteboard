from django import forms
from django.utils.translation import gettext_lazy as _

from .models import Article, Board

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


class BoardForm(forms.ModelForm):
    class Meta:
        model = Board
        fields = {'name'}
        labels = {'name': _('名前')}
        widgets = {'name': forms.TextInput(attrs={'class': 'form-control'})}