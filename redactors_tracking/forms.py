from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError

from redactors_tracking.models import Newspaper, Redactor


class NewspaperForm(forms.ModelForm):
    publishers = forms.ModelMultipleChoiceField(
        queryset=get_user_model().objects.all(),
        widget=forms.CheckboxSelectMultiple,
    )

    class Meta:
        model = Newspaper
        fields = "__all__"

    def clean_publishers(self):
        publishers = self.cleaned_data["publishers"]
        if len(publishers) > 5:
            raise ValidationError("You cannot select more than 5 publishers.")
        return publishers


class NewspaperSearchForm(forms.Form):
    title = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput(attrs={"placeholder": "Search by title"})
    )


class RedactorSearchForm(forms.Form):
    username = forms.CharField(
        max_length=150,
        required=False,
        label="",
        widget=forms.TextInput(
            attrs={"placeholder": "Search by username"})
    )


class TopicSearchForm(forms.Form):
    name = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput(
            attrs={"placeholder": "Search by name"})
    )


def validate_license(license):
    if len(license) != 8:
        raise ValidationError("Redactor id should consist of 8 characters")
    elif not license[:3].isupper() or not license[:3].isalpha():
        raise ValidationError("First 3 characters should be uppercase letters")
    elif not license[3:].isdigit():
        raise ValidationError("Last 5 characters should be digits")

    return license


class RedactorCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = Redactor
        fields = UserCreationForm.Meta.fields + (
            "license",
            "first_name",
            "last_name",
        )

    def clean_license(self):
        license = self.cleaned_data["license"]
        return validate_license(license)


class RedactorUpdateForm(forms.ModelForm):
    class Meta:
        model = Redactor
        fields = [
            "username",
            "license",
            "first_name",
            "last_name",
        ]

    def clean_license(self):
        license = self.cleaned_data.get("license")
        if license:
            return validate_license(license)
        return license
