from twilio.base.domain import Domain as Domain
from twilio.rest.api.v2010 import V2010 as V2010
from typing import Any

class Api(Domain):
    base_url: str = ...
    def __init__(self, twilio: Any) -> None: ...

    @property
    def v2010(self) -> V2010: ...

    @property
    def account(self): ...
    @property
    def accounts(self): ...
    @property
    def addresses(self): ...
    @property
    def applications(self): ...
    @property
    def authorized_connect_apps(self): ...
    @property
    def available_phone_numbers(self): ...
    @property
    def balance(self): ...
    @property
    def calls(self): ...
    @property
    def conferences(self): ...
    @property
    def connect_apps(self): ...
    @property
    def incoming_phone_numbers(self): ...
    @property
    def keys(self): ...
    @property
    def messages(self): ...
    @property
    def new_keys(self): ...
    @property
    def new_signing_keys(self): ...
    @property
    def notifications(self): ...
    @property
    def outgoing_caller_ids(self): ...
    @property
    def queues(self): ...
    @property
    def recordings(self): ...
    @property
    def signing_keys(self): ...
    @property
    def sip(self): ...
    @property
    def short_codes(self): ...
    @property
    def tokens(self): ...
    @property
    def transcriptions(self): ...
    @property
    def usage(self): ...
    @property
    def validation_requests(self): ...
