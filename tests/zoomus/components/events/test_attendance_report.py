import unittest

from zoomus import components, util
import responses


def suite():
    """Define all the tests of the module."""
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(GetAttendanceReportV2TestCase))
    return suite


class GetAttendanceReportV2TestCase(unittest.TestCase):
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
    def test_can_get_event_attendance(self):
        responses.add(responses.GET, "http://foo.com/zoom_events/events/1/reports/event_attendance")
        self.component.event_attendance(event_id=1)

    def test_requires_id(self):
        with self.assertRaisesRegex(ValueError, "'event_id' must be set"):
            self.component.event_attendance(id=1)

if __name__ == "__main__":
    unittest.main()
