from twilio.base.version import Version as Version
from twilio.rest.preview.sync.service import ServiceList as ServiceList
from typing import Any

class Sync(Version):
    version: str = ...
    def __init__(self, domain: Any) -> None: ...
    @property
    def services(self): ...
