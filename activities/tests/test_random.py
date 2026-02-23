from django.test import TestCase
from django.urls import reverse

from activities.models import Activity
from activities.services.get_rdm_activity import get_random_activity


class GetRandomActivityTests(TestCase):
    def test_get_random_activity_none(self):
        self.assertIsNone(get_random_activity())

    def test_get_random_activity_returns_activity(self):
        a1 = Activity.objects.create(
            id=10,
            activity="X",
            type="relaxation",
            participants=1,
            accessibility="0.1",
            price="0.0",
        )
        a2 = Activity.objects.create(
            id=11,
            activity="Y",
            type="education",
            participants=2,
            accessibility="0.2",
            price="0.0",
        )

        got = get_random_activity()
        self.assertIn(got, [a1, a2])

    def test_get_random_activity_with_queryset(self):
        Activity.objects.create(
            id=20,
            activity="Z",
            type="relaxation",
            participants=1,
            accessibility="0.1",
            price="0.0",
        )
        Activity.objects.create(
            id=21,
            activity="W",
            type="education",
            participants=2,
            accessibility="0.2",
            price="0.0",
        )

        got = get_random_activity(Activity.objects.filter(type="relaxation"))
        self.assertIsNotNone(got)
        self.assertEqual(got.type, "relaxation")


class RandomActivityViewTests(TestCase):
    def test_random_activity_view_empty_db(self):
        response = self.client.get(reverse("random_activity"))

        self.assertEqual(response.status_code, 200)
        self.assertIn("no_activities", response.context)
        self.assertTrue(response.context["no_activities"])

    def test_random_activity_view_returns_activity_context(self):
        Activity.objects.create(
            id=30,
            activity="Stretch",
            type="relaxation",
            participants=1,
            accessibility="0.1",
            price="0.0",
        )

        response = self.client.get(reverse("random_activity"))

        self.assertEqual(response.status_code, 200)
        self.assertIn("activity", response.context)
        self.assertEqual(response.context["activity"].id, 30)

