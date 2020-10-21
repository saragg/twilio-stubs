from twilio.jwt import Jwt as Jwt
from typing import Any, Optional

class TaskRouterCapabilityToken(Jwt):
    VERSION: str = ...
    DOMAIN: str = ...
    EVENTS_BASE_URL: str = ...
    account_sid: Any = ...
    auth_token: Any = ...
    workspace_sid: Any = ...
    channel_id: Any = ...
    policies: Any = ...
    def __init__(self, account_sid: Any, auth_token: Any, workspace_sid: Any, channel_id: Any, **kwargs: Any) -> None: ...
    @property
    def workspace_url(self): ...
    @property
    def resource_url(self) -> None: ...
    @property
    def channel_prefix(self) -> None: ...
    def allow_fetch_self(self) -> None: ...
    def allow_update_self(self) -> None: ...
    def allow_delete_self(self) -> None: ...
    def allow_fetch_subresources(self) -> None: ...
    def allow_update_subresources(self) -> None: ...
    def allow_delete_subresources(self) -> None: ...
    def allow_web_sockets(self, channel_id: Optional[Any] = ...) -> None: ...
