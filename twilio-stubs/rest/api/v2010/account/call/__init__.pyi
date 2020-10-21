from twilio.base import deserialize as deserialize, serialize as serialize, values as values
from twilio.base.instance_context import InstanceContext as InstanceContext
from twilio.base.instance_resource import InstanceResource as InstanceResource
from twilio.base.list_resource import ListResource as ListResource
from twilio.base.page import Page as Page
from twilio.rest.api.v2010.account.call.feedback import FeedbackList as FeedbackList
from twilio.rest.api.v2010.account.call.feedback_summary import FeedbackSummaryList as FeedbackSummaryList
from twilio.rest.api.v2010.account.call.notification import NotificationList as NotificationList
from twilio.rest.api.v2010.account.call.payment import PaymentList as PaymentList
from twilio.rest.api.v2010.account.call.recording import RecordingList as RecordingList
from typing import Any, Optional

class CallList(ListResource):
    def __init__(self, version: Any, account_sid: Any) -> None: ...
    def create(self, to: Any, from_: Any, method: Any = ..., fallback_url: Any = ..., fallback_method: Any = ..., status_callback: Any = ..., status_callback_event: Any = ..., status_callback_method: Any = ..., send_digits: Any = ..., timeout: Any = ..., record: Any = ..., recording_channels: Any = ..., recording_status_callback: Any = ..., recording_status_callback_method: Any = ..., sip_auth_username: Any = ..., sip_auth_password: Any = ..., machine_detection: Any = ..., machine_detection_timeout: Any = ..., recording_status_callback_event: Any = ..., trim: Any = ..., caller_id: Any = ..., machine_detection_speech_threshold: Any = ..., machine_detection_speech_end_threshold: Any = ..., machine_detection_silence_timeout: Any = ..., async_amd: Any = ..., async_amd_status_callback: Any = ..., async_amd_status_callback_method: Any = ..., byoc: Any = ..., call_reason: Any = ..., url: Any = ..., twiml: Any = ..., application_sid: Any = ...): ...
    def stream(self, to: Any = ..., from_: Any = ..., parent_call_sid: Any = ..., status: Any = ..., start_time_before: Any = ..., start_time: Any = ..., start_time_after: Any = ..., end_time_before: Any = ..., end_time: Any = ..., end_time_after: Any = ..., limit: Optional[Any] = ..., page_size: Optional[Any] = ...): ...
    def list(self, to: Any = ..., from_: Any = ..., parent_call_sid: Any = ..., status: Any = ..., start_time_before: Any = ..., start_time: Any = ..., start_time_after: Any = ..., end_time_before: Any = ..., end_time: Any = ..., end_time_after: Any = ..., limit: Optional[Any] = ..., page_size: Optional[Any] = ...): ...
    def page(self, to: Any = ..., from_: Any = ..., parent_call_sid: Any = ..., status: Any = ..., start_time_before: Any = ..., start_time: Any = ..., start_time_after: Any = ..., end_time_before: Any = ..., end_time: Any = ..., end_time_after: Any = ..., page_token: Any = ..., page_number: Any = ..., page_size: Any = ...): ...
    def get_page(self, target_url: Any): ...
    @property
    def feedback_summaries(self): ...
    def get(self, sid: Any): ...
    def __call__(self, sid: Any): ...

class CallPage(Page):
    def __init__(self, version: Any, response: Any, solution: Any) -> None: ...
    def get_instance(self, payload: Any): ...

class CallContext(InstanceContext):
    def __init__(self, version: Any, account_sid: Any, sid: Any) -> None: ...
    def delete(self): ...
    def fetch(self): ...
    def update(self, url: Any = ..., method: Any = ..., status: Any = ..., fallback_url: Any = ..., fallback_method: Any = ..., status_callback: Any = ..., status_callback_method: Any = ..., twiml: Any = ...): ...
    @property
    def recordings(self): ...
    @property
    def notifications(self): ...
    @property
    def feedback(self): ...
    @property
    def payments(self): ...

class CallInstance(InstanceResource):
    class Event:
        INITIATED: str = ...
        RINGING: str = ...
        ANSWERED: str = ...
        COMPLETED: str = ...
    class Status:
        QUEUED: str = ...
        RINGING: str = ...
        IN_PROGRESS: str = ...
        COMPLETED: str = ...
        BUSY: str = ...
        FAILED: str = ...
        NO_ANSWER: str = ...
        CANCELED: str = ...
    class UpdateStatus:
        CANCELED: str = ...
        COMPLETED: str = ...
    def __init__(self, version: Any, payload: Any, account_sid: Any, sid: Optional[Any] = ...) -> None: ...
    @property
    def sid(self): ...
    @property
    def date_created(self): ...
    @property
    def date_updated(self): ...
    @property
    def parent_call_sid(self): ...
    @property
    def account_sid(self): ...
    @property
    def to(self): ...
    @property
    def to_formatted(self): ...
    @property
    def from_(self): ...
    @property
    def from_formatted(self): ...
    @property
    def phone_number_sid(self): ...
    @property
    def status(self): ...
    @property
    def start_time(self): ...
    @property
    def end_time(self): ...
    @property
    def duration(self): ...
    @property
    def price(self): ...
    @property
    def price_unit(self): ...
    @property
    def direction(self): ...
    @property
    def answered_by(self): ...
    @property
    def annotation(self): ...
    @property
    def api_version(self): ...
    @property
    def forwarded_from(self): ...
    @property
    def group_sid(self): ...
    @property
    def caller_name(self): ...
    @property
    def queue_time(self): ...
    @property
    def trunk_sid(self): ...
    @property
    def uri(self): ...
    @property
    def subresource_uris(self): ...
    def delete(self): ...
    def fetch(self): ...
    def update(self, url: Any = ..., method: Any = ..., status: Any = ..., fallback_url: Any = ..., fallback_method: Any = ..., status_callback: Any = ..., status_callback_method: Any = ..., twiml: Any = ...): ...
    @property
    def recordings(self): ...
    @property
    def notifications(self): ...
    @property
    def feedback(self): ...
    @property
    def payments(self): ...
