from twilio.base import deserialize as deserialize, serialize as serialize, values as values
from twilio.base.instance_context import InstanceContext as InstanceContext
from twilio.base.instance_resource import InstanceResource as InstanceResource
from twilio.base.list_resource import ListResource as ListResource
from twilio.base.page import Page as Page
from twilio.rest.api.v2010.account.message.feedback import FeedbackList as FeedbackList
from twilio.rest.api.v2010.account.message.media import MediaList as MediaList
from typing import Any, Optional

class MessageList(ListResource):
    def __init__(self, version: Any, account_sid: Any) -> None: ...
    def create(self, to: Any, status_callback: Any = ..., application_sid: Any = ..., max_price: Any = ..., provide_feedback: Any = ..., attempt: Any = ..., validity_period: Any = ..., force_delivery: Any = ..., content_retention: Any = ..., address_retention: Any = ..., smart_encoded: Any = ..., persistent_action: Any = ..., from_: Any = ..., messaging_service_sid: Any = ..., body: Any = ..., media_url: Any = ...): ...
    def stream(self, to: Any = ..., from_: Any = ..., date_sent_before: Any = ..., date_sent: Any = ..., date_sent_after: Any = ..., limit: Optional[Any] = ..., page_size: Optional[Any] = ...): ...
    def list(self, to: Any = ..., from_: Any = ..., date_sent_before: Any = ..., date_sent: Any = ..., date_sent_after: Any = ..., limit: Optional[Any] = ..., page_size: Optional[Any] = ...): ...
    def page(self, to: Any = ..., from_: Any = ..., date_sent_before: Any = ..., date_sent: Any = ..., date_sent_after: Any = ..., page_token: Any = ..., page_number: Any = ..., page_size: Any = ...): ...
    def get_page(self, target_url: Any): ...
    def get(self, sid: Any): ...
    def __call__(self, sid: Any): ...

class MessagePage(Page):
    def __init__(self, version: Any, response: Any, solution: Any) -> None: ...
    def get_instance(self, payload: Any): ...

class MessageContext(InstanceContext):
    def __init__(self, version: Any, account_sid: Any, sid: Any) -> None: ...
    def delete(self): ...
    def fetch(self): ...
    def update(self, body: Any): ...
    @property
    def media(self): ...
    @property
    def feedback(self): ...

class MessageInstance(InstanceResource):
    class Status:
        QUEUED: str = ...
        SENDING: str = ...
        SENT: str = ...
        FAILED: str = ...
        DELIVERED: str = ...
        UNDELIVERED: str = ...
        RECEIVING: str = ...
        RECEIVED: str = ...
        ACCEPTED: str = ...
        SCHEDULED: str = ...
        READ: str = ...
        PARTIALLY_DELIVERED: str = ...
    class Direction:
        INBOUND: str = ...
        OUTBOUND_API: str = ...
        OUTBOUND_CALL: str = ...
        OUTBOUND_REPLY: str = ...
    class ContentRetention:
        RETAIN: str = ...
    class AddressRetention:
        RETAIN: str = ...
    class TrafficType:
        FREE: str = ...
    class ScheduleType:
        FIXED: str = ...
        OPTIMIZE: str = ...
    def __init__(self, version: Any, payload: Any, account_sid: Any, sid: Optional[Any] = ...) -> None: ...
    @property
    def body(self): ...
    @property
    def num_segments(self): ...
    @property
    def direction(self): ...
    @property
    def from_(self): ...
    @property
    def to(self): ...
    @property
    def date_updated(self): ...
    @property
    def price(self): ...
    @property
    def error_message(self): ...
    @property
    def uri(self): ...
    @property
    def account_sid(self): ...
    @property
    def num_media(self): ...
    @property
    def status(self): ...
    @property
    def messaging_service_sid(self): ...
    @property
    def sid(self): ...
    @property
    def date_sent(self): ...
    @property
    def date_created(self): ...
    @property
    def error_code(self): ...
    @property
    def price_unit(self): ...
    @property
    def api_version(self): ...
    @property
    def subresource_uris(self): ...
    def delete(self): ...
    def fetch(self): ...
    def update(self, body: Any): ...
    @property
    def media(self): ...
    @property
    def feedback(self): ...
