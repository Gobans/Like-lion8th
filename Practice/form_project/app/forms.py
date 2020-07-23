from django import forms
from .models import FirstModel
class Firstform(forms.Form):
    recommend = (
        ('Good','좋아요'),
        ('Bad', '싫어요'),
    )
    title = forms.CharField()
    text = forms.CharField(widget= forms.Textarea)
    choice = forms.ChoiceField(choices= recommend)


class Secondform(forms.ModelForm):
    class Meta:
        model = FirstModel
        fields = ['title','text','recommend']