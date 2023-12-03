from django.contrib.auth import get_user_model
from django.test import TestCase, Client
from django.urls import reverse

from redactors_tracking.models import Newspaper, Redactor, Topic

TOPIC_URL = reverse("redactors_tracking:topic-list")
REDACTOR_URL = reverse("redactors_tracking:redactor-list")
NEWSPAPER_URL = reverse("redactors_tracking:newspaper-list")


class PublicTopicTest(TestCase):
    def test_login_required(self):
        response = self.client.get(TOPIC_URL)
        self.assertNotEquals(response.status_code, 200)


class PrivateTopicTest(TestCase):
    def setUp(self) -> None:
        self.user = get_user_model().objects.create(
            username="test_name",
            license="VVV12345",
            password="test_password"
        )
        self.client.force_login(self.user)

    def test_retrieve_topic(self):
        Topic.objects.create(name="test_name")
        response = self.client.get(TOPIC_URL)
        self.assertEqual(response.status_code, 200)
        topic = Topic.objects.all()
        self.assertEqual(list(response.context["topic_list"]),
                         list(topic))
        self.assertTemplateUsed(response, "redactors_tracking/topic_list.html")


class PublicRedactorTest(TestCase):
    def test_login_required(self):
        response = self.client.get(REDACTOR_URL)
        self.assertNotEquals(response.status_code, 200)


class PublicNewspaperTest(TestCase):
    def test_login_required(self):
        response = self.client.get(NEWSPAPER_URL)
        self.assertNotEquals(response.status_code, 200)


class PrivateNewspaperTest(TestCase):
    def setUp(self) -> None:
        self.user = get_user_model().objects.create(
            username="test_name",
            license="VVV12345",
            password="test_password"
        )
        self.client.force_login(self.user)

    def test_retrieve_newspaper(self):
        topic = Topic.objects.create(name="test_name")
        Newspaper.objects.create(title="test_title",
                                 topic=topic)
        response = self.client.get(NEWSPAPER_URL)
        self.assertEqual(response.status_code, 200)
        newspapers = Newspaper.objects.all()
        self.assertEqual(list(response.context["newspaper_list"]),
                         list(newspapers))
        self.assertTemplateUsed(response,
                                "redactors_tracking/newspaper_list.html")
