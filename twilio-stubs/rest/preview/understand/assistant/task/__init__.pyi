from twilio.base import deserialize as deserialize, serialize as serialize, values as values
from twilio.base.instance_context import InstanceContext as InstanceContext
from twilio.base.instance_resource import InstanceResource as InstanceResource
from twilio.base.list_resource import ListResource as ListResource
from twilio.base.page import Page as Page
from twilio.rest.preview.understand.assistant.task.field import FieldList as FieldList
from twilio.rest.preview.understand.assistant.task.sample import SampleList as SampleList
from twilio.rest.preview.understand.assistant.task.task_actions import TaskActionsList as TaskActionsList
from twilio.rest.preview.understand.assistant.task.task_statistics import TaskStatisticsList as TaskStatisticsList
from typing import Any, Optional

class TaskList(ListResource):
    def __init__(self, version: Any, assistant_sid: Any) -> None: ...
    def stream(self, limit: Optional[Any] = ..., page_size: Optional[Any] = ...): ...
    def list(self, limit: Optional[Any] = ..., page_size: Optional[Any] = ...): ...
    def page(self, page_token: Any = ..., page_number: Any = ..., page_size: Any = ...): ...
    def get_page(self, target_url: Any): ...
    def create(self, unique_name: Any, friendly_name: Any = ..., actions: Any = ..., actions_url: Any = ...): ...
    def get(self, sid: Any): ...
    def __call__(self, sid: Any): ...

class TaskPage(Page):
    def __init__(self, version: Any, response: Any, solution: Any) -> None: ...
    def get_instance(self, payload: Any): ...

class TaskContext(InstanceContext):
    def __init__(self, version: Any, assistant_sid: Any, sid: Any) -> None: ...
    def fetch(self): ...
    def update(self, friendly_name: Any = ..., unique_name: Any = ..., actions: Any = ..., actions_url: Any = ...): ...
    def delete(self): ...
    @property
    def fields(self): ...
    @property
    def samples(self): ...
    @property
    def task_actions(self): ...
    @property
    def statistics(self): ...

class TaskInstance(InstanceResource):
    def __init__(self, version: Any, payload: Any, assistant_sid: Any, sid: Optional[Any] = ...) -> None: ...
    @property
    def account_sid(self): ...
    @property
    def date_created(self): ...
    @property
    def date_updated(self): ...
    @property
    def friendly_name(self): ...
    @property
    def links(self): ...
    @property
    def assistant_sid(self): ...
    @property
    def sid(self): ...
    @property
    def unique_name(self): ...
    @property
    def actions_url(self): ...
    @property
    def url(self): ...
    def fetch(self): ...
    def update(self, friendly_name: Any = ..., unique_name: Any = ..., actions: Any = ..., actions_url: Any = ...): ...
    def delete(self): ...
    @property
    def fields(self): ...
    @property
    def samples(self): ...
    @property
    def task_actions(self): ...
    @property
    def statistics(self): ...
