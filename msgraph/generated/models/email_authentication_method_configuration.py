from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .authentication_method_configuration import AuthenticationMethodConfiguration
    from .authentication_method_target import AuthenticationMethodTarget
    from .external_email_otp_state import ExternalEmailOtpState

from .authentication_method_configuration import AuthenticationMethodConfiguration

@dataclass
class EmailAuthenticationMethodConfiguration(AuthenticationMethodConfiguration):
    odata_type = "#microsoft.graph.emailAuthenticationMethodConfiguration"
    # Determines whether email OTP is usable by external users for authentication. Possible values are: default, enabled, disabled, unknownFutureValue. Tenants in the default state who did not use public preview will automatically have email OTP enabled beginning in October 2021.
    allow_external_id_to_use_email_otp: Optional[ExternalEmailOtpState] = None
    # A collection of groups that are enabled to use the authentication method.
    include_targets: Optional[List[AuthenticationMethodTarget]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> EmailAuthenticationMethodConfiguration:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: EmailAuthenticationMethodConfiguration
        """
        if not parse_node:
            raise TypeError("parse_node cannot be null.")
        return EmailAuthenticationMethodConfiguration()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .authentication_method_configuration import AuthenticationMethodConfiguration
        from .authentication_method_target import AuthenticationMethodTarget
        from .external_email_otp_state import ExternalEmailOtpState

        from .authentication_method_configuration import AuthenticationMethodConfiguration
        from .authentication_method_target import AuthenticationMethodTarget
        from .external_email_otp_state import ExternalEmailOtpState

        fields: Dict[str, Callable[[Any], None]] = {
            "allowExternalIdToUseEmailOtp": lambda n : setattr(self, 'allow_external_id_to_use_email_otp', n.get_enum_value(ExternalEmailOtpState)),
            "includeTargets": lambda n : setattr(self, 'include_targets', n.get_collection_of_object_values(AuthenticationMethodTarget)),
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
        writer.write_enum_value("allowExternalIdToUseEmailOtp", self.allow_external_id_to_use_email_otp)
        writer.write_collection_of_object_values("includeTargets", self.include_targets)
    

