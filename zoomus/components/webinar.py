"""Zoom.us REST API Python Client -- Webinar component"""

from __future__ import absolute_import

from zoomus import util
from zoomus.components import base


class WebinarComponent(base.BaseComponent):
    """Component dealing with all webinar related matters"""

    def list(self, **kwargs):
        util.require_keys(kwargs, "host_id")
        if kwargs.get("start_time"):
            kwargs["start_time"] = util.date_to_str(kwargs["start_time"])
        return self.post_request("/webinar/list", params=kwargs)

    def upcoming(self, **kwargs):
        util.require_keys(kwargs, "host_id")
        if kwargs.get("start_time"):
            kwargs["start_time"] = util.date_to_str(kwargs["start_time"])
        return self.post_request("/webinar/list/registration", params=kwargs)

    def create(self, **kwargs):
        util.require_keys(kwargs, ["host_id", "topic"])
        if kwargs.get("start_time"):
            kwargs["start_time"] = util.date_to_str(kwargs["start_time"])
        return self.post_request("/webinar/create", params=kwargs)

    def update(self, **kwargs):
        util.require_keys(kwargs, ["id", "host_id"])
        if kwargs.get("start_time"):
            kwargs["start_time"] = util.date_to_str(kwargs["start_time"])
        return self.post_request("/webinar/update", params=kwargs)

    def delete(self, **kwargs):
        util.require_keys(kwargs, ["id", "host_id"])
        return self.post_request("/webinar/delete", params=kwargs)

    def end(self, **kwargs):
        util.require_keys(kwargs, ["id", "host_id"])
        return self.post_request("/webinar/end", params=kwargs)

    def get(self, **kwargs):
        util.require_keys(kwargs, ["id", "host_id"])
        return self.post_request("/webinar/get", params=kwargs)

    def register(self, **kwargs):
        util.require_keys(kwargs, ["id", "email", "first_name", "last_name"])
        if kwargs.get("start_time"):
            kwargs["start_time"] = util.date_to_str(kwargs["start_time"])
        return self.post_request("/webinar/register", params=kwargs)


class WebinarComponentV2(base.BaseComponent):
    """Component dealing with all webinar related matters"""

    def list(self, **kwargs):
        util.require_keys(kwargs, "user_id")
        return self.get_request(
            "/users/{}/webinars".format(kwargs.get("user_id")), params=kwargs
        )

    def create(self, **kwargs):
        util.require_keys(kwargs, "user_id")
        return self.post_request(
            "/users/{}/webinars".format(kwargs.get("user_id")), data=kwargs
        )

    def update(self, **kwargs):
        util.require_keys(kwargs, "id")
        return self.patch_request("/webinars/{}".format(kwargs.get("id")), data=kwargs)

    def delete(self, **kwargs):
        util.require_keys(kwargs, "id")
        return self.delete_request(
            "/webinars/{}".format(kwargs.get("id")), params=kwargs
        )

    def end(self, **kwargs):
        util.require_keys(kwargs, "id")
        return self.put_request(
            "/webinars/{}/status".format(kwargs.get("id")), data={"status": "end"}
        )

    def get(self, **kwargs):
        util.require_keys(kwargs, "id")
        return self.get_request("/webinars/{}".format(kwargs.get("id")), params=kwargs)

    def register(self, **kwargs):
        util.require_keys(kwargs, ["id", "email", "first_name", "last_name"])
        return self.post_request(
            "/webinars/{}/registrants".format(kwargs.get("id")), data=kwargs
        )

    def get_registrants(self, **kwargs):
        util.require_keys(kwargs, "id")
        return self.get_request(
            "/webinars/{}/registrants".format(kwargs.get("id")), params=kwargs
        )

    def get_absentees(self, **kwargs):
        util.require_keys(kwargs, "id")
        return self.get_request(
            "/past_webinars/{}/absentees".format(kwargs.get("id")), params=kwargs
        )

    def add_panelists(self, **kwargs):
        util.require_keys(kwargs, "id")
        return self.post_request(
            "/webinars/{}/panelists".format(kwargs.get("id")), data=kwargs
        )

    def list_panelists(self, **kwargs):
        util.require_keys(kwargs, "id")
        return self.get_request(
            "/webinars/{}/panelists".format(kwargs.get("id")), params=kwargs
        )

    def remove_panelists(self, **kwargs):
        util.require_keys(kwargs, "id")
        return self.delete_request(
            "/webinars/{}/panelists".format(kwargs.get("id")), params=kwargs
        )
    
    def participants_report(self, **kwargs):
        util.require_keys(kwargs, "id")
        url = f'/report/webinars/{}/participants'.format(kwargs.get("id"))
        page_size = 300
        participant_report_response = self.get_request(
            url,
            params={"page_size": page_size}
        )

        if participant_report_response.status_code >= 300:
            self.log.error('Error retrieving webinar participant report')
            raise ParticipantReportException('Error retrieving webinar participant report')

        data = json.loads(participant_report_response.content)
        participants = deepcopy(data["participants"])

        while data["next_page_token"] != "":
            participant_report_response = self.get_request(
                url,
                params={
                    "page_size": page_size,
                    "next_page_token": data["next_page_token"]
                }
            )
            if participant_report_response.status_code >= 300:
                raise ParticipantReportException('Error retrieving webinar participant report')

            data = json.loads(participant_report_response.content)
            participants.extend([w for w in deepcopy(data["participants"])])

        return participants