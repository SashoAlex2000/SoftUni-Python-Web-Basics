from django import forms
from django.core.exceptions import ValidationError

from final_exam.web.models import Profile, Car


def validate_min_length(value):
    if len(value) < 2:
        raise ValidationError("The username must be a minimum of 2 chars")


class ProfileBaseForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['profile_username', 'profile_email', 'profile_age', 'profile_password']
        widgets = {
            'profile_password': forms.PasswordInput(
            )
        }

        labels = {
            'profile_username': 'Username',
            'profile_email': 'Email',
            'profile_age': 'Age',
            'profile_password': 'Password',

        }


class ProfileCreateForm(ProfileBaseForm):
    pass


class ProfileEditForm(ProfileBaseForm):
    class Meta:
        model = Profile
        fields = '__all__'

        labels = {
            'profile_username': 'Username',
            'profile_email': 'Email',
            'profile_age': 'Age',
            'profile_password': 'Password',
            'profile_first_name': 'First Name',
            'profile_last_name': 'Last Name',
            'profile_picture_url': 'Profile Picture',

        }



class ProfileDeleteForm(ProfileBaseForm):
    def save(self, commit=True):
        if commit:
            Car.objects.all().delete()
            self.instance.delete()

        return self.instance

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__set_hiddden_fields()

    def __set_hiddden_fields(self):

        for _, field in self.fields.items():
            field.widget = forms.HiddenInput()


class CarBaseForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = '__all__'

        labels = {
            'car_type': 'Type',
            'car_model': 'Model',
            'car_year': 'Year',
            'car_image_url': 'Image URL',
            'car_price': 'Price',
        }


class CarCreateForm(CarBaseForm):
    pass


class CarEditForm(CarBaseForm):
    pass


class CarDeleteForm(CarBaseForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__set_disabled_fields()

    def save(self, commit=True):
        if commit:
            self.instance.delete()

        return self.instance

    def __set_disabled_fields(self):
        for _, field in self.fields.items():
            field.required = False
            field.widget.attrs['disabled'] = 'disabled'
