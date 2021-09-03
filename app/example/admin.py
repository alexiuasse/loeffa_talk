from django.contrib import admin

from .models import Example
from .forms import AdminExampleForm


@admin.register(Example)
class ExampleAdmin(admin.ModelAdmin):
    form = AdminExampleForm
