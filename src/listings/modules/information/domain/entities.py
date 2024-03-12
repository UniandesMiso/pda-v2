from dataclasses import dataclass

from listings.seedwork.domain.entities import Listing
from listings.seedwork.domain.mixins import ValidateRules
from listings.modules.information.domain.events import PropertyProcessed


@dataclass
class GenericListing(Listing, ValidateRules):

    def process_properties(self):
        for property in self.properties:
            event = PropertyProcessed(
                property_id=property.id,
                width=property.width,
                length=property.length,
            )
            self.add_event(event)
