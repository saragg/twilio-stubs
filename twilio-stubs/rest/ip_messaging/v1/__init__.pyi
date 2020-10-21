from twilio.base.version import Version as Version
from twilio.rest.ip_messaging.v1.credential import CredentialList as CredentialList
from twilio.rest.ip_messaging.v1.service import ServiceList as ServiceList
from typing import Any

class V1(Version):
    version: str = ...
    def __init__(self, domain: Any) -> None: ...
    @property
    def credentials(self): ...
    @property
    def services(self): ...
