from twilio.base import deserialize as deserialize, values as values
from twilio.base.instance_context import InstanceContext as InstanceContext
from twilio.base.instance_resource import InstanceResource as InstanceResource
from twilio.base.list_resource import ListResource as ListResource
from twilio.base.page import Page as Page
from typing import Any, Optional

class DayList(ListResource):
    def __init__(self, version: Any, resource_type: Any) -> None: ...
    def stream(self, next_token: Any = ..., previous_token: Any = ..., limit: Optional[Any] = ..., page_size: Optional[Any] = ...): ...
    def list(self, next_token: Any = ..., previous_token: Any = ..., limit: Optional[Any] = ..., page_size: Optional[Any] = ...): ...
    def page(self, next_token: Any = ..., previous_token: Any = ..., page_token: Any = ..., page_number: Any = ..., page_size: Any = ...): ...
    def get_page(self, target_url: Any): ...
    def get(self, day: Any): ...
    def __call__(self, day: Any): ...

class DayPage(Page):
    def __init__(self, version: Any, response: Any, solution: Any) -> None: ...
    def get_instance(self, payload: Any): ...

class DayContext(InstanceContext):
    def __init__(self, version: Any, resource_type: Any, day: Any) -> None: ...
    def fetch(self): ...

class DayInstance(InstanceResource):
    def __init__(self, version: Any, payload: Any, resource_type: Any, day: Optional[Any] = ...) -> None: ...
    @property
    def redirect_to(self): ...
    @property
    def day(self): ...
    @property
    def size(self): ...
    @property
    def create_date(self): ...
    @property
    def friendly_name(self): ...
    @property
    def resource_type(self): ...
    def fetch(self): ...
