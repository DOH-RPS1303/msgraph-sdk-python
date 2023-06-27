from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .print_job_processing_state import PrintJobProcessingState
    from .print_job_state_detail import PrintJobStateDetail

@dataclass
class PrintJobStatus(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)

    # A human-readable description of the print job's current processing state. Read-only.
    description: Optional[str] = None
    # Additional details for print job state. Valid values are described in the following table. Read-only.
    details: Optional[List[PrintJobStateDetail]] = None
    # True if the job was acknowledged by a printer; false otherwise. Read-only.
    is_acquired_by_printer: Optional[bool] = None
    # The OdataType property
    odata_type: Optional[str] = None
    # The state property
    state: Optional[PrintJobProcessingState] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> PrintJobStatus:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: PrintJobStatus
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return PrintJobStatus()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .print_job_processing_state import PrintJobProcessingState
        from .print_job_state_detail import PrintJobStateDetail

        from .print_job_processing_state import PrintJobProcessingState
        from .print_job_state_detail import PrintJobStateDetail

        fields: Dict[str, Callable[[Any], None]] = {
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "details": lambda n : setattr(self, 'details', n.get_collection_of_enum_values(PrintJobStateDetail)),
            "isAcquiredByPrinter": lambda n : setattr(self, 'is_acquired_by_printer', n.get_bool_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "state": lambda n : setattr(self, 'state', n.get_enum_value(PrintJobProcessingState)),
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
        writer.write_str_value("description", self.description)
        writer.write_collection_of_enum_values("details", self.details)
        writer.write_bool_value("isAcquiredByPrinter", self.is_acquired_by_printer)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_enum_value("state", self.state)
        writer.write_additional_data_value(self.additional_data)
    

