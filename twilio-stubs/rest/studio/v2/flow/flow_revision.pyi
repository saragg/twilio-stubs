from twilio.base import deserialize as deserialize, values as values
from twilio.base.instance_context import InstanceContext as InstanceContext
from twilio.base.instance_resource import InstanceResource as InstanceResource
from twilio.base.list_resource import ListResource as ListResource
from twilio.base.page import Page as Page
from typing import Any, Optional

class FlowRevisionList(ListResource):
    def __init__(self, version: Any, sid: Any) -> None: ...
    def stream(self, limit: Optional[Any] = ..., page_size: Optional[Any] = ...): ...
    def list(self, limit: Optional[Any] = ..., page_size: Optional[Any] = ...): ...
    def page(self, page_token: Any = ..., page_number: Any = ..., page_size: Any = ...): ...
    def get_page(self, target_url: Any): ...
    def get(self, revision: Any): ...
    def __call__(self, revision: Any): ...

class FlowRevisionPage(Page):
    def __init__(self, version: Any, response: Any, solution: Any) -> None: ...
    def get_instance(self, payload: Any): ...

class FlowRevisionContext(InstanceContext):
    def __init__(self, version: Any, sid: Any, revision: Any) -> None: ...
    def fetch(self): ...

class FlowRevisionInstance(InstanceResource):
    class Status:
        DRAFT: str = ...
        PUBLISHED: str = ...
    def __init__(self, version: Any, payload: Any, sid: Any, revision: Optional[Any] = ...) -> None: ...
    @property
    def sid(self): ...
    @property
    def account_sid(self): ...
    @property
    def friendly_name(self): ...
    @property
    def definition(self): ...
    @property
    def status(self): ...
    @property
    def revision(self): ...
    @property
    def commit_message(self): ...
    @property
    def valid(self): ...
    @property
    def errors(self): ...
    @property
    def date_created(self): ...
    @property
    def date_updated(self): ...
    @property
    def url(self): ...
    def fetch(self): ...
