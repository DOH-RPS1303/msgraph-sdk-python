from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .access_review_instance_decision_item_resource import AccessReviewInstanceDecisionItemResource

from .access_review_instance_decision_item_resource import AccessReviewInstanceDecisionItemResource

@dataclass
class AccessReviewInstanceDecisionItemServicePrincipalResource(AccessReviewInstanceDecisionItemResource):
    odata_type = "#microsoft.graph.accessReviewInstanceDecisionItemServicePrincipalResource"
    # The globally unique identifier of the application to which access has been granted.
    app_id: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> AccessReviewInstanceDecisionItemServicePrincipalResource:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: AccessReviewInstanceDecisionItemServicePrincipalResource
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return AccessReviewInstanceDecisionItemServicePrincipalResource()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .access_review_instance_decision_item_resource import AccessReviewInstanceDecisionItemResource

        from .access_review_instance_decision_item_resource import AccessReviewInstanceDecisionItemResource

        fields: Dict[str, Callable[[Any], None]] = {
            "appId": lambda n : setattr(self, 'app_id', n.get_str_value()),
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
        writer.write_str_value("appId", self.app_id)
    

