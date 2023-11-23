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
            raise ValidationError('You cannot select more than 5 publishers.')
        return publishers


class NewspaperSearchForm(forms.Form):
    title = forms.CharField(max_length=255,
                            required=False,
                            label="",
                            widget=forms.TextInput(
                                attrs={"placeholder": "Search by title"})
                            )


class RedactorSearchForm(forms.Form):
    username = forms.CharField(max_length=150,
                               required=False,
                               label="",
                               widget=forms.TextInput(
                                   attrs={"placeholder": "Search by username"})
                               )


class TopicSearchForm(forms.Form):
    name = forms.CharField(max_length=255,
                           required=False,
                           label="",
                           widget=forms.TextInput(
                               attrs={"placeholder": "Search by name"})
                           )


def validate_redactor_id(redactor_id):
    if len(redactor_id) != 8:
        raise ValidationError("Redactor id should consist of 8 characters")
    elif not redactor_id[:3].isupper() or not redactor_id[:3].isalpha():
        raise ValidationError("First 3 characters should be uppercase letters")
    elif not redactor_id[3:].isdigit():
        raise ValidationError("Last 5 characters should be digits")

    return redactor_id


class RedactorCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = Redactor
        fields = UserCreationForm.Meta.fields + (
            "redactor_id",
            "first_name",
            "last_name",
        )

    def clean_redactor_id(self):
        redactor_id = self.cleaned_data["redactor_id"]
        return validate_redactor_id(redactor_id)


class RedactorUpdateForm(forms.ModelForm):
    class Meta:
        model = Redactor
        fields = [
            "username",
            "redactor_id",
            "first_name",
            "last_name",
        ]

    def clean_redactor_id(self):
        redactor_id = self.cleaned_data.get("redactor_id")
        if redactor_id:
            return validate_redactor_id(redactor_id)
        return redactor_id
