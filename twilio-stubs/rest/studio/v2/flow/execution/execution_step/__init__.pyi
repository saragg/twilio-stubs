from twilio.base import deserialize as deserialize, values as values
from twilio.base.instance_context import InstanceContext as InstanceContext
from twilio.base.instance_resource import InstanceResource as InstanceResource
from twilio.base.list_resource import ListResource as ListResource
from twilio.base.page import Page as Page
from twilio.rest.studio.v2.flow.execution.execution_step.execution_step_context import ExecutionStepContextList as ExecutionStepContextList
from typing import Any, Optional

class ExecutionStepList(ListResource):
    def __init__(self, version: Any, flow_sid: Any, execution_sid: Any) -> None: ...
    def stream(self, limit: Optional[Any] = ..., page_size: Optional[Any] = ...): ...
    def list(self, limit: Optional[Any] = ..., page_size: Optional[Any] = ...): ...
    def page(self, page_token: Any = ..., page_number: Any = ..., page_size: Any = ...): ...
    def get_page(self, target_url: Any): ...
    def get(self, sid: Any): ...
    def __call__(self, sid: Any): ...

class ExecutionStepPage(Page):
    def __init__(self, version: Any, response: Any, solution: Any) -> None: ...
    def get_instance(self, payload: Any): ...

class ExecutionStepContext(InstanceContext):
    def __init__(self, version: Any, flow_sid: Any, execution_sid: Any, sid: Any) -> None: ...
    def fetch(self): ...
    @property
    def step_context(self): ...

class ExecutionStepInstance(InstanceResource):
    def __init__(self, version: Any, payload: Any, flow_sid: Any, execution_sid: Any, sid: Optional[Any] = ...) -> None: ...
    @property
    def sid(self): ...
    @property
    def account_sid(self): ...
    @property
    def flow_sid(self): ...
    @property
    def execution_sid(self): ...
    @property
    def name(self): ...
    @property
    def context(self): ...
    @property
    def transitioned_from(self): ...
    @property
    def transitioned_to(self): ...
    @property
    def date_created(self): ...
    @property
    def date_updated(self): ...
    @property
    def url(self): ...
    @property
    def links(self): ...
    def fetch(self): ...
    @property
    def step_context(self): ...
