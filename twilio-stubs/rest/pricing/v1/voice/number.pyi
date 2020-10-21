from twilio.base import values as values
from twilio.base.instance_context import InstanceContext as InstanceContext
from twilio.base.instance_resource import InstanceResource as InstanceResource
from twilio.base.list_resource import ListResource as ListResource
from twilio.base.page import Page as Page
from typing import Any, Optional

class NumberList(ListResource):
    def __init__(self, version: Any) -> None: ...
    def get(self, number: Any): ...
    def __call__(self, number: Any): ...

class NumberPage(Page):
    def __init__(self, version: Any, response: Any, solution: Any) -> None: ...
    def get_instance(self, payload: Any): ...

class NumberContext(InstanceContext):
    def __init__(self, version: Any, number: Any) -> None: ...
    def fetch(self): ...

class NumberInstance(InstanceResource):
    def __init__(self, version: Any, payload: Any, number: Optional[Any] = ...) -> None: ...
    @property
    def number(self): ...
    @property
    def country(self): ...
    @property
    def iso_country(self): ...
    @property
    def outbound_call_price(self): ...
    @property
    def inbound_call_price(self): ...
    @property
    def price_unit(self): ...
    @property
    def url(self): ...
    def fetch(self): ...
