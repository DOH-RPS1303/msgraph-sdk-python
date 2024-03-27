from enum import Enum

class CloudPcOnPremisesConnectionHealthCheckErrorType(str, Enum):
    DnsCheckFqdnNotFound = "dnsCheckFqdnNotFound",
    DnsCheckNameWithInvalidCharacter = "dnsCheckNameWithInvalidCharacter",
    DnsCheckUnknownError = "dnsCheckUnknownError",
    AdJoinCheckFqdnNotFound = "adJoinCheckFqdnNotFound",
    AdJoinCheckIncorrectCredentials = "adJoinCheckIncorrectCredentials",
    AdJoinCheckOrganizationalUnitNotFound = "adJoinCheckOrganizationalUnitNotFound",
    AdJoinCheckOrganizationalUnitIncorrectFormat = "adJoinCheckOrganizationalUnitIncorrectFormat",
    AdJoinCheckComputerObjectAlreadyExists = "adJoinCheckComputerObjectAlreadyExists",
    AdJoinCheckAccessDenied = "adJoinCheckAccessDenied",
    AdJoinCheckCredentialsExpired = "adJoinCheckCredentialsExpired",
    AdJoinCheckAccountLockedOrDisabled = "adJoinCheckAccountLockedOrDisabled",
    AdJoinCheckAccountQuotaExceeded = "adJoinCheckAccountQuotaExceeded",
    AdJoinCheckServerNotOperational = "adJoinCheckServerNotOperational",
    AdJoinCheckUnknownError = "adJoinCheckUnknownError",
    EndpointConnectivityCheckCloudPcUrlNotAllowListed = "endpointConnectivityCheckCloudPcUrlNotAllowListed",
    EndpointConnectivityCheckWVDUrlNotAllowListed = "endpointConnectivityCheckWVDUrlNotAllowListed",
    EndpointConnectivityCheckIntuneUrlNotAllowListed = "endpointConnectivityCheckIntuneUrlNotAllowListed",
    EndpointConnectivityCheckAzureADUrlNotAllowListed = "endpointConnectivityCheckAzureADUrlNotAllowListed",
    EndpointConnectivityCheckLocaleUrlNotAllowListed = "endpointConnectivityCheckLocaleUrlNotAllowListed",
    EndpointConnectivityCheckUnknownError = "endpointConnectivityCheckUnknownError",
    AzureAdDeviceSyncCheckDeviceNotFound = "azureAdDeviceSyncCheckDeviceNotFound",
    AzureAdDeviceSyncCheckLongSyncCircle = "azureAdDeviceSyncCheckLongSyncCircle",
    AzureAdDeviceSyncCheckConnectDisabled = "azureAdDeviceSyncCheckConnectDisabled",
    AzureAdDeviceSyncCheckDurationExceeded = "azureAdDeviceSyncCheckDurationExceeded",
    AzureAdDeviceSyncCheckScpNotConfigured = "azureAdDeviceSyncCheckScpNotConfigured",
    AzureAdDeviceSyncCheckTransientServiceError = "azureAdDeviceSyncCheckTransientServiceError",
    AzureAdDeviceSyncCheckUnknownError = "azureAdDeviceSyncCheckUnknownError",
    ResourceAvailabilityCheckNoSubnetIP = "resourceAvailabilityCheckNoSubnetIP",
    ResourceAvailabilityCheckSubscriptionDisabled = "resourceAvailabilityCheckSubscriptionDisabled",
    ResourceAvailabilityCheckAzurePolicyViolation = "resourceAvailabilityCheckAzurePolicyViolation",
    ResourceAvailabilityCheckSubscriptionNotFound = "resourceAvailabilityCheckSubscriptionNotFound",
    ResourceAvailabilityCheckSubscriptionTransferred = "resourceAvailabilityCheckSubscriptionTransferred",
    ResourceAvailabilityCheckGeneralSubscriptionError = "resourceAvailabilityCheckGeneralSubscriptionError",
    ResourceAvailabilityCheckUnsupportedVNetRegion = "resourceAvailabilityCheckUnsupportedVNetRegion",
    ResourceAvailabilityCheckResourceGroupInvalid = "resourceAvailabilityCheckResourceGroupInvalid",
    ResourceAvailabilityCheckVNetInvalid = "resourceAvailabilityCheckVNetInvalid",
    ResourceAvailabilityCheckSubnetInvalid = "resourceAvailabilityCheckSubnetInvalid",
    ResourceAvailabilityCheckResourceGroupBeingDeleted = "resourceAvailabilityCheckResourceGroupBeingDeleted",
    ResourceAvailabilityCheckVNetBeingMoved = "resourceAvailabilityCheckVNetBeingMoved",
    ResourceAvailabilityCheckSubnetDelegationFailed = "resourceAvailabilityCheckSubnetDelegationFailed",
    ResourceAvailabilityCheckSubnetWithExternalResources = "resourceAvailabilityCheckSubnetWithExternalResources",
    ResourceAvailabilityCheckResourceGroupLockedForReadonly = "resourceAvailabilityCheckResourceGroupLockedForReadonly",
    ResourceAvailabilityCheckResourceGroupLockedForDelete = "resourceAvailabilityCheckResourceGroupLockedForDelete",
    ResourceAvailabilityCheckNoIntuneReaderRoleError = "resourceAvailabilityCheckNoIntuneReaderRoleError",
    ResourceAvailabilityCheckIntuneDefaultWindowsRestrictionViolation = "resourceAvailabilityCheckIntuneDefaultWindowsRestrictionViolation",
    ResourceAvailabilityCheckIntuneCustomWindowsRestrictionViolation = "resourceAvailabilityCheckIntuneCustomWindowsRestrictionViolation",
    ResourceAvailabilityCheckDeploymentQuotaLimitReached = "resourceAvailabilityCheckDeploymentQuotaLimitReached",
    ResourceAvailabilityCheckTransientServiceError = "resourceAvailabilityCheckTransientServiceError",
    ResourceAvailabilityCheckUnknownError = "resourceAvailabilityCheckUnknownError",
    PermissionCheckNoSubscriptionReaderRole = "permissionCheckNoSubscriptionReaderRole",
    PermissionCheckNoResourceGroupOwnerRole = "permissionCheckNoResourceGroupOwnerRole",
    PermissionCheckNoVNetContributorRole = "permissionCheckNoVNetContributorRole",
    PermissionCheckNoResourceGroupNetworkContributorRole = "permissionCheckNoResourceGroupNetworkContributorRole",
    PermissionCheckNoWindows365NetworkUserRole = "permissionCheckNoWindows365NetworkUserRole",
    PermissionCheckNoWindows365NetworkInterfaceContributorRole = "permissionCheckNoWindows365NetworkInterfaceContributorRole",
    PermissionCheckTransientServiceError = "permissionCheckTransientServiceError",
    PermissionCheckUnknownError = "permissionCheckUnknownError",
    UdpConnectivityCheckStunUrlNotAllowListed = "udpConnectivityCheckStunUrlNotAllowListed",
    UdpConnectivityCheckTurnUrlNotAllowListed = "udpConnectivityCheckTurnUrlNotAllowListed",
    UdpConnectivityCheckUrlsNotAllowListed = "udpConnectivityCheckUrlsNotAllowListed",
    UdpConnectivityCheckUnknownError = "udpConnectivityCheckUnknownError",
    InternalServerErrorDeploymentCanceled = "internalServerErrorDeploymentCanceled",
    InternalServerErrorAllocateResourceFailed = "internalServerErrorAllocateResourceFailed",
    InternalServerErrorVMDeploymentTimeout = "internalServerErrorVMDeploymentTimeout",
    InternalServerErrorUnableToRunDscScript = "internalServerErrorUnableToRunDscScript",
    SsoCheckKerberosConfigurationError = "ssoCheckKerberosConfigurationError",
    InternalServerUnknownError = "internalServerUnknownError",
    UnknownFutureValue = "unknownFutureValue",
