from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .json import Json
    from .managed_app_status import ManagedAppStatus

from .managed_app_status import ManagedAppStatus

@dataclass
class ManagedAppStatusRaw(ManagedAppStatus):
    odata_type = "#microsoft.graph.managedAppStatusRaw"
    # Status report content.
    content: Optional[Json] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ManagedAppStatusRaw:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ManagedAppStatusRaw
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return ManagedAppStatusRaw()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .json import Json
        from .managed_app_status import ManagedAppStatus

        from .json import Json
        from .managed_app_status import ManagedAppStatus

        fields: Dict[str, Callable[[Any], None]] = {
            "content": lambda n : setattr(self, 'content', n.get_object_value(Json)),
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
        writer.write_object_value("content", self.content)
    

