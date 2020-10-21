from twilio.base import values as values
from twilio.base.instance_resource import InstanceResource as InstanceResource
from twilio.base.list_resource import ListResource as ListResource
from twilio.base.page import Page as Page
from typing import Any

class ChannelList(ListResource):
    def __init__(self, version: Any, branded_channel_sid: Any) -> None: ...
    def create(self, phone_number_sid: Any): ...

class ChannelPage(Page):
    def __init__(self, version: Any, response: Any, solution: Any) -> None: ...
    def get_instance(self, payload: Any): ...

class ChannelInstance(InstanceResource):
    def __init__(self, version: Any, payload: Any, branded_channel_sid: Any) -> None: ...
    @property
    def account_sid(self): ...
    @property
    def business_sid(self): ...
    @property
    def brand_sid(self): ...
    @property
    def branded_channel_sid(self): ...
    @property
    def phone_number_sid(self): ...
    @property
    def phone_number(self): ...
    @property
    def url(self): ...
