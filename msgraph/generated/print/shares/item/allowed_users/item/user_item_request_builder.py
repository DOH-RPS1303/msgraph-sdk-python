from __future__ import annotations
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.request_adapter import RequestAdapter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .mailbox_settings import mailbox_settings_request_builder
    from .ref import ref_request_builder

class UserItemRequestBuilder():
    """
    Builds and executes requests for operations under /print/shares/{printerShare-id}/allowedUsers/{user-id}
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Optional[Union[Dict[str, Any], str]] = None) -> None:
        """
        Instantiates a new UserItemRequestBuilder and sets the default values.
        Args:
            pathParameters: The raw url or the Url template parameters for the request.
            requestAdapter: The request adapter to use to execute the requests.
        """
        if path_parameters is None:
            raise Exception("path_parameters cannot be undefined")
        if request_adapter is None:
            raise Exception("request_adapter cannot be undefined")
        # Url template to use to build the URL for the current request builder
        self.url_template: str = "{+baseurl}/print/shares/{printerShare%2Did}/allowedUsers/{user%2Did}"

        url_tpl_params = get_path_parameters(path_parameters)
        self.path_parameters = url_tpl_params
        self.request_adapter = request_adapter
    
    @property
    def mailbox_settings(self) -> mailbox_settings_request_builder.MailboxSettingsRequestBuilder:
        """
        The mailboxSettings property
        """
        from .mailbox_settings import mailbox_settings_request_builder

        return mailbox_settings_request_builder.MailboxSettingsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def ref(self) -> ref_request_builder.RefRequestBuilder:
        """
        Provides operations to manage the collection of print entities.
        """
        from .ref import ref_request_builder

        return ref_request_builder.RefRequestBuilder(self.request_adapter, self.path_parameters)
    

