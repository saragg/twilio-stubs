from twilio.base.instance_resource import InstanceResource as InstanceResource
from twilio.base.list_resource import ListResource as ListResource
from twilio.base.page import Page as Page
from twilio.rest.pricing.v2.voice.country import CountryList as CountryList
from twilio.rest.pricing.v2.voice.number import NumberList as NumberList
from typing import Any

class VoiceList(ListResource):
    def __init__(self, version: Any) -> None: ...
    @property
    def countries(self): ...
    @property
    def numbers(self): ...

class VoicePage(Page):
    def __init__(self, version: Any, response: Any, solution: Any) -> None: ...
    def get_instance(self, payload: Any): ...

class VoiceInstance(InstanceResource):
    def __init__(self, version: Any, payload: Any) -> None: ...
    @property
    def name(self): ...
    @property
    def url(self): ...
    @property
    def links(self): ...
