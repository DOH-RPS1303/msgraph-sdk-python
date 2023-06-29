from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

@dataclass
class FileDetails(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)

    # The name of the file.
    file_name: Optional[str] = None
    # The file path (location) of the file instance.
    file_path: Optional[str] = None
    # The publisher of the file.
    file_publisher: Optional[str] = None
    # The size of the file in bytes.
    file_size: Optional[int] = None
    # The certificate authority (CA) that issued the certificate.
    issuer: Optional[str] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The Sha1 cryptographic hash of the file content.
    sha1: Optional[str] = None
    # The Sha256 cryptographic hash of the file content.
    sha256: Optional[str] = None
    # The signer of the signed file.
    signer: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> FileDetails:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parse_node: The parse node to use to read the discriminator value and create the object
        Returns: FileDetails
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return FileDetails()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields: Dict[str, Callable[[Any], None]] = {
            "fileName": lambda n : setattr(self, 'file_name', n.get_str_value()),
            "filePath": lambda n : setattr(self, 'file_path', n.get_str_value()),
            "filePublisher": lambda n : setattr(self, 'file_publisher', n.get_str_value()),
            "fileSize": lambda n : setattr(self, 'file_size', n.get_int_value()),
            "issuer": lambda n : setattr(self, 'issuer', n.get_str_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "sha1": lambda n : setattr(self, 'sha1', n.get_str_value()),
            "sha256": lambda n : setattr(self, 'sha256', n.get_str_value()),
            "signer": lambda n : setattr(self, 'signer', n.get_str_value()),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if not writer:
            raise TypeError("writer cannot be null.")
        writer.write_str_value("fileName", self.file_name)
        writer.write_str_value("filePath", self.file_path)
        writer.write_str_value("filePublisher", self.file_publisher)
        writer.write_int_value("fileSize", self.file_size)
        writer.write_str_value("issuer", self.issuer)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("sha1", self.sha1)
        writer.write_str_value("sha256", self.sha256)
        writer.write_str_value("signer", self.signer)
        writer.write_additional_data_value(self.additional_data)
    

