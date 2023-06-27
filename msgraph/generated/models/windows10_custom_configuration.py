from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .device_configuration import DeviceConfiguration
    from .oma_setting import OmaSetting

from .device_configuration import DeviceConfiguration

@dataclass
class Windows10CustomConfiguration(DeviceConfiguration):
    odata_type = "#microsoft.graph.windows10CustomConfiguration"
    # OMA settings. This collection can contain a maximum of 1000 elements.
    oma_settings: Optional[List[OmaSetting]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> Windows10CustomConfiguration:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: Windows10CustomConfiguration
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return Windows10CustomConfiguration()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .device_configuration import DeviceConfiguration
        from .oma_setting import OmaSetting

        from .device_configuration import DeviceConfiguration
        from .oma_setting import OmaSetting

        fields: Dict[str, Callable[[Any], None]] = {
            "omaSettings": lambda n : setattr(self, 'oma_settings', n.get_collection_of_object_values(OmaSetting)),
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
        writer.write_collection_of_object_values("omaSettings", self.oma_settings)
    

