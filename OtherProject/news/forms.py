from .models import Artiles
from django.forms import ModelForm, TextInput, Textarea, DateTimeInput

class ArtilesForm(ModelForm):
    class Meta:
        model = Artiles
        fields = ['title', 'anons', 'full_text', 'data']

        widgets = {
            'title': TextInput(attrs={
                'placeholder': "Название статьи",
                'class': "form-control"
            }),
            'anons': TextInput(attrs={
                'placeholder': "Анонс статьи",
                'class': "form-control"
            }),
            'full_text': Textarea(attrs={
                'placeholder': "Текст статьи",
                'class': "form-control"
            }),
            'data': DateTimeInput(attrs={
                'placeholder': "Дата публикации",
                'class': "form-control"
            })
        }