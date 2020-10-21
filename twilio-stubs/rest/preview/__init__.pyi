from twilio.base.domain import Domain as Domain
from twilio.rest.preview.bulk_exports import BulkExports as BulkExports
from twilio.rest.preview.deployed_devices import DeployedDevices as DeployedDevices
from twilio.rest.preview.hosted_numbers import HostedNumbers as HostedNumbers
from twilio.rest.preview.marketplace import Marketplace as Marketplace
from twilio.rest.preview.sync import Sync as Sync
from twilio.rest.preview.trusted_comms import TrustedComms as TrustedComms
from twilio.rest.preview.understand import Understand as Understand
from twilio.rest.preview.wireless import Wireless as Wireless
from typing import Any

class Preview(Domain):
    base_url: str = ...
    def __init__(self, twilio: Any) -> None: ...
    @property
    def bulk_exports(self): ...
    @property
    def deployed_devices(self): ...
    @property
    def hosted_numbers(self): ...
    @property
    def marketplace(self): ...
    @property
    def sync(self): ...
    @property
    def understand(self): ...
    @property
    def wireless(self): ...
    @property
    def trusted_comms(self): ...
    @property
    def exports(self): ...
    @property
    def export_configuration(self): ...
    @property
    def fleets(self): ...
    @property
    def authorization_documents(self): ...
    @property
    def hosted_number_orders(self): ...
    @property
    def available_add_ons(self): ...
    @property
    def installed_add_ons(self): ...
    @property
    def services(self): ...
    @property
    def assistants(self): ...
    @property
    def commands(self): ...
    @property
    def rate_plans(self): ...
    @property
    def sims(self): ...
    @property
    def branded_calls(self): ...
    @property
    def branded_channels(self): ...
    @property
    def brands_information(self): ...
    @property
    def businesses(self): ...
    @property
    def cps(self): ...
    @property
    def current_calls(self): ...
    @property
    def phone_calls(self): ...
