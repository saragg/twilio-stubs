from twilio.base.domain import Domain as Domain
from twilio.rest.conversations.v1 import V1 as V1
from typing import Any

class Conversations(Domain):
    base_url: str = ...
    def __init__(self, twilio: Any) -> None: ...
    @property
    def v1(self): ...
    @property
    def configuration(self): ...
    @property
    def conversations(self): ...
    @property
    def credentials(self): ...
    @property
    def roles(self): ...
    @property
    def services(self): ...
    @property
    def users(self): ...
