from django.contrib.auth import get_user_model
from django.test import TestCase

from redactors_tracking.models import Topic, Redactor, Newspaper


class ModelTest(TestCase):
    def test_topic_str(self):
        topic = Topic.objects.create(name="test_name")
        self.assertEqual(str(topic), f"{topic.name}")

    def test_redactor_str(self):
        username = "test"
        first_name = "test_first"
        last_name = "last_name"
        license = "AAA12345"
        password = "password"
        redactor = get_user_model().objects.create_user(
            username=username,
            first_name=first_name,
            last_name=last_name,
            license=license,
            password=password,
        )
        self.assertEqual(redactor.username, username)
        self.assertEqual(redactor.first_name, first_name)
        self.assertEqual(redactor.last_name, last_name)
        self.assertEqual(redactor.license, license)
        self.assertTrue(redactor.check_password(password))

    def test_newspaper_str(self):
        topic = Topic.objects.create(name="test_name")
        newspaper = Newspaper.objects.create(title="test_title",
                                             topic=topic)
        self.assertEqual(
            str(newspaper),
            f"{newspaper.title} {newspaper.topic.name}")
