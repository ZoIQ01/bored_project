"""Form classes for importing and filtering activities."""

from django import forms

from activities.const import DEFAULT_IMPORT_COUNT, MAX_IMPORT_COUNT


class ImportForm(forms.Form):
    """Collect the number of activities to import."""
    count = forms.IntegerField(
        min_value=1,
        max_value=MAX_IMPORT_COUNT,
        initial=DEFAULT_IMPORT_COUNT,
        label="how many activities to import",
    )


class ActivityFilterForm(forms.Form):
    """Collect optional filter values for the activity list."""
    type = forms.ChoiceField(required=False, choices=[("", "Any")])
    participants = forms.IntegerField(
        required=False,
        min_value=1,
        error_messages={"invalid": "Enter a valid whole number for participants."},
    )
    price = forms.DecimalField(
        required=False,
        min_value=0,
        max_digits=5,
        decimal_places=2,
        error_messages={"invalid": "Enter a valid number for price."},
    )
    accessibility = forms.ChoiceField(required=False, choices=[("", "Any")])
    activity = forms.CharField(required=False, max_length=255)

    def __init__(self, *args, types=None, accessibility=None, **kwargs):
        """Populate dynamic choice fields from available filter values."""
        super().__init__(*args, **kwargs)
        self.fields["type"].choices = [("", "Any")] + [
            (item, item) for item in (types or [])
        ]
        self.fields["accessibility"].choices = [("", "Any")] + [
            (str(item), str(item)) for item in (accessibility or [])
        ]
