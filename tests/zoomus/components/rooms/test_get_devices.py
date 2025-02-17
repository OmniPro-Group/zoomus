import unittest

from zoomus import components, util
import responses


def suite():
    """Define all the tests of the module."""
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(GetDevicesV2TestCase))
    return suite


class GetDevicesV2TestCase(unittest.TestCase):
    def setUp(self):
        self.component = components.room.RoomComponentV2(
            base_uri="http://foo.com",
            config={
                "token": "token",
                "version": util.API_VERSION_2,
            },
        )

    @responses.activate
    def test_can_get_devices(self):
        responses.add(responses.GET, "http://foo.com/rooms/42/devices")
        self.component.get_devices(id="42")

    def test_requires_room_id(self):
        with self.assertRaisesRegex(ValueError, "'id' must be set"):
            self.component.get()


if __name__ == "__main__":
    unittest.main()
