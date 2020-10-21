from twilio.base import values as values
from twilio.base.instance_context import InstanceContext as InstanceContext
from twilio.base.instance_resource import InstanceResource as InstanceResource
from twilio.base.list_resource import ListResource as ListResource
from twilio.base.page import Page as Page
from twilio.rest.preview.marketplace.available_add_on.available_add_on_extension import AvailableAddOnExtensionList as AvailableAddOnExtensionList
from typing import Any, Optional

class AvailableAddOnList(ListResource):
    def __init__(self, version: Any) -> None: ...
    def stream(self, limit: Optional[Any] = ..., page_size: Optional[Any] = ...): ...
    def list(self, limit: Optional[Any] = ..., page_size: Optional[Any] = ...): ...
    def page(self, page_token: Any = ..., page_number: Any = ..., page_size: Any = ...): ...
    def get_page(self, target_url: Any): ...
    def get(self, sid: Any): ...
    def __call__(self, sid: Any): ...

class AvailableAddOnPage(Page):
    def __init__(self, version: Any, response: Any, solution: Any) -> None: ...
    def get_instance(self, payload: Any): ...

class AvailableAddOnContext(InstanceContext):
    def __init__(self, version: Any, sid: Any) -> None: ...
    def fetch(self): ...
    @property
    def extensions(self): ...

class AvailableAddOnInstance(InstanceResource):
    def __init__(self, version: Any, payload: Any, sid: Optional[Any] = ...) -> None: ...
    @property
    def sid(self): ...
    @property
    def friendly_name(self): ...
    @property
    def description(self): ...
    @property
    def pricing_type(self): ...
    @property
    def configuration_schema(self): ...
    @property
    def url(self): ...
    @property
    def links(self): ...
    def fetch(self): ...
    @property
    def extensions(self): ...
