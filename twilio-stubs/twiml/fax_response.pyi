from twilio.twiml import TwiML as TwiML, format_language as format_language
from typing import Any, Optional

class FaxResponse(TwiML):
    name: str = ...
    def __init__(self, **kwargs: Any) -> None: ...
    def receive(self, action: Optional[Any] = ..., method: Optional[Any] = ..., media_type: Optional[Any] = ..., page_size: Optional[Any] = ..., store_media: Optional[Any] = ..., **kwargs: Any): ...

class Receive(TwiML):
    name: str = ...
    def __init__(self, **kwargs: Any) -> None: ...
