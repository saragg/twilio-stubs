from twilio.base import deserialize as deserialize, values as values
from twilio.base.instance_context import InstanceContext as InstanceContext
from twilio.base.instance_resource import InstanceResource as InstanceResource
from twilio.base.list_resource import ListResource as ListResource
from twilio.base.page import Page as Page
from twilio.rest.proxy.v1.service.session.participant.message_interaction import MessageInteractionList as MessageInteractionList
from typing import Any, Optional

class ParticipantList(ListResource):
    def __init__(self, version: Any, service_sid: Any, session_sid: Any) -> None: ...
    def stream(self, limit: Optional[Any] = ..., page_size: Optional[Any] = ...): ...
    def list(self, limit: Optional[Any] = ..., page_size: Optional[Any] = ...): ...
    def page(self, page_token: Any = ..., page_number: Any = ..., page_size: Any = ...): ...
    def get_page(self, target_url: Any): ...
    def create(self, identifier: Any, friendly_name: Any = ..., proxy_identifier: Any = ..., proxy_identifier_sid: Any = ..., fail_on_participant_conflict: Any = ...): ...
    def get(self, sid: Any): ...
    def __call__(self, sid: Any): ...

class ParticipantPage(Page):
    def __init__(self, version: Any, response: Any, solution: Any) -> None: ...
    def get_instance(self, payload: Any): ...

class ParticipantContext(InstanceContext):
    def __init__(self, version: Any, service_sid: Any, session_sid: Any, sid: Any) -> None: ...
    def fetch(self): ...
    def delete(self): ...
    @property
    def message_interactions(self): ...

class ParticipantInstance(InstanceResource):
    def __init__(self, version: Any, payload: Any, service_sid: Any, session_sid: Any, sid: Optional[Any] = ...) -> None: ...
    @property
    def sid(self): ...
    @property
    def session_sid(self): ...
    @property
    def service_sid(self): ...
    @property
    def account_sid(self): ...
    @property
    def friendly_name(self): ...
    @property
    def identifier(self): ...
    @property
    def proxy_identifier(self): ...
    @property
    def proxy_identifier_sid(self): ...
    @property
    def date_deleted(self): ...
    @property
    def date_created(self): ...
    @property
    def date_updated(self): ...
    @property
    def url(self): ...
    @property
    def links(self): ...
    def fetch(self): ...
    def delete(self): ...
    @property
    def message_interactions(self): ...
