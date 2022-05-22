from django import forms
from .models import Material


class EntryModelForm(forms.ModelForm):
    class Meta:
        model = Material
        fields = (
            'id',
            'description',
            'trademark',
            'stock',
            'system',
            'value',
            'position',
            'owner',
            'safety_stock',
            'status'
        )


class SearchModelForm(forms.Form):
    id = forms.CharField()
    description = forms.CharField()



