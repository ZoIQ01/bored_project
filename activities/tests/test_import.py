from unittest.mock import Mock, patch

from django.test import TestCase
from django.urls import reverse

from activities.models import Activity
from activities.services.import_from_api import import_activities


@patch("activities.services.import_from_api.requests.get")
class ImportActivitiesServiceTests(TestCase):
    def make_response(self, key):
        m = Mock()
        m.json.return_value = {
            "key": key,
            "activity": f"Activity {key}",
            "type": "relaxation",
            "participants": 1,
            "accessibility": "0.1",
            "price": "0.0",
            "link": "",
        }
        return m

    def test_import_activities_adds_and_skips(self, mock_get):
        mock_get.side_effect = [
            self.make_response(1),
            self.make_response(2),
            self.make_response(1),
        ]

        added, skipped = import_activities(count=3)

        self.assertEqual(added, 2)
        self.assertEqual(skipped, 1)
        self.assertEqual(Activity.objects.count(), 2)

    def test_import_activities_respects_timeout(self, mock_get):
        mock_get.return_value = self.make_response(1)

        calls = {"n": 0}

        def fake_time_provider():
            calls["n"] += 1
            return calls["n"]

        added, skipped = import_activities(
            count=100, timeout=3, time_provider=fake_time_provider
        )
        self.assertEqual(added, 1)
        self.assertGreater(skipped, 0)


class ImportActivitiesViewTests(TestCase):
    @patch("activities.views.import_view.import_activities")
    def test_import_view_post(self, mock_import):
        mock_import.return_value = (2, 0)

        Activity.objects.create(
            id=1,
            activity="Existing",
            type="relaxation",
            participants=1,
            accessibility="0.1",
            price="0.0",
            link="",
        )

        resp = self.client.post(reverse("import_activities_view"), {"count": 2}, follow=True)

        self.assertEqual(resp.status_code, 200)
        self.assertEqual(len(resp.redirect_chain), 1)
        self.assertEqual(resp.context["added"], 2)
        self.assertEqual(resp.context["skipped"], 0)
        self.assertEqual(resp.context["count"], 2)
        self.assertEqual(resp.context["total"], 1)
        self.assertEqual(Activity.objects.count(), 1)

