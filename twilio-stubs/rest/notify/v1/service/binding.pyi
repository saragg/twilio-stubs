from twilio.base import deserialize as deserialize, serialize as serialize, values as values
from twilio.base.instance_context import InstanceContext as InstanceContext
from twilio.base.instance_resource import InstanceResource as InstanceResource
from twilio.base.list_resource import ListResource as ListResource
from twilio.base.page import Page as Page
from typing import Any, Optional

class BindingList(ListResource):
    def __init__(self, version: Any, service_sid: Any) -> None: ...
    def create(self, identity: Any, binding_type: Any, address: Any, tag: Any = ..., notification_protocol_version: Any = ..., credential_sid: Any = ..., endpoint: Any = ...): ...
    def stream(self, start_date: Any = ..., end_date: Any = ..., identity: Any = ..., tag: Any = ..., limit: Optional[Any] = ..., page_size: Optional[Any] = ...): ...
    def list(self, start_date: Any = ..., end_date: Any = ..., identity: Any = ..., tag: Any = ..., limit: Optional[Any] = ..., page_size: Optional[Any] = ...): ...
    def page(self, start_date: Any = ..., end_date: Any = ..., identity: Any = ..., tag: Any = ..., page_token: Any = ..., page_number: Any = ..., page_size: Any = ...): ...
    def get_page(self, target_url: Any): ...
    def get(self, sid: Any): ...
    def __call__(self, sid: Any): ...

class BindingPage(Page):
    def __init__(self, version: Any, response: Any, solution: Any) -> None: ...
    def get_instance(self, payload: Any): ...

class BindingContext(InstanceContext):
    def __init__(self, version: Any, service_sid: Any, sid: Any) -> None: ...
    def fetch(self): ...
    def delete(self): ...

class BindingInstance(InstanceResource):
    class BindingType:
        APN: str = ...
        GCM: str = ...
        SMS: str = ...
        FCM: str = ...
        FACEBOOK_MESSENGER: str = ...
        ALEXA: str = ...
    def __init__(self, version: Any, payload: Any, service_sid: Any, sid: Optional[Any] = ...) -> None: ...
    @property
    def sid(self): ...
    @property
    def account_sid(self): ...
    @property
    def service_sid(self): ...
    @property
    def credential_sid(self): ...
    @property
    def date_created(self): ...
    @property
    def date_updated(self): ...
    @property
    def notification_protocol_version(self): ...
    @property
    def endpoint(self): ...
    @property
    def identity(self): ...
    @property
    def binding_type(self): ...
    @property
    def address(self): ...
    @property
    def tags(self): ...
    @property
    def url(self): ...
    @property
    def links(self): ...
    def fetch(self): ...
    def delete(self): ...
