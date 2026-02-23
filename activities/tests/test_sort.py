from django.test import TestCase
from django.urls import reverse

from activities.models import Activity


class SortActivitiesViewTests(TestCase):
    def test_sort_view_get(self):
        Activity.objects.create(
            id=1,
            activity="A",
            type="relaxation",
            participants=1,
            accessibility="0.1",
            price="0.0",
        )
        Activity.objects.create(
            id=2,
            activity="B",
            type="education",
            participants=2,
            accessibility="0.2",
            price="0.0",
        )

        resp = self.client.get(reverse("activities_list") + "?sort_by=type&order=asc")

        self.assertEqual(resp.status_code, 200)
        self.assertIn("page_obj", resp.context)
        self.assertIn("types", resp.context)

        activities = list(resp.context["page_obj"].object_list)
        self.assertEqual([a.activity for a in activities], ["B", "A"])


class ActivityDetailViewTests(TestCase):
    def test_activity_detail_view_404(self):
        resp = self.client.get(reverse("activity_detail", args=[999]))
        self.assertEqual(resp.status_code, 404)

    def test_activity_detail_view_displays_activity(self):
        a = Activity.objects.create(
            id=100,
            activity="DetailMe",
            type="relaxation",
            participants=1,
            accessibility="0.1",
            price="0.0",
            link="",
        )

        resp = self.client.get(reverse("activity_detail", args=[a.id]))
        self.assertEqual(resp.status_code, 200)
        self.assertIn("activity", resp.context)
        self.assertEqual(resp.context["activity"].id, a.id)
        self.assertContains(resp, "DetailMe")

