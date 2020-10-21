from twilio.base import deserialize as deserialize, values as values
from twilio.base.instance_context import InstanceContext as InstanceContext
from twilio.base.instance_resource import InstanceResource as InstanceResource
from twilio.base.list_resource import ListResource as ListResource
from twilio.base.page import Page as Page
from typing import Any

class SecondaryAuthTokenList(ListResource):
    def __init__(self, version: Any) -> None: ...
    def get(self): ...
    def __call__(self): ...

class SecondaryAuthTokenPage(Page):
    def __init__(self, version: Any, response: Any, solution: Any) -> None: ...
    def get_instance(self, payload: Any): ...

class SecondaryAuthTokenContext(InstanceContext):
    def __init__(self, version: Any) -> None: ...
    def create(self): ...
    def delete(self): ...

class SecondaryAuthTokenInstance(InstanceResource):
    def __init__(self, version: Any, payload: Any) -> None: ...
    @property
    def account_sid(self): ...
    @property
    def date_created(self): ...
    @property
    def date_updated(self): ...
    @property
    def secondary_auth_token(self): ...
    @property
    def url(self): ...
    def create(self): ...
    def delete(self): ...
