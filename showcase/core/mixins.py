from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django import forms

class FormHelperMixin(forms.Form):
    """Universal mixin for all forms with Crispy Forms."""
    submit_text = "Submit"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = "post"
        self.helper.add_input(Submit("submit", self.submit_text))