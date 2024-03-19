from django.test import TestCase

from redactors_tracking.forms import (RedactorCreationForm,
                                      RedactorSearchForm,
                                      NewspaperSearchForm,
                                      TopicSearchForm)


class FormsTest(TestCase):
    def test_create_redactor_form_with_license_first_name_last_name(self):
        form_data = {
            "username": "test_name",
            "license": "NNN12345",
            "first_name": "test_first",
            "last_name": "test_last",
            "password1": "test_password",
            "password2": "test_password",

        }
        form = RedactorCreationForm(data=form_data)
        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data, form_data)

    def test_create_redactor_form_invalid_len_numbers_license(self):
        form_data = {
            "username": "test_name",
            "license": "NNN1234",
            "first_name": "test_first",
            "last_name": "test_last",
            "password1": "test_password",
            "password2": "test_password",

        }
        form = RedactorCreationForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertNotEquals(form.cleaned_data, form_data)

    def test_create_redactor_form_invalid_letter_license(self):
        form_data = {
            "username": "test_name",
            "license": "aQN12342",
            "first_name": "test_first",
            "last_name": "test_last",
            "password1": "test_password",
            "password2": "test_password",

        }
        form = RedactorCreationForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertNotEquals(form.cleaned_data, form_data)

    def test_create_redactor_form_invalid_len_letters_license(self):
        form_data = {
            "username": "test_name",
            "license": "QW12342",
            "first_name": "test_first",
            "last_name": "test_last",
            "password1": "test_password",
            "password2": "test_password",

        }
        form = RedactorCreationForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertNotEquals(form.cleaned_data, form_data)


class RedactorSearchFormTest(TestCase):

    def test_form_with_valid_data(self):
        form = RedactorSearchForm(data={'username': 'test_username'})
        self.assertTrue(form.is_valid())

    def test_form_with_blank_data(self):
        form = RedactorSearchForm(data={})
        self.assertTrue(form.is_valid())

    def test_form_with_invalid_data(self):
        form = RedactorSearchForm(data={"username": "A" * 151})
        self.assertFalse(form.is_valid())


class NewspaperSearchFormTest(TestCase):

    def test_form_with_valid_data(self):
        form = NewspaperSearchForm(data={"title": "test_title"})
        self.assertTrue(form.is_valid())

    def test_form_with_blank_data(self):
        form = NewspaperSearchForm(data={})
        self.assertTrue(form.is_valid())

    def test_form_with_invalid_data(self):
        form = NewspaperSearchForm(data={"title": "n" * 346})
        self.assertFalse(form.is_valid())


class TopicSearchFormTest(TestCase):

    def test_form_with_valid_data(self):
        form = TopicSearchForm(data={"name": "test_name"})
        self.assertTrue(form.is_valid())

    def test_form_with_blank_data(self):
        form = TopicSearchForm(data={})
        self.assertTrue(form.is_valid())

    def test_form_with_invalid_data(self):
        form = TopicSearchForm(data={"name": "v" * 254})
        self.assertTrue(form.is_valid())
