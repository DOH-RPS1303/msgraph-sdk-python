from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ..site import Site
    from .data_source import DataSource

from .data_source import DataSource

@dataclass
class SiteSource(DataSource):
    odata_type = "#microsoft.graph.security.siteSource"
    # The site property
    site: Optional[Site] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> SiteSource:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parse_node: The parse node to use to read the discriminator value and create the object
        Returns: SiteSource
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return SiteSource()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from ..site import Site
        from .data_source import DataSource

        from ..site import Site
        from .data_source import DataSource

        fields: Dict[str, Callable[[Any], None]] = {
            "site": lambda n : setattr(self, 'site', n.get_object_value(Site)),
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
        writer.write_object_value("site", self.site)
    

