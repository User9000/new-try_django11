from django import forms
from .models import RestaurantLocation


class RestaurantCreateForm(forms.Form):
    name        =    forms.CharField()
    location    =    forms.CharField(required = False)
    category    =    forms.CharField(required = False)

    #clean_ functions are called when form.is_valid() is invoked
    def clean_name(self):
        name = self.cleaned_data.get("name")
        if name == 'Hello':
            raise forms.ValidationError("Error")
        return name


class RestaurantLocationCreateForm(forms.ModelForm):
    class Meta:
            model = RestaurantLocation
            fields = [
                'name',
                'location',
                'category'
            ]
