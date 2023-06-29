from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .agreement_file_localization import AgreementFileLocalization
    from .agreement_file_properties import AgreementFileProperties

from .agreement_file_properties import AgreementFileProperties

@dataclass
class AgreementFile(AgreementFileProperties):
    # The localized version of the terms of use agreement files attached to the agreement.
    localizations: Optional[List[AgreementFileLocalization]] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> AgreementFile:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parse_node: The parse node to use to read the discriminator value and create the object
        Returns: AgreementFile
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return AgreementFile()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .agreement_file_localization import AgreementFileLocalization
        from .agreement_file_properties import AgreementFileProperties

        from .agreement_file_localization import AgreementFileLocalization
        from .agreement_file_properties import AgreementFileProperties

        fields: Dict[str, Callable[[Any], None]] = {
            "localizations": lambda n : setattr(self, 'localizations', n.get_collection_of_object_values(AgreementFileLocalization)),
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
    

