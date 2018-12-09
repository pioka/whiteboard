from django import forms
from django.utils.translation import gettext_lazy as _

from .models import Article,Tag

class ArticleForm(forms.ModelForm):
    tag = forms.ModelChoiceField(
        queryset=Tag.objects.none(),
        widget=forms.Select(attrs={'class': 'form-control'}),
        label='タグ',
        empty_label='- 未選択 -',
        required=False
    )
    
    class Meta:
        model = Article
        fields = ('subject', 'body', 'tag')
        
        labels = {
            'subject': _('タイトル'),
            'body':_('本文'),
        }
        widgets = {
            'subject': forms.TextInput(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'})
        }
