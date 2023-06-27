from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .organizational_branding_localization import OrganizationalBrandingLocalization
    from .organizational_branding_properties import OrganizationalBrandingProperties

from .organizational_branding_properties import OrganizationalBrandingProperties

@dataclass
class OrganizationalBranding(OrganizationalBrandingProperties):
    odata_type = "#microsoft.graph.organizationalBranding"
    # Add different branding based on a locale.
    localizations: Optional[List[OrganizationalBrandingLocalization]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> OrganizationalBranding:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: OrganizationalBranding
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return OrganizationalBranding()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .organizational_branding_localization import OrganizationalBrandingLocalization
        from .organizational_branding_properties import OrganizationalBrandingProperties

        from .organizational_branding_localization import OrganizationalBrandingLocalization
        from .organizational_branding_properties import OrganizationalBrandingProperties

        fields: Dict[str, Callable[[Any], None]] = {
            "localizations": lambda n : setattr(self, 'localizations', n.get_collection_of_object_values(OrganizationalBrandingLocalization)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if not writer:
            raise TypeError("writer cannot be null.")
        super().serialize(writer)
        writer.write_collection_of_object_values("localizations", self.localizations)
    

