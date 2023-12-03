from django.contrib.auth import get_user_model
from django.test import TestCase, Client
from django.urls import reverse


class AdminSiteTest(TestCase):
    def setUp(self) -> None:
        self.client = Client()
        self.admin_user = get_user_model().objects.create_superuser(
            username="admin_name",
            password="admin_password",
        )
        self.client.force_login(self.admin_user)
        self.redactor = get_user_model().objects.create_user(
            username="test_name",
            password="test_password",
            license="QLT12345",
        )

    def test_license_display_on_admin_page(self):
        url = reverse("admin:redactors_tracking_redactor_changelist")
        response = self.client.get(url)
        self.assertContains(response, self.redactor.license)

    def test_license_display_on_admin_detail_page(self):
        url = reverse(
            "admin:redactors_tracking_redactor_change",
            args=[self.redactor.id]
        )
        response = self.client.get(url)
        self.assertContains(response, self.redactor.license)

    def test_license_display_on_admin_add_page(self):
        url = reverse("admin:redactors_tracking_redactor_add")
        response = self.client.get(url)
        self.assertContains(response, "license")
        self.assertTrue(response, self.redactor.license)
