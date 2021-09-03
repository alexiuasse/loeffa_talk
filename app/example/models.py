from django.db import models
from django.utils.translation import gettext as _


class Example(models.Model):
    name = models.CharField(
        verbose_name=_("Name"),
        max_length=255
    )
    value = models.DecimalField(
        verbose_name=_("Value"),
        max_digits=10,
        decimal_places=2,
        blank=True,
        null=True,
    )
    email = models.EmailField(
        verbose_name=_("E-mail"),
    )
    date = models.DateField(
        _("Date"),
        auto_now=False,
        auto_now_add=False
    )
    time = models.TimeField(
        _("Time"),
        auto_now=False,
        auto_now_add=False
    )
    date_time = models.DateTimeField(
        _("Date Time"),
        auto_now=False,
        auto_now_add=False
    )
    observation = models.TextField(
        verbose_name=_("Observation"),
        blank=True
    )
    father_example = models.ForeignKey(
        'self',
        verbose_name=_("Father"),
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        help_text=_("Luke i'm your father!")
    )

    def __str__(self):
        return str(self.name)
