from django import forms


# class ContratoCreateForm(forms.Form):
#     # Adicione um campo para o título do contrato (opcional)
#     # title = forms.CharField(max_length=100, required=False)
#
#     # Adicione um campo para o envio de múltiplos arquivos
#     # images = forms.FileField(widget=forms.FileInput(attrs={'multiple': True}))
#     images = forms.FileField()


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
