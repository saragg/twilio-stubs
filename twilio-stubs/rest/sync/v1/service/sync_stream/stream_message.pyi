from twilio.base import serialize as serialize, values as values
from twilio.base.instance_resource import InstanceResource as InstanceResource
from twilio.base.list_resource import ListResource as ListResource
from twilio.base.page import Page as Page
from typing import Any

class StreamMessageList(ListResource):
    def __init__(self, version: Any, service_sid: Any, stream_sid: Any) -> None: ...
    def create(self, data: Any): ...

class StreamMessagePage(Page):
    def __init__(self, version: Any, response: Any, solution: Any) -> None: ...
    def get_instance(self, payload: Any): ...

class StreamMessageInstance(InstanceResource):
    def __init__(self, version: Any, payload: Any, service_sid: Any, stream_sid: Any) -> None: ...
    @property
    def sid(self): ...
    @property
    def data(self): ...
