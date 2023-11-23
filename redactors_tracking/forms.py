from django import forms
from django.contrib.auth import get_user_model

from redactors_tracking.models import Newspaper


class NewspaperForm(forms.ModelForm):
    publishers = forms.ModelMultipleChoiceField(
        queryset=get_user_model().objects.all(),
        widget=forms.CheckboxSelectMultiple,
    )

    class Meta:
        model = Newspaper
        fields = "__all__"


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
