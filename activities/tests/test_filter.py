from django.test import TestCase
from django.urls import reverse

from activities.models import Activity


class FilterActivitiesViewTests(TestCase):
    def test_filter_activities_filters_by_type_and_participants(self):
        Activity.objects.create(
            id=12345,
            activity="Go for a walk",
            type="recreational",
            participants=1,
            price="0.0",
            accessibility="0.1",
            link="",
        )
        Activity.objects.create(
            id=12346,
            activity="Read a book",
            type="education",
            participants=1,
            price="0.0",
            accessibility="0.1",
            link="",
        )

        url = reverse("activities_list") + "?type=recreational&participants=1"
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Go for a walk")

    def test_filter_activities_invalid_price_shows_error(self):
        Activity.objects.create(
            id=20001,
            activity="Read docs",
            type="education",
            participants=1,
            price="0.10",
            accessibility="0.10",
            link="",
        )

        url = reverse("activities_list") + "?price=abc"
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Enter a valid number for price.")

    def test_filter_activities_invalid_participants_shows_error(self):
        Activity.objects.create(
            id=20002,
            activity="Practice guitar",
            type="education",
            participants=1,
            price="0.10",
            accessibility="0.10",
            link="",
        )

        url = reverse("activities_list") + "?participants=abc"
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Enter a valid whole number for participants.")

    def test_filter_activities_filters_by_accessibility(self):
        Activity.objects.create(
            id=30001,
            activity="Accessible one",
            type="education",
            participants=1,
            price="0.0",
            accessibility="0.1",
            link="",
        )
        Activity.objects.create(
            id=30002,
            activity="Accessible two",
            type="education",
            participants=1,
            price="0.0",
            accessibility="0.9",
            link="",
        )

        url = reverse("activities_list") + "?accessibility=0.1"
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Accessible one")
        self.assertNotContains(response, "Accessible two")

