from twilio.base import deserialize as deserialize, serialize as serialize, values as values
from twilio.base.instance_context import InstanceContext as InstanceContext
from twilio.base.instance_resource import InstanceResource as InstanceResource
from twilio.base.list_resource import ListResource as ListResource
from twilio.base.page import Page as Page
from twilio.rest.preview.hosted_numbers.authorization_document.dependent_hosted_number_order import DependentHostedNumberOrderList as DependentHostedNumberOrderList
from typing import Any, Optional

class AuthorizationDocumentList(ListResource):
    def __init__(self, version: Any) -> None: ...
    def stream(self, email: Any = ..., status: Any = ..., limit: Optional[Any] = ..., page_size: Optional[Any] = ...): ...
    def list(self, email: Any = ..., status: Any = ..., limit: Optional[Any] = ..., page_size: Optional[Any] = ...): ...
    def page(self, email: Any = ..., status: Any = ..., page_token: Any = ..., page_number: Any = ..., page_size: Any = ...): ...
    def get_page(self, target_url: Any): ...
    def create(self, hosted_number_order_sids: Any, address_sid: Any, email: Any, contact_title: Any, contact_phone_number: Any, cc_emails: Any = ...): ...
    def get(self, sid: Any): ...
    def __call__(self, sid: Any): ...

class AuthorizationDocumentPage(Page):
    def __init__(self, version: Any, response: Any, solution: Any) -> None: ...
    def get_instance(self, payload: Any): ...

class AuthorizationDocumentContext(InstanceContext):
    def __init__(self, version: Any, sid: Any) -> None: ...
    def fetch(self): ...
    def update(self, hosted_number_order_sids: Any = ..., address_sid: Any = ..., email: Any = ..., cc_emails: Any = ..., status: Any = ..., contact_title: Any = ..., contact_phone_number: Any = ...): ...
    @property
    def dependent_hosted_number_orders(self): ...

class AuthorizationDocumentInstance(InstanceResource):
    class Status:
        OPENED: str = ...
        SIGNING: str = ...
        SIGNED: str = ...
        CANCELED: str = ...
        FAILED: str = ...
    def __init__(self, version: Any, payload: Any, sid: Optional[Any] = ...) -> None: ...
    @property
    def sid(self): ...
    @property
    def address_sid(self): ...
    @property
    def status(self): ...
    @property
    def email(self): ...
    @property
    def cc_emails(self): ...
    @property
    def date_created(self): ...
    @property
    def date_updated(self): ...
    @property
    def url(self): ...
    @property
    def links(self): ...
    def fetch(self): ...
    def update(self, hosted_number_order_sids: Any = ..., address_sid: Any = ..., email: Any = ..., cc_emails: Any = ..., status: Any = ..., contact_title: Any = ..., contact_phone_number: Any = ...): ...
    @property
    def dependent_hosted_number_orders(self): ...
