from twilio.base.version import Version as Version
from twilio.rest.preview.bulk_exports.export import ExportList as ExportList
from twilio.rest.preview.bulk_exports.export_configuration import ExportConfigurationList as ExportConfigurationList
from typing import Any

class BulkExports(Version):
    version: str = ...
    def __init__(self, domain: Any) -> None: ...
    @property
    def exports(self): ...
    @property
    def export_configuration(self): ...
