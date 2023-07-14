import unittest

from zoomus import components, util
import responses


def suite():
    """Define all the tests of the module."""
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(GetRegistrationsReportV2TestCase))
    return suite


class GetRegistrationsReportV2TestCase(unittest.TestCase):
    def setUp(self):
        self.component = components.events.EventsComponentV2(
            base_uri="http://foo.com",
            config={
                "api_key": "KEY",
                "api_secret": "SECRET",
                "version": util.API_VERSION_2,
            },
        )

    @responses.activate
    def test_can_get_event_registrations(self):
        responses.add(responses.GET, "http://foo.com/zoom_events/events/1/reports/ticket_registration")
        self.component.event_registrations(event_id=1)

    def test_requires_id(self):
        with self.assertRaisesRegex(ValueError, "'event_id' must be set"):
            self.component.event_registrations(id=1)

if __name__ == "__main__":
    unittest.main()
