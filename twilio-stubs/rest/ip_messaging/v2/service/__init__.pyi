from twilio.base import deserialize as deserialize, serialize as serialize, values as values
from twilio.base.instance_context import InstanceContext as InstanceContext
from twilio.base.instance_resource import InstanceResource as InstanceResource
from twilio.base.list_resource import ListResource as ListResource
from twilio.base.page import Page as Page
from twilio.rest.ip_messaging.v2.service.binding import BindingList as BindingList
from twilio.rest.ip_messaging.v2.service.channel import ChannelList as ChannelList
from twilio.rest.ip_messaging.v2.service.role import RoleList as RoleList
from twilio.rest.ip_messaging.v2.service.user import UserList as UserList
from typing import Any, Optional

class ServiceList(ListResource):
    def __init__(self, version: Any) -> None: ...
    def create(self, friendly_name: Any): ...
    def stream(self, limit: Optional[Any] = ..., page_size: Optional[Any] = ...): ...
    def list(self, limit: Optional[Any] = ..., page_size: Optional[Any] = ...): ...
    def page(self, page_token: Any = ..., page_number: Any = ..., page_size: Any = ...): ...
    def get_page(self, target_url: Any): ...
    def get(self, sid: Any): ...
    def __call__(self, sid: Any): ...

class ServicePage(Page):
    def __init__(self, version: Any, response: Any, solution: Any) -> None: ...
    def get_instance(self, payload: Any): ...

class ServiceContext(InstanceContext):
    def __init__(self, version: Any, sid: Any) -> None: ...
    def fetch(self): ...
    def delete(self): ...
    def update(self, friendly_name: Any = ..., default_service_role_sid: Any = ..., default_channel_role_sid: Any = ..., default_channel_creator_role_sid: Any = ..., read_status_enabled: Any = ..., reachability_enabled: Any = ..., typing_indicator_timeout: Any = ..., consumption_report_interval: Any = ..., notifications_new_message_enabled: Any = ..., notifications_new_message_template: Any = ..., notifications_new_message_sound: Any = ..., notifications_new_message_badge_count_enabled: Any = ..., notifications_added_to_channel_enabled: Any = ..., notifications_added_to_channel_template: Any = ..., notifications_added_to_channel_sound: Any = ..., notifications_removed_from_channel_enabled: Any = ..., notifications_removed_from_channel_template: Any = ..., notifications_removed_from_channel_sound: Any = ..., notifications_invited_to_channel_enabled: Any = ..., notifications_invited_to_channel_template: Any = ..., notifications_invited_to_channel_sound: Any = ..., pre_webhook_url: Any = ..., post_webhook_url: Any = ..., webhook_method: Any = ..., webhook_filters: Any = ..., limits_channel_members: Any = ..., limits_user_channels: Any = ..., media_compatibility_message: Any = ..., pre_webhook_retry_count: Any = ..., post_webhook_retry_count: Any = ..., notifications_log_enabled: Any = ...): ...
    @property
    def channels(self): ...
    @property
    def roles(self): ...
    @property
    def users(self): ...
    @property
    def bindings(self): ...

class ServiceInstance(InstanceResource):
    def __init__(self, version: Any, payload: Any, sid: Optional[Any] = ...) -> None: ...
    @property
    def sid(self): ...
    @property
    def account_sid(self): ...
    @property
    def friendly_name(self): ...
    @property
    def date_created(self): ...
    @property
    def date_updated(self): ...
    @property
    def default_service_role_sid(self): ...
    @property
    def default_channel_role_sid(self): ...
    @property
    def default_channel_creator_role_sid(self): ...
    @property
    def read_status_enabled(self): ...
    @property
    def reachability_enabled(self): ...
    @property
    def typing_indicator_timeout(self): ...
    @property
    def consumption_report_interval(self): ...
    @property
    def limits(self): ...
    @property
    def pre_webhook_url(self): ...
    @property
    def post_webhook_url(self): ...
    @property
    def webhook_method(self): ...
    @property
    def webhook_filters(self): ...
    @property
    def pre_webhook_retry_count(self): ...
    @property
    def post_webhook_retry_count(self): ...
    @property
    def notifications(self): ...
    @property
    def media(self): ...
    @property
    def url(self): ...
    @property
    def links(self): ...
    def fetch(self): ...
    def delete(self): ...
    def update(self, friendly_name: Any = ..., default_service_role_sid: Any = ..., default_channel_role_sid: Any = ..., default_channel_creator_role_sid: Any = ..., read_status_enabled: Any = ..., reachability_enabled: Any = ..., typing_indicator_timeout: Any = ..., consumption_report_interval: Any = ..., notifications_new_message_enabled: Any = ..., notifications_new_message_template: Any = ..., notifications_new_message_sound: Any = ..., notifications_new_message_badge_count_enabled: Any = ..., notifications_added_to_channel_enabled: Any = ..., notifications_added_to_channel_template: Any = ..., notifications_added_to_channel_sound: Any = ..., notifications_removed_from_channel_enabled: Any = ..., notifications_removed_from_channel_template: Any = ..., notifications_removed_from_channel_sound: Any = ..., notifications_invited_to_channel_enabled: Any = ..., notifications_invited_to_channel_template: Any = ..., notifications_invited_to_channel_sound: Any = ..., pre_webhook_url: Any = ..., post_webhook_url: Any = ..., webhook_method: Any = ..., webhook_filters: Any = ..., limits_channel_members: Any = ..., limits_user_channels: Any = ..., media_compatibility_message: Any = ..., pre_webhook_retry_count: Any = ..., post_webhook_retry_count: Any = ..., notifications_log_enabled: Any = ...): ...
    @property
    def channels(self): ...
    @property
    def roles(self): ...
    @property
    def users(self): ...
    @property
    def bindings(self): ...
