from importlib.metadata import requires

from django import forms
from django.forms import widgets

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'mail', 'status', 'content']


#class BookForm(forms.Form):
    #title = forms.CharField(max_length=50, required=True, label='Заголовок')
    #author = forms.CharField(max_length=60, required=True, label='Автор')
    #mail = forms.EmailField(required=True, label='Почта')
    #STATUS_CHOICES = [
    #    ('active', 'Активно'),
    #    ('blocked', 'Заблокировано'),
    #]
    #status = forms.ChoiceField(choices=STATUS_CHOICES, required=True, label='Статус')
    #content = forms.CharField(max_length=5000, widget=widgets.Textarea, required=True, label='Контент')

