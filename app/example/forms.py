from django import forms
from django.forms.widgets import TextInput
from django.utils.translation import gettext as _

from django.forms.models import modelformset_factory
from crispy_forms.helper import FormHelper
from crispy_forms.layout import HTML, Layout, Row, Field, Submit, Button
from crispy_forms.bootstrap import PrependedText, AppendedText, FormActions
from django_select2 import forms as s2forms

from .models import Example


class FatherExampleWidget(s2forms.ModelSelect2Widget):
    search_fields = [
        "name__icontains",
    ]


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
            'father_example': FatherExampleWidget(attrs={'data-width': '100%'}),
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
            'father_example': FatherExampleWidget(attrs={'data-width': '100%'}),
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
        HTML("<p class='text-danger'> Usuário {{ request.user }} </p>"),
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
            'father_example': FatherExampleWidget(attrs={'data-width': '100%'}),
        }

    def clean_value(self):
        value = self.cleaned_data['value']
        if value is not None and value < 0:
            raise forms.ValidationError(
                _("Value must be positive!"),
                code="invalid"
            )


CrispyExampleFormset = modelformset_factory(Example, extra=0, exclude=[])


class CrispyExampleFormsetHelper(FormHelper):

    layout = Layout(
        Field('name'),
        PrependedText('value', 'R$'),
        AppendedText('email', '@'),
        Field('date_time'),
        Field('father_example'),
        Field('date'),
        Field('time'),
        Field('observation', rows=2),
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.form_method = "post"
        self.form_class = "form-control"
        self.layout = self.layout
