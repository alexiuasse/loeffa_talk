from django import forms
from django.utils.translation import gettext as _

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Row, Field, Fieldset, Submit, Button
from crispy_forms.bootstrap import PrependedText, AppendedText, FormActions

from .models import Example


class AdminExampleForm(forms.ModelForm):

    class Meta:
        model = Example
        exclude = []

    def clean_value(self):
        value = self.cleaned_data['value']
        if value is not None and value < 0:
            raise forms.ValidationError(
                _("Value must be positive!"),
                code="invalid"
            )


class SimpleExampleForm(forms.ModelForm):
    prefix = "simpleExampleForm"

    class Meta:
        model = Example
        exclude = []
        widgets = {
            'date': forms.TextInput(attrs={'type': 'date'}),
            'time': forms.TextInput(attrs={'type': 'time'}),
            'observation': forms.Textarea(attrs={'rows': '3'}),
        }

    def clean_value(self):
        value = self.cleaned_data['value']
        if value is not None and value < 0:
            raise forms.ValidationError(
                _("Value must be positive!"),
                code="invalid"
            )


class AdminCrispyExampleForm(forms.ModelForm):
    prefix = "adminCrispyExampleForm"

    layout = Layout(
        Field('name'),
        PrependedText('value', 'R$'),
        AppendedText('email', '@'),
        Field('date_time'),
        Field('father_example'),
        Field('date'),
        Field('time'),
        Field('observation'),
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False  # False to remove <form></form>
        self.helper.layout = self.layout
        self.helper.form_class = 'form-control'

    class Meta:
        model = Example
        exclude = []
        widgets = {
            # 'date': forms.TextInput(attrs={'type': 'date'}),
            # 'time': forms.TextInput(attrs={'type': 'time'}),
            'observation': forms.Textarea(attrs={'rows': '3'}),
        }

    def clean_value(self):
        value = self.cleaned_data['value']
        if value is not None and value < 0:
            raise forms.ValidationError(
                _("Value must be positive!"),
                code="invalid"
            )


class CrispyExampleForm(forms.ModelForm):
    prefix = "crispyExampleForm"

    layout = Layout(
        Field('name'),
        PrependedText('value', 'R$'),
        AppendedText('email', '@'),
        Field('date_time'),
        Field('father_example'),
        Row(
            Field('date', wrapper_class="col-md-6 col-sm-12"),
            Field('time', wrapper_class="col-md-6 col-sm-12"),
        ),
        Field('observation'),
        FormActions(
            Submit('submit', 'Submit'),
            Button('cancel', 'Cancel', css_class='btn-danger'),
        ),
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = True  # False to remove <form></form>
        self.helper.layout = self.layout
        self.helper.form_class = 'form-control'

    class Meta:
        model = Example
        exclude = []
        widgets = {
            'date': forms.TextInput(attrs={'type': 'date'}),
            'time': forms.TextInput(attrs={'type': 'time'}),
            'observation': forms.Textarea(attrs={'rows': '3'}),
        }

    def clean_value(self):
        value = self.cleaned_data['value']
        if value is not None and value < 0:
            raise forms.ValidationError(
                _("Value must be positive!"),
                code="invalid"
            )
