from django import forms
from .models import RestaurantLocation
from .validators import validate_category

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
    category = forms.CharField(required = False,validators= [validate_category])
    class Meta:
            model = RestaurantLocation
            fields = [
                'name',
                'location',
                'category'
            ]
    def clean_name(self):
        name = self.cleaned_data.get("name")
        if name == 'Hello':
            raise forms.ValidationError("Error")
        return name
    
    def clean_email(self):
        name = self.cleaned_data.get("name")
        if name == 'Hello':
            raise forms.ValidationError("Error")
        return name

