from django import forms

from library_past_exam.web.models import Profile, Book


class ProfileBaseForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'


class ProfileCreateForm(ProfileBaseForm):
    pass


class ProfileDeleteForm(ProfileBaseForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__set_disabled_fields()

    def save(self, commit=True):
        if commit:
            self.instance.delete()

        return self.instance

    def __set_disabled_fields(self):
        for _, field in self.fields.items():
            field.widget.attrs['readonly'] = 'readonly'


class ProfileEditForm(ProfileBaseForm):
    pass


class BookBaseForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'


class BookAddForm(BookBaseForm):
    pass


class BookEditForm(BookBaseForm):
    pass
