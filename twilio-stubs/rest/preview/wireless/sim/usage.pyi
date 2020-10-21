from twilio.base import values as values
from twilio.base.instance_context import InstanceContext as InstanceContext
from twilio.base.instance_resource import InstanceResource as InstanceResource
from twilio.base.list_resource import ListResource as ListResource
from twilio.base.page import Page as Page
from typing import Any

class UsageList(ListResource):
    def __init__(self, version: Any, sim_sid: Any) -> None: ...
    def get(self): ...
    def __call__(self): ...

class UsagePage(Page):
    def __init__(self, version: Any, response: Any, solution: Any) -> None: ...
    def get_instance(self, payload: Any): ...

class UsageContext(InstanceContext):
    def __init__(self, version: Any, sim_sid: Any) -> None: ...
    def fetch(self, end: Any = ..., start: Any = ...): ...

class UsageInstance(InstanceResource):
    def __init__(self, version: Any, payload: Any, sim_sid: Any) -> None: ...
    @property
    def sim_sid(self): ...
    @property
    def sim_unique_name(self): ...
    @property
    def account_sid(self): ...
    @property
    def period(self): ...
    @property
    def commands_usage(self): ...
    @property
    def commands_costs(self): ...
    @property
    def data_usage(self): ...
    @property
    def data_costs(self): ...
    @property
    def url(self): ...
    def fetch(self, end: Any = ..., start: Any = ...): ...
