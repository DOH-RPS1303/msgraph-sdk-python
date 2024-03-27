from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.request_adapter import RequestAdapter
from kiota_abstractions.request_information import RequestInformation
from kiota_abstractions.request_option import RequestOption
from kiota_abstractions.serialization import Parsable, ParsableFactory
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .....models.cloud_p_c import CloudPC
    from .....models.o_data_errors.o_data_error import ODataError
    from .end_grace_period.end_grace_period_request_builder import EndGracePeriodRequestBuilder
    from .reboot.reboot_request_builder import RebootRequestBuilder
    from .rename.rename_request_builder import RenameRequestBuilder
    from .restore.restore_request_builder import RestoreRequestBuilder
    from .troubleshoot.troubleshoot_request_builder import TroubleshootRequestBuilder

class CloudPCItemRequestBuilder(BaseRequestBuilder):
    """
    Provides operations to manage the cloudPCs property of the microsoft.graph.virtualEndpoint entity.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, Dict[str, Any]]) -> None:
        """
        Instantiates a new CloudPCItemRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/deviceManagement/virtualEndpoint/cloudPCs/{cloudPC%2Did}{?%24expand,%24select}", path_parameters)
    
    async def delete(self,request_configuration: Optional[CloudPCItemRequestBuilderDeleteRequestConfiguration] = None) -> None:
        """
        Delete navigation property cloudPCs for deviceManagement
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: None
        """
        request_info = self.to_delete_request_information(
            request_configuration
        )
        from .....models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, ParsableFactory] = {
            "XXX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_no_response_content_async(request_info, error_mapping)
    
    async def get(self,request_configuration: Optional[CloudPCItemRequestBuilderGetRequestConfiguration] = None) -> Optional[CloudPC]:
        """
        Get cloudPCs from deviceManagement
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[CloudPC]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from .....models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, ParsableFactory] = {
            "XXX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .....models.cloud_p_c import CloudPC

        return await self.request_adapter.send_async(request_info, CloudPC, error_mapping)
    
    async def patch(self,body: Optional[CloudPC] = None, request_configuration: Optional[CloudPCItemRequestBuilderPatchRequestConfiguration] = None) -> Optional[CloudPC]:
        """
        Update the navigation property cloudPCs in deviceManagement
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[CloudPC]
        """
        if not body:
            raise TypeError("body cannot be null.")
        request_info = self.to_patch_request_information(
            body, request_configuration
        )
        from .....models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, ParsableFactory] = {
            "XXX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .....models.cloud_p_c import CloudPC

        return await self.request_adapter.send_async(request_info, CloudPC, error_mapping)
    
    def to_delete_request_information(self,request_configuration: Optional[CloudPCItemRequestBuilderDeleteRequestConfiguration] = None) -> RequestInformation:
        """
        Delete navigation property cloudPCs for deviceManagement
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.DELETE, '{+baseurl}/deviceManagement/virtualEndpoint/cloudPCs/{cloudPC%2Did}', self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_get_request_information(self,request_configuration: Optional[CloudPCItemRequestBuilderGetRequestConfiguration] = None) -> RequestInformation:
        """
        Get cloudPCs from deviceManagement
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_patch_request_information(self,body: Optional[CloudPC] = None, request_configuration: Optional[CloudPCItemRequestBuilderPatchRequestConfiguration] = None) -> RequestInformation:
        """
        Update the navigation property cloudPCs in deviceManagement
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        if not body:
            raise TypeError("body cannot be null.")
        request_info = RequestInformation(Method.PATCH, '{+baseurl}/deviceManagement/virtualEndpoint/cloudPCs/{cloudPC%2Did}', self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        request_info.set_content_from_parsable(self.request_adapter, "application/json", body)
        return request_info
    
    def with_url(self,raw_url: Optional[str] = None) -> CloudPCItemRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: CloudPCItemRequestBuilder
        """
        if not raw_url:
            raise TypeError("raw_url cannot be null.")
        return CloudPCItemRequestBuilder(self.request_adapter, raw_url)
    
    @property
    def end_grace_period(self) -> EndGracePeriodRequestBuilder:
        """
        Provides operations to call the endGracePeriod method.
        """
        from .end_grace_period.end_grace_period_request_builder import EndGracePeriodRequestBuilder

        return EndGracePeriodRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def reboot(self) -> RebootRequestBuilder:
        """
        Provides operations to call the reboot method.
        """
        from .reboot.reboot_request_builder import RebootRequestBuilder

        return RebootRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def rename(self) -> RenameRequestBuilder:
        """
        Provides operations to call the rename method.
        """
        from .rename.rename_request_builder import RenameRequestBuilder

        return RenameRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def restore(self) -> RestoreRequestBuilder:
        """
        Provides operations to call the restore method.
        """
        from .restore.restore_request_builder import RestoreRequestBuilder

        return RestoreRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def troubleshoot(self) -> TroubleshootRequestBuilder:
        """
        Provides operations to call the troubleshoot method.
        """
        from .troubleshoot.troubleshoot_request_builder import TroubleshootRequestBuilder

        return TroubleshootRequestBuilder(self.request_adapter, self.path_parameters)
    
    from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

    @dataclass
    class CloudPCItemRequestBuilderDeleteRequestConfiguration(BaseRequestConfiguration):
        from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
    
    @dataclass
    class CloudPCItemRequestBuilderGetQueryParameters():
        """
        Get cloudPCs from deviceManagement
        """
        def get_query_parameter(self,original_name: Optional[str] = None) -> str:
            """
            Maps the query parameters names to their encoded names for the URI template parsing.
            param original_name: The original query parameter name in the class.
            Returns: str
            """
            if not original_name:
                raise TypeError("original_name cannot be null.")
            if original_name == "expand":
                return "%24expand"
            if original_name == "select":
                return "%24select"
            return original_name
        
        # Expand related entities
        expand: Optional[List[str]] = None

        # Select properties to be returned
        select: Optional[List[str]] = None

    
    from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

    @dataclass
    class CloudPCItemRequestBuilderGetRequestConfiguration(BaseRequestConfiguration):
        from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request query parameters
        query_parameters: Optional[CloudPCItemRequestBuilder.CloudPCItemRequestBuilderGetQueryParameters] = None

    
    from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

    @dataclass
    class CloudPCItemRequestBuilderPatchRequestConfiguration(BaseRequestConfiguration):
        from kiota_abstractions.base_request_configuration import BaseRequestConfiguration

        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
    
