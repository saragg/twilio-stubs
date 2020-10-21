from twilio.base import deserialize as deserialize, values as values
from twilio.base.instance_context import InstanceContext as InstanceContext
from twilio.base.instance_resource import InstanceResource as InstanceResource
from twilio.base.list_resource import ListResource as ListResource
from twilio.base.page import Page as Page
from typing import Any, Optional

class QueryList(ListResource):
    def __init__(self, version: Any, assistant_sid: Any) -> None: ...
    def stream(self, language: Any = ..., model_build: Any = ..., status: Any = ..., limit: Optional[Any] = ..., page_size: Optional[Any] = ...): ...
    def list(self, language: Any = ..., model_build: Any = ..., status: Any = ..., limit: Optional[Any] = ..., page_size: Optional[Any] = ...): ...
    def page(self, language: Any = ..., model_build: Any = ..., status: Any = ..., page_token: Any = ..., page_number: Any = ..., page_size: Any = ...): ...
    def get_page(self, target_url: Any): ...
    def create(self, language: Any, query: Any, tasks: Any = ..., model_build: Any = ..., field: Any = ...): ...
    def get(self, sid: Any): ...
    def __call__(self, sid: Any): ...

class QueryPage(Page):
    def __init__(self, version: Any, response: Any, solution: Any) -> None: ...
    def get_instance(self, payload: Any): ...

class QueryContext(InstanceContext):
    def __init__(self, version: Any, assistant_sid: Any, sid: Any) -> None: ...
    def fetch(self): ...
    def update(self, sample_sid: Any = ..., status: Any = ...): ...
    def delete(self): ...

class QueryInstance(InstanceResource):
    def __init__(self, version: Any, payload: Any, assistant_sid: Any, sid: Optional[Any] = ...) -> None: ...
    @property
    def account_sid(self): ...
    @property
    def date_created(self): ...
    @property
    def date_updated(self): ...
    @property
    def results(self): ...
    @property
    def language(self): ...
    @property
    def model_build_sid(self): ...
    @property
    def query(self): ...
    @property
    def sample_sid(self): ...
    @property
    def assistant_sid(self): ...
    @property
    def sid(self): ...
    @property
    def status(self): ...
    @property
    def url(self): ...
    @property
    def source_channel(self): ...
    def fetch(self): ...
    def update(self, sample_sid: Any = ..., status: Any = ...): ...
    def delete(self): ...
