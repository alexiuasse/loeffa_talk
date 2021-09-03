from django.contrib import admin

from .models import Example
from .forms import SimpleExampleForm


@admin.register(Example)
class ExampleAdmin(admin.ModelAdmin):
    form = SimpleExampleForm
