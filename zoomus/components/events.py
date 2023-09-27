"""Zoom.us REST API Python Client -- Events component"""

from __future__ import absolute_import

from zoomus import util
from zoomus.components import base


class EventsComponentV2(base.BaseComponent):
    """Component dealing with all zoom events related matters"""

    #
    # Events
    #

    def list_events(self, **kwargs):
        """
        List events
        GET /zoom_events/events
        Use this API to retrieve all events associated with the user.
        """
        return self.get_request(
            "/zoom_events/events",
            params=kwargs
        )

    def create_event(self, **kwargs):
        """
        Create an event
        POST /zoom_events/events
        Use this API to create an event.
        """
        return self.post_request(
            "/zoom_events/events",
            data=kwargs
        )

    def get_event(self, **kwargs):
        """
        Get an event
        GET /zoom_events/events/{eventId}
        Use this API to get information on a specified event.
        """
        util.require_keys(kwargs, "event_id")

        event_id = kwargs.get("event_id")

        return self.get_request(
            f"/zoom_events/events/{event_id}",
            params=kwargs
        )

    def delete_event(self, **kwargs):
        """
        Delete an event
        DELETE /zoom_events/events/{eventId}
        Use this API to delete an event.
        """
        util.require_keys(kwargs, "event_id")

        event_id = kwargs.get("event_id")

        return self.delete_request(
            f"/zoom_events/events/{event_id}",
            params=kwargs
        )

    def update_event(self, **kwargs):
        """
        Update an event
        PATCH /zoom_events/events/{eventId}
        Use this API to update an event.
        """
        util.require_keys(kwargs, "event_id")

        event_id = kwargs.get("event_id")

        return self.patch_request(
            f"/zoom_events/events/{event_id}",
            data=kwargs
        )

    #
    # Hubs
    #

    def list_hubs(self, **kwargs):
        """
        List hubs
        GET /zoom_events/hubs
        Use this API to retrieve event hubs.
        """
        util.require_keys(kwargs, "role_type")
        return self.get_request(
            "/zoom_events/hubs",
            params=kwargs
        )

    #
    # Registrants
    #

    def list_session_attendees(self, **kwargs):
        """
        List session attendees
        GET /zoom_events/events/{eventId}/sessions/{sessionId}/attendees
        Use this API to retrieve session attendees.
        """
        util.require_keys(kwargs, ["event_id", "session_id"])

        event_id = kwargs.get("event_id")
        session_id = kwargs.get("session_id")
        return self.get_request(
            f"/zoom_events/events/{event_id}/sessions/{session_id}/attendees",
            params=kwargs
        )

    def list_registrants(self, **kwargs):
        """
        List registrants
        GET /zoom_events/events/{eventId}/registrants
        Use this API to retrieve event registrants.
        """
        util.require_keys(kwargs, "event_id")

        event_id = kwargs.get("event_id")
        return self.get_request(
            f"/zoom_events/events/{event_id}/registrants",
            params=kwargs
        )

    #
    # Sessions
    #

    def list_sessions(self, **kwargs):
        """
        List sessions
        GET /zoom_events/events/{eventId}/sessions
        Use this API to retrieve sessions in an event.
        """
        util.require_keys(kwargs, "event_id")

        event_id = kwargs.get("event_id")

        return self.get_request(
            f"/zoom_events/events/{event_id}/sessions",
            params=kwargs
        )

    def create_session(self, **kwargs):
        """
        Create a session
        POST /zoom_events/events/{eventId}/sessions
        Use this API to create a session.
        """
        util.require_keys(kwargs, "event_id")

        event_id = kwargs.get("event_id")
        return self.post_request(
            f"/zoom_events/events/{event_id}/sessions",
            data=kwargs
        )

    def get_session(self, **kwargs):
        """
        Get the session information
        GET /zoom_events/events/{eventId}/sessions/{sessionId}
        Use this API to get the session information.
        """
        util.require_keys(kwargs, ["event_id", "session_id"])

        event_id = kwargs.get("event_id")
        session_id = kwargs.get("session_id")

        return self.get_request(
            f"/zoom_events/events/{event_id}/sessions/{session_id}",
            params=kwargs
        )

    def delete_session(self, **kwargs):
        """
        Delete a session
        DELETE /zoom_events/events/{eventId}/sessions/{sessionId}
        Use this API to delete a session.
        """
        util.require_keys(kwargs, ["event_id", "session_id"])

        event_id = kwargs.get("event_id")
        session_id = kwargs.get("session_id")

        return self.delete_request(
            f"/zoom_events/events/{event_id}/sessions/{session_id}",
            params=kwargs
        )

    def update_session(self, **kwargs):
        """
        Update a session
        PATCH /zoom_events/events/{eventId}/sessions/{sessionId}
        Use this API to update an existing session in an event.
        """
        util.require_keys(kwargs, ["event_id", "session_id"])

        event_id = kwargs.get("event_id")
        session_id = kwargs.get("session_id")

        return self.patch_request(
            f"/zoom_events/events/{event_id}/sessions/{session_id}",
            data=kwargs
        )

    def get_ticket_session_join_token(self, **kwargs):
        """
        Get ticket session join token by Event ID and Session ID
        GET /zoom_events/events/{eventId}/sessions/{sessionId}/join_token
        Retrieves the join token to join an event session.
        """
        util.require_keys(kwargs, ["event_id", "session_id"])

        event_id = kwargs.get("event_id")
        session_id = kwargs.get("session_id")

        return self.get_request(
            f"/zoom_events/events/{event_id}/sessions/{session_id}/join_token",
            params=kwargs
        )

    def list_session_interpreters(self, **kwargs):
        """
        List session interpreters
        GET /zoom_events/events/{eventId}/sessions/{sessionId}/interpreters
        Use this API to retrieve interpreters in a session.
        """
        pass

    def upsert_session_interpreters(self, **kwargs):
        """
        Create or update session interpreters.
        PUT /zoom_events/events/{eventId}/sessions/{sessionId}/interpreters
        Use this API to create or update the list of interpreters for the session.
        """
        pass

    def list_session_polls(self, **kwargs):
        """
        List session polls
        GET /zoom_events/events/{eventId}/sessions/{sessionId}/polls
        List all the polls of a session.
        """
        pass

    def upsert_session_polls(self, **kwargs):
        """
        Create or update session polls.
        PUT /zoom_events/events/{eventId}/sessions/{sessionId}/polls
        Use this API to create or update the list of polls for the session.
        """
        pass

    #
    # Ticket Types
    #
    def list_ticket_types(self, **kwargs):
        """
        List ticket types
        GET /zoom_events/events/{eventId}/ticket_types
        Use this API to retrieve all ticket types associated with an event.
        """
        util.require_keys(kwargs, "event_id")

        event_id = kwargs.get("event_id")

        return self.get_request(
            f"/zoom_events/events/{event_id}/ticket_types",
            params=kwargs
        )

    def create_ticket_type(self, **kwargs):
        """
        Create an event ticket type
        POST /zoom_events/events/{eventId}/ticket_types
        Use this API to create create a ticket type for the event ID.
        """
        util.require_keys(kwargs, "event_id")

        event_id = kwargs.get("event_id")
        return self.post_request(
            f"/zoom_events/events/{event_id}/ticket_types",
            data=kwargs
        )

    def delete_ticket_type(self, **kwargs):
        """
        Delete a ticket type
        DELETE /zoom_events/events/{eventId}/ticket_types/{ticketTypeId}
        Use this API to delete a ticket type of an event.
        """
        util.require_keys(kwargs, ["event_id", "ticket_type_id"])

        event_id = kwargs.get("event_id")
        ticket_type_id = kwargs.get("ticket_type_id")

        return self.delete_request(
            f"/zoom_events/events/{event_id}/ticket_types/{ticket_type_id}",
            params=kwargs
        )

    def update_ticket_type(self, **kwargs):
        """
        Update ticket type for an event
        PATCH /zoom_events/events/{eventId}/ticket_types/{ticketTypeId}
        Use this API to update the ticket type for an event ID.
        """
        util.require_keys(kwargs, ["event_id", "ticket_type_id"])

        event_id = kwargs.get("event_id")
        ticket_type_id = kwargs.get("ticket_type_id")

        return self.patch_request(
            f"/zoom_events/events/{event_id}/ticket_types/{ticket_type_id}",
            data=kwargs
        )

    def list_registration_questions(self, **kwargs):
        """
        List registration questions for an event
        GET /zoom_events/events/{eventId}/questions
        Use this API to list registration questions and fields that are to be answered by users while registering
        for an event. These questions are setup at event level.
        """
        pass

    def update_registration_questions(self, **kwargs):
        """
        Update registration questions for an event
        PUT /zoom_events/events/{eventId}/questions
        Use this API to update registration questions and fields that are to be answered by users while registering
        for an event. These questions are setup at event level.
        """
        pass

    def list_registration_questions_ticket_type(self, **kwargs):
        """
        List registration questions for ticket type
        GET /zoom_events/events/{eventId}/ticket_types/{ticketTypeId}/questions
        Use this API to list registration questions and fields that are to be answered by users while registering for
        an event. These questions are setup at ticket_type level.
        """
        pass

    def update_registration_questions_ticket_type(self, **kwargs):
        """
        Update registration questions for ticket type
        PUT /zoom_events/events/{eventId}/ticket_types/{ticketTypeId}/questions
        Use this API to update registration questions and fields that are to be answered by users while registering
        for an event. These questions are setup at ticket_type level.
        """
        pass

    #
    # Tickets
    #
    def list_tickets(self, **kwargs):
        """
        List tickets
        GET /zoom_events/events/{eventId}/tickets
        Use this API to retrieve the ticket information of an event.
        """
        util.require_keys(kwargs, "event_id")

        event_id = kwargs.get("event_id")

        return self.get_request(
            f"/zoom_events/events/{event_id}/tickets",
            params=kwargs
        )

    def create_ticket(self, **kwargs):
        """
        Create tickets
        POST /zoom_events/events/{eventId}/tickets
        Use this API to create tickets for an event. You can add a single ticket or up to 30 tickets in a batch
        operation. Please note that this request uses the pre-registration flow.
        """
        util.require_keys(kwargs, "event_id")

        event_id = kwargs.get("event_id")

        return self.post_request(
            f"/zoom_events/events/{event_id}/tickets",
            params=kwargs,
            data=kwargs
        )

    def get_ticket(self, **kwargs):
        """
        Get a ticket
        GET /zoom_events/events/{eventId}/tickets/{ticketId}
        Use this API to get information on a specific ticket.
        """
        util.require_keys(kwargs, ["event_id", "ticket_id"])

        event_id = kwargs.get("event_id")
        ticket_id = kwargs.get("ticket_id")

        return self.get_request(
            f"/zoom_events/events/{event_id}/tickets/{ticket_id}",
            params=kwargs
        )

    def delete_ticket(self, **kwargs):
        """
        Delete a ticket
        DELETE /zoom_events/events/{eventId}/tickets/{ticketId}
        Use this API to delete a ticket.
        """
        util.require_keys(kwargs, ["event_id", "ticket_id"])

        event_id = kwargs.get("event_id")
        ticket_id = kwargs.get("ticket_id")

        return self.delete_request(
            f"/zoom_events/events/{event_id}/tickets/{ticket_id}",
            params=kwargs
        )

    #
    # Event Reports
    #
    def event_attendance(self, **kwargs):
        """
        Get event attendance report
        GET /zoom_events/events/{eventId}/reports/event_attendance
        Use this API to retrieve the attendance report of an event.
        """
        util.require_keys(kwargs, "event_id")
        event_id = kwargs.get("event_id")
        return self.get_request(
            f"/zoom_events/events/{event_id}/reports/event_attendance",
            params=kwargs
        )

    def event_registrations(self, **kwargs):
        """
        Get event registrations report
        GET /zoom_events/events/{eventId}/reports/ticket_registration
        Use this API to retrieve the registrations report of an event.
        """
        util.require_keys(kwargs, "event_id")
        event_id = kwargs.get("event_id")
        return self.get_request(
            f"/zoom_events/events/{event_id}/reports/ticket_registration",
            params=kwargs
        )
