from twilio.base import deserialize as deserialize, values as values
from twilio.base.instance_resource import InstanceResource as InstanceResource
from twilio.base.list_resource import ListResource as ListResource
from twilio.base.page import Page as Page
from typing import Any, Optional

class DependentHostedNumberOrderList(ListResource):
    def __init__(self, version: Any, signing_document_sid: Any) -> None: ...
    def stream(self, status: Any = ..., phone_number: Any = ..., incoming_phone_number_sid: Any = ..., friendly_name: Any = ..., unique_name: Any = ..., limit: Optional[Any] = ..., page_size: Optional[Any] = ...): ...
    def list(self, status: Any = ..., phone_number: Any = ..., incoming_phone_number_sid: Any = ..., friendly_name: Any = ..., unique_name: Any = ..., limit: Optional[Any] = ..., page_size: Optional[Any] = ...): ...
    def page(self, status: Any = ..., phone_number: Any = ..., incoming_phone_number_sid: Any = ..., friendly_name: Any = ..., unique_name: Any = ..., page_token: Any = ..., page_number: Any = ..., page_size: Any = ...): ...
    def get_page(self, target_url: Any): ...

class DependentHostedNumberOrderPage(Page):
    def __init__(self, version: Any, response: Any, solution: Any) -> None: ...
    def get_instance(self, payload: Any): ...

class DependentHostedNumberOrderInstance(InstanceResource):
    class Status:
        RECEIVED: str = ...
        PENDING_VERIFICATION: str = ...
        VERIFIED: str = ...
        PENDING_LOA: str = ...
        CARRIER_PROCESSING: str = ...
        TESTING: str = ...
        COMPLETED: str = ...
        FAILED: str = ...
        ACTION_REQUIRED: str = ...
    class VerificationType:
        PHONE_CALL: str = ...
        PHONE_BILL: str = ...
    def __init__(self, version: Any, payload: Any, signing_document_sid: Any) -> None: ...
    @property
    def sid(self): ...
    @property
    def account_sid(self): ...
    @property
    def incoming_phone_number_sid(self): ...
    @property
    def address_sid(self): ...
    @property
    def signing_document_sid(self): ...
    @property
    def phone_number(self): ...
    @property
    def capabilities(self): ...
    @property
    def friendly_name(self): ...
    @property
    def unique_name(self): ...
    @property
    def status(self): ...
    @property
    def failure_reason(self): ...
    @property
    def date_created(self): ...
    @property
    def date_updated(self): ...
    @property
    def verification_attempts(self): ...
    @property
    def email(self): ...
    @property
    def cc_emails(self): ...
    @property
    def verification_type(self): ...
    @property
    def verification_document_sid(self): ...
    @property
    def extension(self): ...
    @property
    def call_delay(self): ...
    @property
    def verification_code(self): ...
    @property
    def verification_call_sids(self): ...
