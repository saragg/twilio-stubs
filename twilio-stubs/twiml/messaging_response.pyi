from twilio.twiml import TwiML as TwiML, format_language as format_language
from typing import Any, Optional

class MessagingResponse(TwiML):
    name: str = ...
    def __init__(self, **kwargs: Any) -> None: ...
    def message(self, body: Optional[Any] = ..., to: Optional[Any] = ..., from_: Optional[Any] = ..., action: Optional[Any] = ..., method: Optional[Any] = ..., status_callback: Optional[Any] = ..., **kwargs: Any): ...
    def redirect(self, url: Any, method: Optional[Any] = ..., **kwargs: Any): ...

class Redirect(TwiML):
    name: str = ...
    value: Any = ...
    def __init__(self, url: Any, **kwargs: Any) -> None: ...

class Message(TwiML):
    name: str = ...
    value: Any = ...
    def __init__(self, body: Optional[Any] = ..., **kwargs: Any) -> None: ...
    def body(self, message: Any, **kwargs: Any): ...
    def media(self, url: Any, **kwargs: Any): ...

class Media(TwiML):
    name: str = ...
    value: Any = ...
    def __init__(self, url: Any, **kwargs: Any) -> None: ...

class Body(TwiML):
    name: str = ...
    value: Any = ...
    def __init__(self, message: Any, **kwargs: Any) -> None: ...
