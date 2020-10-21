from twilio.base import deserialize as deserialize, serialize as serialize, values as values
from twilio.base.instance_context import InstanceContext as InstanceContext
from twilio.base.instance_resource import InstanceResource as InstanceResource
from twilio.base.list_resource import ListResource as ListResource
from twilio.base.page import Page as Page
from typing import Any, Optional

class SyncMapItemList(ListResource):
    def __init__(self, version: Any, service_sid: Any, map_sid: Any) -> None: ...
    def create(self, key: Any, data: Any): ...
    def stream(self, order: Any = ..., from_: Any = ..., bounds: Any = ..., limit: Optional[Any] = ..., page_size: Optional[Any] = ...): ...
    def list(self, order: Any = ..., from_: Any = ..., bounds: Any = ..., limit: Optional[Any] = ..., page_size: Optional[Any] = ...): ...
    def page(self, order: Any = ..., from_: Any = ..., bounds: Any = ..., page_token: Any = ..., page_number: Any = ..., page_size: Any = ...): ...
    def get_page(self, target_url: Any): ...
    def get(self, key: Any): ...
    def __call__(self, key: Any): ...

class SyncMapItemPage(Page):
    def __init__(self, version: Any, response: Any, solution: Any) -> None: ...
    def get_instance(self, payload: Any): ...

class SyncMapItemContext(InstanceContext):
    def __init__(self, version: Any, service_sid: Any, map_sid: Any, key: Any) -> None: ...
    def fetch(self): ...
    def delete(self, if_match: Any = ...): ...
    def update(self, data: Any, if_match: Any = ...): ...

class SyncMapItemInstance(InstanceResource):
    class QueryResultOrder:
        ASC: str = ...
        DESC: str = ...
    class QueryFromBoundType:
        INCLUSIVE: str = ...
        EXCLUSIVE: str = ...
    def __init__(self, version: Any, payload: Any, service_sid: Any, map_sid: Any, key: Optional[Any] = ...) -> None: ...
    @property
    def key(self): ...
    @property
    def account_sid(self): ...
    @property
    def service_sid(self): ...
    @property
    def map_sid(self): ...
    @property
    def url(self): ...
    @property
    def revision(self): ...
    @property
    def data(self): ...
    @property
    def date_created(self): ...
    @property
    def date_updated(self): ...
    @property
    def created_by(self): ...
    def fetch(self): ...
    def delete(self, if_match: Any = ...): ...
    def update(self, data: Any, if_match: Any = ...): ...
