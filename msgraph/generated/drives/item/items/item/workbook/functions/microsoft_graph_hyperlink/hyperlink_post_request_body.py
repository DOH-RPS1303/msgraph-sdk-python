from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from kiota_abstractions.utils import lazy_import
from typing import Any, Callable, Dict, List, Optional, Union

json = lazy_import('msgraph.generated.models.json')

class HyperlinkPostRequestBody(AdditionalDataHolder, Parsable):
    @property
    def additional_data(self,) -> Dict[str, Any]:
        """
        Gets the additionalData property value. Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        Returns: Dict[str, Any]
        """
        return self._additional_data
    
    @additional_data.setter
    def additional_data(self,value: Dict[str, Any]) -> None:
        """
        Sets the additionalData property value. Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        Args:
            value: Value to set for the AdditionalData property.
        """
        self._additional_data = value
    
    def __init__(self,) -> None:
        """
        Instantiates a new hyperlinkPostRequestBody and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The friendlyName property
        self._friendly_name: Optional[json.Json] = None
        # The linkLocation property
        self._link_location: Optional[json.Json] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> HyperlinkPostRequestBody:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: HyperlinkPostRequestBody
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return HyperlinkPostRequestBody()
    
    @property
    def friendly_name(self,) -> Optional[json.Json]:
        """
        Gets the friendlyName property value. The friendlyName property
        Returns: Optional[json.Json]
        """
        return self._friendly_name
    
    @friendly_name.setter
    def friendly_name(self,value: Optional[json.Json] = None) -> None:
        """
        Sets the friendlyName property value. The friendlyName property
        Args:
            value: Value to set for the friendly_name property.
        """
        self._friendly_name = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields = {
            "friendlyName": lambda n : setattr(self, 'friendly_name', n.get_object_value(json.Json)),
            "linkLocation": lambda n : setattr(self, 'link_location', n.get_object_value(json.Json)),
        }
        return fields
    
    @property
    def link_location(self,) -> Optional[json.Json]:
        """
        Gets the linkLocation property value. The linkLocation property
        Returns: Optional[json.Json]
        """
        return self._link_location
    
    @link_location.setter
    def link_location(self,value: Optional[json.Json] = None) -> None:
        """
        Sets the linkLocation property value. The linkLocation property
        Args:
            value: Value to set for the link_location property.
        """
        self._link_location = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_object_value("friendlyName", self.friendly_name)
        writer.write_object_value("linkLocation", self.link_location)
        writer.write_additional_data_value(self.additional_data)
    
