from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .risk_detection import RiskDetection
    from .risky_service_principal import RiskyServicePrincipal
    from .risky_user import RiskyUser
    from .service_principal_risk_detection import ServicePrincipalRiskDetection

@dataclass
class IdentityProtectionRoot(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: Dict[str, Any] = field(default_factory=dict)

    # The OdataType property
    odata_type: Optional[str] = None
    # Risk detection in Azure AD Identity Protection and the associated information about the detection.
    risk_detections: Optional[List[RiskDetection]] = None
    # Azure AD service principals that are at risk.
    risky_service_principals: Optional[List[RiskyServicePrincipal]] = None
    # Users that are flagged as at-risk by Azure AD Identity Protection.
    risky_users: Optional[List[RiskyUser]] = None
    # Represents information about detected at-risk service principals in an Azure AD tenant.
    service_principal_risk_detections: Optional[List[ServicePrincipalRiskDetection]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> IdentityProtectionRoot:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parse_node: The parse node to use to read the discriminator value and create the object
        Returns: IdentityProtectionRoot
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return IdentityProtectionRoot()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .risk_detection import RiskDetection
        from .risky_service_principal import RiskyServicePrincipal
        from .risky_user import RiskyUser
        from .service_principal_risk_detection import ServicePrincipalRiskDetection

        from .risk_detection import RiskDetection
        from .risky_service_principal import RiskyServicePrincipal
        from .risky_user import RiskyUser
        from .service_principal_risk_detection import ServicePrincipalRiskDetection

        fields: Dict[str, Callable[[Any], None]] = {
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "riskDetections": lambda n : setattr(self, 'risk_detections', n.get_collection_of_object_values(RiskDetection)),
            "riskyServicePrincipals": lambda n : setattr(self, 'risky_service_principals', n.get_collection_of_object_values(RiskyServicePrincipal)),
            "riskyUsers": lambda n : setattr(self, 'risky_users', n.get_collection_of_object_values(RiskyUser)),
            "servicePrincipalRiskDetections": lambda n : setattr(self, 'service_principal_risk_detections', n.get_collection_of_object_values(ServicePrincipalRiskDetection)),
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
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_collection_of_object_values("riskDetections", self.risk_detections)
        writer.write_collection_of_object_values("riskyServicePrincipals", self.risky_service_principals)
        writer.write_collection_of_object_values("riskyUsers", self.risky_users)
        writer.write_collection_of_object_values("servicePrincipalRiskDetections", self.service_principal_risk_detections)
        writer.write_additional_data_value(self.additional_data)
    

