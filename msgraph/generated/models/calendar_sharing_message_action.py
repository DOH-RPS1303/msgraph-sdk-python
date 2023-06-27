from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .calendar_sharing_action import CalendarSharingAction
    from .calendar_sharing_action_importance import CalendarSharingActionImportance
    from .calendar_sharing_action_type import CalendarSharingActionType

@dataclass
class CalendarSharingMessageAction(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)

    # The action property
    action: Optional[CalendarSharingAction] = None
    # The actionType property
    action_type: Optional[CalendarSharingActionType] = None
    # The importance property
    importance: Optional[CalendarSharingActionImportance] = None
    # The OdataType property
    odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> CalendarSharingMessageAction:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: CalendarSharingMessageAction
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return CalendarSharingMessageAction()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .calendar_sharing_action import CalendarSharingAction
        from .calendar_sharing_action_importance import CalendarSharingActionImportance
        from .calendar_sharing_action_type import CalendarSharingActionType

        from .calendar_sharing_action import CalendarSharingAction
        from .calendar_sharing_action_importance import CalendarSharingActionImportance
        from .calendar_sharing_action_type import CalendarSharingActionType

        fields: Dict[str, Callable[[Any], None]] = {
            "action": lambda n : setattr(self, 'action', n.get_enum_value(CalendarSharingAction)),
            "actionType": lambda n : setattr(self, 'action_type', n.get_enum_value(CalendarSharingActionType)),
            "importance": lambda n : setattr(self, 'importance', n.get_enum_value(CalendarSharingActionImportance)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
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
        writer.write_enum_value("action", self.action)
        writer.write_enum_value("actionType", self.action_type)
        writer.write_enum_value("importance", self.importance)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

