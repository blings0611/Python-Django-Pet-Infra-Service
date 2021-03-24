from django import forms
from themes.models import Local


class LocalForm(forms.ModelForm):
    class Meta:
        model = Local
        fields = '__all__'
