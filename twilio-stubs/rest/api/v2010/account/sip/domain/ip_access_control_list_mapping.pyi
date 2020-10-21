from twilio.base import deserialize as deserialize, values as values
from twilio.base.instance_context import InstanceContext as InstanceContext
from twilio.base.instance_resource import InstanceResource as InstanceResource
from twilio.base.list_resource import ListResource as ListResource
from twilio.base.page import Page as Page
from typing import Any, Optional

class IpAccessControlListMappingList(ListResource):
    def __init__(self, version: Any, account_sid: Any, domain_sid: Any) -> None: ...
    def create(self, ip_access_control_list_sid: Any): ...
    def stream(self, limit: Optional[Any] = ..., page_size: Optional[Any] = ...): ...
    def list(self, limit: Optional[Any] = ..., page_size: Optional[Any] = ...): ...
    def page(self, page_token: Any = ..., page_number: Any = ..., page_size: Any = ...): ...
    def get_page(self, target_url: Any): ...
    def get(self, sid: Any): ...
    def __call__(self, sid: Any): ...

class IpAccessControlListMappingPage(Page):
    def __init__(self, version: Any, response: Any, solution: Any) -> None: ...
    def get_instance(self, payload: Any): ...

class IpAccessControlListMappingContext(InstanceContext):
    def __init__(self, version: Any, account_sid: Any, domain_sid: Any, sid: Any) -> None: ...
    def fetch(self): ...
    def delete(self): ...

class IpAccessControlListMappingInstance(InstanceResource):
    def __init__(self, version: Any, payload: Any, account_sid: Any, domain_sid: Any, sid: Optional[Any] = ...) -> None: ...
    @property
    def account_sid(self): ...
    @property
    def date_created(self): ...
    @property
    def date_updated(self): ...
    @property
    def friendly_name(self): ...
    @property
    def sid(self): ...
    @property
    def uri(self): ...
    @property
    def subresource_uris(self): ...
    def fetch(self): ...
    def delete(self): ...
