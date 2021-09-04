from django.shortcuts import render

from .forms import CrispyExampleForm, SimpleExampleForm, CrispyExampleFormset, CrispyExampleFormsetHelper


def test_form(request):
    simple_form = SimpleExampleForm(request.POST or None)
    crispy_form = CrispyExampleForm(request.POST or None)
    crispy_form_set = CrispyExampleFormset()
    crispy_form_set_helper = CrispyExampleFormsetHelper()
    if request.method == "POST":
        if simple_form.is_valid() and crispy_form.is_valid():
            simple_object = simple_form.save()
            crispy_object = crispy_form.save()
            simple_form = SimpleExampleForm(instance=simple_object)
            crispy_form = CrispyExampleForm(instance=crispy_object)
    return render(
        request,
        template_name="test_form.html",
        context={
            'crispy_form': crispy_form,
            'simple_form': simple_form,
            'crispy_form_set': crispy_form_set,
            'crispy_form_set_helper': crispy_form_set_helper,
        }
    )
