from django import forms
from django.core.exceptions import ValidationError


class MultipleFileInput(forms.ClearableFileInput):
    allow_multiple_selected = True


class MultipleFileField(forms.FileField):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault("widget", MultipleFileInput())
        super().__init__(*args, **kwargs)

    def clean(self, data, initial=None):
        single_file_clean = super().clean
        if isinstance(data, (list, tuple)):
            result = [single_file_clean(d, initial) for d in data]
        else:
            result = single_file_clean(data, initial)

        return result


class ContratoCreateForm(forms.Form):
    images = MultipleFileField()

    def clean(self):
        files = self.cleaned_data["images"]
        for documento in files:
            file_extension = documento.name.split('.')[-1].lower()
            if not file_extension in ['jpg', 'jpeg', 'png', 'gif', 'pdf']:
                raise ValidationError('Ao menos um documento dos enviados possui o formato inválido, os formatos aceitos: jpg, jpeg, png, gif, pdf')

        return self.cleaned_data
