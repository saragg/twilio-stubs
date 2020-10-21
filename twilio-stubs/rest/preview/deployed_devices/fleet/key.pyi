from twilio.base import deserialize as deserialize, values as values
from twilio.base.instance_context import InstanceContext as InstanceContext
from twilio.base.instance_resource import InstanceResource as InstanceResource
from twilio.base.list_resource import ListResource as ListResource
from twilio.base.page import Page as Page
from typing import Any, Optional

class KeyList(ListResource):
    def __init__(self, version: Any, fleet_sid: Any) -> None: ...
    def create(self, friendly_name: Any = ..., device_sid: Any = ...): ...
    def stream(self, device_sid: Any = ..., limit: Optional[Any] = ..., page_size: Optional[Any] = ...): ...
    def list(self, device_sid: Any = ..., limit: Optional[Any] = ..., page_size: Optional[Any] = ...): ...
    def page(self, device_sid: Any = ..., page_token: Any = ..., page_number: Any = ..., page_size: Any = ...): ...
    def get_page(self, target_url: Any): ...
    def get(self, sid: Any): ...
    def __call__(self, sid: Any): ...

class KeyPage(Page):
    def __init__(self, version: Any, response: Any, solution: Any) -> None: ...
    def get_instance(self, payload: Any): ...

class KeyContext(InstanceContext):
    def __init__(self, version: Any, fleet_sid: Any, sid: Any) -> None: ...
    def fetch(self): ...
    def delete(self): ...
    def update(self, friendly_name: Any = ..., device_sid: Any = ...): ...

class KeyInstance(InstanceResource):
    def __init__(self, version: Any, payload: Any, fleet_sid: Any, sid: Optional[Any] = ...) -> None: ...
    @property
    def sid(self): ...
    @property
    def url(self): ...
    @property
    def friendly_name(self): ...
    @property
    def fleet_sid(self): ...
    @property
    def account_sid(self): ...
    @property
    def device_sid(self): ...
    @property
    def secret(self): ...
    @property
    def date_created(self): ...
    @property
    def date_updated(self): ...
    def fetch(self): ...
    def delete(self): ...
    def update(self, friendly_name: Any = ..., device_sid: Any = ...): ...
