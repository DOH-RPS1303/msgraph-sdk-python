from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.request_adapter import RequestAdapter
from kiota_abstractions.request_information import RequestInformation
from kiota_abstractions.request_option import RequestOption
from kiota_abstractions.response_handler import ResponseHandler
from kiota_abstractions.serialization import Parsable, ParsableFactory
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ........models.o_data_errors.o_data_error import ODataError
    from .get_recent_notebooks_with_include_personal_notebooks_response import GetRecentNotebooksWithIncludePersonalNotebooksResponse

class GetRecentNotebooksWithIncludePersonalNotebooksRequestBuilder():
    """
    Provides operations to call the getRecentNotebooks method.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Optional[Union[Dict[str, Any], str]] = None, include_personal_notebooks: Optional[bool] = None) -> None:
        """
        Instantiates a new GetRecentNotebooksWithIncludePersonalNotebooksRequestBuilder and sets the default values.
        Args:
            includePersonalNotebooks: Usage: includePersonalNotebooks={includePersonalNotebooks}
            pathParameters: The raw url or the Url template parameters for the request.
            requestAdapter: The request adapter to use to execute the requests.
        """
        if not path_parameters:
            raise TypeError("path_parameters cannot be null.")
        if not request_adapter:
            raise TypeError("request_adapter cannot be null.")
        # Url template to use to build the URL for the current request builder
        self.url_template: str = "{+baseurl}/groups/{group%2Did}/sites/{site%2Did}/onenote/notebooks/getRecentNotebooks(includePersonalNotebooks={includePersonalNotebooks}){?%24top,%24skip,%24search,%24filter,%24count}"

        url_tpl_params = get_path_parameters(path_parameters)
        url_tpl_params[""] = includePersonalNotebooks
        self.path_parameters = url_tpl_params
        self.request_adapter = request_adapter
    
    async def get(self,request_configuration: Optional[GetRecentNotebooksWithIncludePersonalNotebooksRequestBuilderGetRequestConfiguration] = None) -> Optional[GetRecentNotebooksWithIncludePersonalNotebooksResponse]:
        """
        Invoke function getRecentNotebooks
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[GetRecentNotebooksWithIncludePersonalNotebooksResponse]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from ........models.o_data_errors.o_data_error import ODataError

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": ODataError,
            "5XX": ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .get_recent_notebooks_with_include_personal_notebooks_response import GetRecentNotebooksWithIncludePersonalNotebooksResponse

        return await self.request_adapter.send_async(request_info, GetRecentNotebooksWithIncludePersonalNotebooksResponse, error_mapping)
    
    def to_get_request_information(self,request_configuration: Optional[GetRecentNotebooksWithIncludePersonalNotebooksRequestBuilderGetRequestConfiguration] = None) -> RequestInformation:
        """
        Invoke function getRecentNotebooks
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation()
        request_info.url_template = self.url_template
        request_info.path_parameters = self.path_parameters
        request_info.http_method = Method.GET
        request_info.headers["Accept"] = ["application/json"]
        if request_configuration:
            request_info.add_request_headers(request_configuration.headers)
            request_info.set_query_string_parameters_from_raw_object(request_configuration.query_parameters)
            request_info.add_request_options(request_configuration.options)
        return request_info
    
    @dataclass
    class GetRecentNotebooksWithIncludePersonalNotebooksRequestBuilderGetQueryParameters():
        """
        Invoke function getRecentNotebooks
        """
        def get_query_parameter(self,original_name: Optional[str] = None) -> str:
            """
            Maps the query parameters names to their encoded names for the URI template parsing.
            Args:
                originalName: The original query parameter name in the class.
            Returns: str
            """
            if not original_name:
                raise TypeError("original_name cannot be null.")
            if original_name == "count":
                return "%24count"
            if original_name == "filter":
                return "%24filter"
            if original_name == "search":
                return "%24search"
            if original_name == "skip":
                return "%24skip"
            if original_name == "top":
                return "%24top"
            return original_name
        
        # Include count of items
        count: Optional[bool] = None

        # Filter items by property values
        filter: Optional[str] = None

        # Search items by search phrases
        search: Optional[str] = None

        # Skip the first n items
        skip: Optional[int] = None

        # Show only the first n items
        top: Optional[int] = None

    
    @dataclass
    class GetRecentNotebooksWithIncludePersonalNotebooksRequestBuilderGetRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, Union[str, List[str]]]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

        # Request query parameters
        query_parameters: Optional[GetRecentNotebooksWithIncludePersonalNotebooksRequestBuilder.GetRecentNotebooksWithIncludePersonalNotebooksRequestBuilderGetQueryParameters] = None

    

