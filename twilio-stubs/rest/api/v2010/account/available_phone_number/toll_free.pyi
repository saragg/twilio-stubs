from twilio.base import deserialize as deserialize, values as values
from twilio.base.instance_resource import InstanceResource as InstanceResource
from twilio.base.list_resource import ListResource as ListResource
from twilio.base.page import Page as Page
from typing import Any, Optional

class TollFreeList(ListResource):
    def __init__(self, version: Any, account_sid: Any, country_code: Any) -> None: ...
    def stream(self, area_code: Any = ..., contains: Any = ..., sms_enabled: Any = ..., mms_enabled: Any = ..., voice_enabled: Any = ..., exclude_all_address_required: Any = ..., exclude_local_address_required: Any = ..., exclude_foreign_address_required: Any = ..., beta: Any = ..., near_number: Any = ..., near_lat_long: Any = ..., distance: Any = ..., in_postal_code: Any = ..., in_region: Any = ..., in_rate_center: Any = ..., in_lata: Any = ..., in_locality: Any = ..., fax_enabled: Any = ..., limit: Optional[Any] = ..., page_size: Optional[Any] = ...): ...
    def list(self, area_code: Any = ..., contains: Any = ..., sms_enabled: Any = ..., mms_enabled: Any = ..., voice_enabled: Any = ..., exclude_all_address_required: Any = ..., exclude_local_address_required: Any = ..., exclude_foreign_address_required: Any = ..., beta: Any = ..., near_number: Any = ..., near_lat_long: Any = ..., distance: Any = ..., in_postal_code: Any = ..., in_region: Any = ..., in_rate_center: Any = ..., in_lata: Any = ..., in_locality: Any = ..., fax_enabled: Any = ..., limit: Optional[Any] = ..., page_size: Optional[Any] = ...): ...
    def page(self, area_code: Any = ..., contains: Any = ..., sms_enabled: Any = ..., mms_enabled: Any = ..., voice_enabled: Any = ..., exclude_all_address_required: Any = ..., exclude_local_address_required: Any = ..., exclude_foreign_address_required: Any = ..., beta: Any = ..., near_number: Any = ..., near_lat_long: Any = ..., distance: Any = ..., in_postal_code: Any = ..., in_region: Any = ..., in_rate_center: Any = ..., in_lata: Any = ..., in_locality: Any = ..., fax_enabled: Any = ..., page_token: Any = ..., page_number: Any = ..., page_size: Any = ...): ...
    def get_page(self, target_url: Any): ...

class TollFreePage(Page):
    def __init__(self, version: Any, response: Any, solution: Any) -> None: ...
    def get_instance(self, payload: Any): ...

class TollFreeInstance(InstanceResource):
    def __init__(self, version: Any, payload: Any, account_sid: Any, country_code: Any) -> None: ...
    @property
    def friendly_name(self): ...
    @property
    def phone_number(self): ...
    @property
    def lata(self): ...
    @property
    def locality(self): ...
    @property
    def rate_center(self): ...
    @property
    def latitude(self): ...
    @property
    def longitude(self): ...
    @property
    def region(self): ...
    @property
    def postal_code(self): ...
    @property
    def iso_country(self): ...
    @property
    def address_requirements(self): ...
    @property
    def beta(self): ...
    @property
    def capabilities(self): ...
