from django import forms
from .models import Text


class TextForm(forms.ModelForm):
    text = forms.CharField(widget=forms.Textarea)

    class Meta:
        model = Text
        fields = ["text"]
