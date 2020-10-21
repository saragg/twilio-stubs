from twilio.base import deserialize as deserialize, serialize as serialize, values as values
from twilio.base.instance_context import InstanceContext as InstanceContext
from twilio.base.instance_resource import InstanceResource as InstanceResource
from twilio.base.list_resource import ListResource as ListResource
from twilio.base.page import Page as Page
from typing import Any, Optional

class AlertList(ListResource):
    def __init__(self, version: Any) -> None: ...
    def stream(self, log_level: Any = ..., start_date: Any = ..., end_date: Any = ..., limit: Optional[Any] = ..., page_size: Optional[Any] = ...): ...
    def list(self, log_level: Any = ..., start_date: Any = ..., end_date: Any = ..., limit: Optional[Any] = ..., page_size: Optional[Any] = ...): ...
    def page(self, log_level: Any = ..., start_date: Any = ..., end_date: Any = ..., page_token: Any = ..., page_number: Any = ..., page_size: Any = ...): ...
    def get_page(self, target_url: Any): ...
    def get(self, sid: Any): ...
    def __call__(self, sid: Any): ...

class AlertPage(Page):
    def __init__(self, version: Any, response: Any, solution: Any) -> None: ...
    def get_instance(self, payload: Any): ...

class AlertContext(InstanceContext):
    def __init__(self, version: Any, sid: Any) -> None: ...
    def fetch(self): ...

class AlertInstance(InstanceResource):
    def __init__(self, version: Any, payload: Any, sid: Optional[Any] = ...) -> None: ...
    @property
    def account_sid(self): ...
    @property
    def alert_text(self): ...
    @property
    def api_version(self): ...
    @property
    def date_created(self): ...
    @property
    def date_generated(self): ...
    @property
    def date_updated(self): ...
    @property
    def error_code(self): ...
    @property
    def log_level(self): ...
    @property
    def more_info(self): ...
    @property
    def request_method(self): ...
    @property
    def request_url(self): ...
    @property
    def request_variables(self): ...
    @property
    def resource_sid(self): ...
    @property
    def response_body(self): ...
    @property
    def response_headers(self): ...
    @property
    def sid(self): ...
    @property
    def url(self): ...
    @property
    def request_headers(self): ...
    @property
    def service_sid(self): ...
    def fetch(self): ...
