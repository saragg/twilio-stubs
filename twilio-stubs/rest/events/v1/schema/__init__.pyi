from twilio.base import deserialize as deserialize, values as values
from twilio.base.instance_context import InstanceContext as InstanceContext
from twilio.base.instance_resource import InstanceResource as InstanceResource
from twilio.base.list_resource import ListResource as ListResource
from twilio.base.page import Page as Page
from twilio.rest.events.v1.schema.schema_version import VersionList as VersionList
from typing import Any, Optional

class SchemaList(ListResource):
    def __init__(self, version: Any) -> None: ...
    def get(self, id: Any): ...
    def __call__(self, id: Any): ...

class SchemaPage(Page):
    def __init__(self, version: Any, response: Any, solution: Any) -> None: ...
    def get_instance(self, payload: Any): ...

class SchemaContext(InstanceContext):
    def __init__(self, version: Any, id: Any) -> None: ...
    def fetch(self): ...
    @property
    def versions(self): ...

class SchemaInstance(InstanceResource):
    def __init__(self, version: Any, payload: Any, id: Optional[Any] = ...) -> None: ...
    @property
    def id(self): ...
    @property
    def url(self): ...
    @property
    def links(self): ...
    @property
    def last_created(self): ...
    @property
    def last_version(self): ...
    def fetch(self): ...
    @property
    def versions(self): ...
