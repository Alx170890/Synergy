from django import forms

class PlaceholderForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super(PlaceholderForm, self).__init__(*args, **kwargs)
        for _, field in self.fields.items():
            field.widget.attrs['placeholder'] = "Длинный URL"
class ShortUrlForm(PlaceholderForm):
    url = forms.URLField(label="")