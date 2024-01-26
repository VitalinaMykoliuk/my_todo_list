from django import forms
from dashboard.models import Note


class AddNoteForm(forms.Form):
    title = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Введите название вашей заметки'}))
    content = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Введите вашу заметку'}))

    class Meta:
        model = Note
        fields = ['title', 'content']