from twilio.base import deserialize as deserialize, values as values
from twilio.base.instance_context import InstanceContext as InstanceContext
from twilio.base.instance_resource import InstanceResource as InstanceResource
from twilio.base.list_resource import ListResource as ListResource
from twilio.base.page import Page as Page
from typing import Any, Optional

class PublishedTrackList(ListResource):
    def __init__(self, version: Any, room_sid: Any, participant_sid: Any) -> None: ...
    def stream(self, limit: Optional[Any] = ..., page_size: Optional[Any] = ...): ...
    def list(self, limit: Optional[Any] = ..., page_size: Optional[Any] = ...): ...
    def page(self, page_token: Any = ..., page_number: Any = ..., page_size: Any = ...): ...
    def get_page(self, target_url: Any): ...
    def get(self, sid: Any): ...
    def __call__(self, sid: Any): ...

class PublishedTrackPage(Page):
    def __init__(self, version: Any, response: Any, solution: Any) -> None: ...
    def get_instance(self, payload: Any): ...

class PublishedTrackContext(InstanceContext):
    def __init__(self, version: Any, room_sid: Any, participant_sid: Any, sid: Any) -> None: ...
    def fetch(self): ...

class PublishedTrackInstance(InstanceResource):
    class Kind:
        AUDIO: str = ...
        VIDEO: str = ...
        DATA: str = ...
    def __init__(self, version: Any, payload: Any, room_sid: Any, participant_sid: Any, sid: Optional[Any] = ...) -> None: ...
    @property
    def sid(self): ...
    @property
    def participant_sid(self): ...
    @property
    def room_sid(self): ...
    @property
    def name(self): ...
    @property
    def date_created(self): ...
    @property
    def date_updated(self): ...
    @property
    def enabled(self): ...
    @property
    def kind(self): ...
    @property
    def url(self): ...
    def fetch(self): ...
