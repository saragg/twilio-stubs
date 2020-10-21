from twilio.base import deserialize as deserialize, values as values
from twilio.base.instance_context import InstanceContext as InstanceContext
from twilio.base.instance_resource import InstanceResource as InstanceResource
from twilio.base.list_resource import ListResource as ListResource
from twilio.base.page import Page as Page
from typing import Any, Optional

class EventTypeList(ListResource):
    def __init__(self, version: Any) -> None: ...
    def stream(self, limit: Optional[Any] = ..., page_size: Optional[Any] = ...): ...
    def list(self, limit: Optional[Any] = ..., page_size: Optional[Any] = ...): ...
    def page(self, page_token: Any = ..., page_number: Any = ..., page_size: Any = ...): ...
    def get_page(self, target_url: Any): ...
    def get(self, type: Any): ...
    def __call__(self, type: Any): ...

class EventTypePage(Page):
    def __init__(self, version: Any, response: Any, solution: Any) -> None: ...
    def get_instance(self, payload: Any): ...

class EventTypeContext(InstanceContext):
    def __init__(self, version: Any, type: Any) -> None: ...
    def fetch(self): ...

class EventTypeInstance(InstanceResource):
    def __init__(self, version: Any, payload: Any, type: Optional[Any] = ...) -> None: ...
    @property
    def type(self): ...
    @property
    def schema_id(self): ...
    @property
    def date_created(self): ...
    @property
    def date_updated(self): ...
    @property
    def description(self): ...
    @property
    def url(self): ...
    @property
    def links(self): ...
    def fetch(self): ...
