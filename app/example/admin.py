from django.contrib import admin

from .models import Example
from .forms import AdminExampleForm, AdminCrispyExampleForm


@admin.register(Example)
class ExampleAdmin(admin.ModelAdmin):
    form = AdminExampleForm
    # form = AdminCrispyExampleForm
    # add_form_template = "admin/example_form.html"
