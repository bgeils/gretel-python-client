"""

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 0.0.1
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from gretel_client.rest_v1.api_client import ApiClient
from gretel_client.rest_v1.api_client import Endpoint as _Endpoint
from gretel_client.rest_v1.model.list_models_response import ListModelsResponse
from gretel_client.rest_v1.model.model import Model
from gretel_client.rest_v1.model.model_run import ModelRun
from gretel_client.rest_v1.model.search_model_runs_response import (
    SearchModelRunsResponse,
)
from gretel_client.rest_v1.model.status import Status
from gretel_client.rest_v1.model.update_model_run_status_request import (
    UpdateModelRunStatusRequest,
)
from gretel_client.rest_v1.model_utils import (  # noqa: F401
    check_allowed_values,
    check_validations,
    date,
    datetime,
    file_type,
    none_type,
    validate_and_convert_types,
)


class ModelsApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

        def __create_model(self, model, **kwargs):
            """create_model  # noqa: E501

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.create_model(model, async_req=True)
            >>> result = thread.get()

            Args:
                model (Model):

            Keyword Args:
                _return_http_data_only (bool): response data without head status
                    code and headers. Default is True.
                _preload_content (bool): if False, the urllib3.HTTPResponse object
                    will be returned without reading/decoding response data.
                    Default is True.
                _request_timeout (float/tuple): timeout setting for this request. If one
                    number provided, it will be total request timeout. It can also
                    be a pair (tuple) of (connection, read) timeouts.
                    Default is None.
                _check_input_type (bool): specifies if type checking
                    should be done one the data sent to the server.
                    Default is True.
                _check_return_type (bool): specifies if type checking
                    should be done one the data received from the server.
                    Default is True.
                _host_index (int/None): specifies the index of the server
                    that we want to use.
                    Default is read from the configuration.
                async_req (bool): execute request asynchronously

            Returns:
                Model
                    If the method is called asynchronously, returns the request
                    thread.
            """
            kwargs["async_req"] = kwargs.get("async_req", False)
            kwargs["_return_http_data_only"] = kwargs.get(
                "_return_http_data_only", True
            )
            kwargs["_preload_content"] = kwargs.get("_preload_content", True)
            kwargs["_request_timeout"] = kwargs.get("_request_timeout", None)
            kwargs["_check_input_type"] = kwargs.get("_check_input_type", True)
            kwargs["_check_return_type"] = kwargs.get("_check_return_type", True)
            kwargs["_host_index"] = kwargs.get("_host_index")
            kwargs["model"] = model
            return self.call_with_http_info(**kwargs)

        self.create_model = _Endpoint(
            settings={
                "response_type": (Model,),
                "auth": [],
                "endpoint_path": "/v1/models",
                "operation_id": "create_model",
                "http_method": "POST",
                "servers": None,
            },
            params_map={
                "all": [
                    "model",
                ],
                "required": [
                    "model",
                ],
                "nullable": [],
                "enum": [],
                "validation": [],
            },
            root_map={
                "validations": {},
                "allowed_values": {},
                "openapi_types": {
                    "model": (Model,),
                },
                "attribute_map": {},
                "location_map": {
                    "model": "body",
                },
                "collection_format_map": {},
            },
            headers_map={
                "accept": ["application/json"],
                "content_type": ["application/json"],
            },
            api_client=api_client,
            callable=__create_model,
        )

        def __create_model_run(self, model_run, **kwargs):
            """create_model_run  # noqa: E501

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.create_model_run(model_run, async_req=True)
            >>> result = thread.get()

            Args:
                model_run (ModelRun):

            Keyword Args:
                _return_http_data_only (bool): response data without head status
                    code and headers. Default is True.
                _preload_content (bool): if False, the urllib3.HTTPResponse object
                    will be returned without reading/decoding response data.
                    Default is True.
                _request_timeout (float/tuple): timeout setting for this request. If one
                    number provided, it will be total request timeout. It can also
                    be a pair (tuple) of (connection, read) timeouts.
                    Default is None.
                _check_input_type (bool): specifies if type checking
                    should be done one the data sent to the server.
                    Default is True.
                _check_return_type (bool): specifies if type checking
                    should be done one the data received from the server.
                    Default is True.
                _host_index (int/None): specifies the index of the server
                    that we want to use.
                    Default is read from the configuration.
                async_req (bool): execute request asynchronously

            Returns:
                ModelRun
                    If the method is called asynchronously, returns the request
                    thread.
            """
            kwargs["async_req"] = kwargs.get("async_req", False)
            kwargs["_return_http_data_only"] = kwargs.get(
                "_return_http_data_only", True
            )
            kwargs["_preload_content"] = kwargs.get("_preload_content", True)
            kwargs["_request_timeout"] = kwargs.get("_request_timeout", None)
            kwargs["_check_input_type"] = kwargs.get("_check_input_type", True)
            kwargs["_check_return_type"] = kwargs.get("_check_return_type", True)
            kwargs["_host_index"] = kwargs.get("_host_index")
            kwargs["model_run"] = model_run
            return self.call_with_http_info(**kwargs)

        self.create_model_run = _Endpoint(
            settings={
                "response_type": (ModelRun,),
                "auth": [],
                "endpoint_path": "/v1/models/runs",
                "operation_id": "create_model_run",
                "http_method": "POST",
                "servers": None,
            },
            params_map={
                "all": [
                    "model_run",
                ],
                "required": [
                    "model_run",
                ],
                "nullable": [],
                "enum": [],
                "validation": [],
            },
            root_map={
                "validations": {},
                "allowed_values": {},
                "openapi_types": {
                    "model_run": (ModelRun,),
                },
                "attribute_map": {},
                "location_map": {
                    "model_run": "body",
                },
                "collection_format_map": {},
            },
            headers_map={
                "accept": ["application/json"],
                "content_type": ["application/json"],
            },
            api_client=api_client,
            callable=__create_model_run,
        )

        def __delete_model(self, model_id, **kwargs):
            """delete_model  # noqa: E501

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.delete_model(model_id, async_req=True)
            >>> result = thread.get()

            Args:
                model_id (str):

            Keyword Args:
                _return_http_data_only (bool): response data without head status
                    code and headers. Default is True.
                _preload_content (bool): if False, the urllib3.HTTPResponse object
                    will be returned without reading/decoding response data.
                    Default is True.
                _request_timeout (float/tuple): timeout setting for this request. If one
                    number provided, it will be total request timeout. It can also
                    be a pair (tuple) of (connection, read) timeouts.
                    Default is None.
                _check_input_type (bool): specifies if type checking
                    should be done one the data sent to the server.
                    Default is True.
                _check_return_type (bool): specifies if type checking
                    should be done one the data received from the server.
                    Default is True.
                _host_index (int/None): specifies the index of the server
                    that we want to use.
                    Default is read from the configuration.
                async_req (bool): execute request asynchronously

            Returns:
                None
                    If the method is called asynchronously, returns the request
                    thread.
            """
            kwargs["async_req"] = kwargs.get("async_req", False)
            kwargs["_return_http_data_only"] = kwargs.get(
                "_return_http_data_only", True
            )
            kwargs["_preload_content"] = kwargs.get("_preload_content", True)
            kwargs["_request_timeout"] = kwargs.get("_request_timeout", None)
            kwargs["_check_input_type"] = kwargs.get("_check_input_type", True)
            kwargs["_check_return_type"] = kwargs.get("_check_return_type", True)
            kwargs["_host_index"] = kwargs.get("_host_index")
            kwargs["model_id"] = model_id
            return self.call_with_http_info(**kwargs)

        self.delete_model = _Endpoint(
            settings={
                "response_type": None,
                "auth": [],
                "endpoint_path": "/v1/models/{model_id}",
                "operation_id": "delete_model",
                "http_method": "DELETE",
                "servers": None,
            },
            params_map={
                "all": [
                    "model_id",
                ],
                "required": [
                    "model_id",
                ],
                "nullable": [],
                "enum": [],
                "validation": [],
            },
            root_map={
                "validations": {},
                "allowed_values": {},
                "openapi_types": {
                    "model_id": (str,),
                },
                "attribute_map": {
                    "model_id": "model_id",
                },
                "location_map": {
                    "model_id": "path",
                },
                "collection_format_map": {},
            },
            headers_map={
                "accept": ["application/json"],
                "content_type": [],
            },
            api_client=api_client,
            callable=__delete_model,
        )

        def __get_model(self, model_id, **kwargs):
            """get_model  # noqa: E501

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.get_model(model_id, async_req=True)
            >>> result = thread.get()

            Args:
                model_id (str):

            Keyword Args:
                _return_http_data_only (bool): response data without head status
                    code and headers. Default is True.
                _preload_content (bool): if False, the urllib3.HTTPResponse object
                    will be returned without reading/decoding response data.
                    Default is True.
                _request_timeout (float/tuple): timeout setting for this request. If one
                    number provided, it will be total request timeout. It can also
                    be a pair (tuple) of (connection, read) timeouts.
                    Default is None.
                _check_input_type (bool): specifies if type checking
                    should be done one the data sent to the server.
                    Default is True.
                _check_return_type (bool): specifies if type checking
                    should be done one the data received from the server.
                    Default is True.
                _host_index (int/None): specifies the index of the server
                    that we want to use.
                    Default is read from the configuration.
                async_req (bool): execute request asynchronously

            Returns:
                Model
                    If the method is called asynchronously, returns the request
                    thread.
            """
            kwargs["async_req"] = kwargs.get("async_req", False)
            kwargs["_return_http_data_only"] = kwargs.get(
                "_return_http_data_only", True
            )
            kwargs["_preload_content"] = kwargs.get("_preload_content", True)
            kwargs["_request_timeout"] = kwargs.get("_request_timeout", None)
            kwargs["_check_input_type"] = kwargs.get("_check_input_type", True)
            kwargs["_check_return_type"] = kwargs.get("_check_return_type", True)
            kwargs["_host_index"] = kwargs.get("_host_index")
            kwargs["model_id"] = model_id
            return self.call_with_http_info(**kwargs)

        self.get_model = _Endpoint(
            settings={
                "response_type": (Model,),
                "auth": [],
                "endpoint_path": "/v1/models/{model_id}",
                "operation_id": "get_model",
                "http_method": "GET",
                "servers": None,
            },
            params_map={
                "all": [
                    "model_id",
                ],
                "required": [
                    "model_id",
                ],
                "nullable": [],
                "enum": [],
                "validation": [],
            },
            root_map={
                "validations": {},
                "allowed_values": {},
                "openapi_types": {
                    "model_id": (str,),
                },
                "attribute_map": {
                    "model_id": "model_id",
                },
                "location_map": {
                    "model_id": "path",
                },
                "collection_format_map": {},
            },
            headers_map={
                "accept": ["application/json"],
                "content_type": [],
            },
            api_client=api_client,
            callable=__get_model,
        )

        def __get_model_run(self, model_run_id, **kwargs):
            """get_model_run  # noqa: E501

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.get_model_run(model_run_id, async_req=True)
            >>> result = thread.get()

            Args:
                model_run_id (str):

            Keyword Args:
                _return_http_data_only (bool): response data without head status
                    code and headers. Default is True.
                _preload_content (bool): if False, the urllib3.HTTPResponse object
                    will be returned without reading/decoding response data.
                    Default is True.
                _request_timeout (float/tuple): timeout setting for this request. If one
                    number provided, it will be total request timeout. It can also
                    be a pair (tuple) of (connection, read) timeouts.
                    Default is None.
                _check_input_type (bool): specifies if type checking
                    should be done one the data sent to the server.
                    Default is True.
                _check_return_type (bool): specifies if type checking
                    should be done one the data received from the server.
                    Default is True.
                _host_index (int/None): specifies the index of the server
                    that we want to use.
                    Default is read from the configuration.
                async_req (bool): execute request asynchronously

            Returns:
                ModelRun
                    If the method is called asynchronously, returns the request
                    thread.
            """
            kwargs["async_req"] = kwargs.get("async_req", False)
            kwargs["_return_http_data_only"] = kwargs.get(
                "_return_http_data_only", True
            )
            kwargs["_preload_content"] = kwargs.get("_preload_content", True)
            kwargs["_request_timeout"] = kwargs.get("_request_timeout", None)
            kwargs["_check_input_type"] = kwargs.get("_check_input_type", True)
            kwargs["_check_return_type"] = kwargs.get("_check_return_type", True)
            kwargs["_host_index"] = kwargs.get("_host_index")
            kwargs["model_run_id"] = model_run_id
            return self.call_with_http_info(**kwargs)

        self.get_model_run = _Endpoint(
            settings={
                "response_type": (ModelRun,),
                "auth": [],
                "endpoint_path": "/v1/models/runs/{model_run_id}",
                "operation_id": "get_model_run",
                "http_method": "GET",
                "servers": None,
            },
            params_map={
                "all": [
                    "model_run_id",
                ],
                "required": [
                    "model_run_id",
                ],
                "nullable": [],
                "enum": [],
                "validation": [],
            },
            root_map={
                "validations": {},
                "allowed_values": {},
                "openapi_types": {
                    "model_run_id": (str,),
                },
                "attribute_map": {
                    "model_run_id": "model_run_id",
                },
                "location_map": {
                    "model_run_id": "path",
                },
                "collection_format_map": {},
            },
            headers_map={
                "accept": ["application/json"],
                "content_type": [],
            },
            api_client=api_client,
            callable=__get_model_run,
        )

        def __list_models(self, **kwargs):
            """list_models  # noqa: E501

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.list_models(async_req=True)
            >>> result = thread.get()


            Keyword Args:
                project_id (str): [optional]
                _return_http_data_only (bool): response data without head status
                    code and headers. Default is True.
                _preload_content (bool): if False, the urllib3.HTTPResponse object
                    will be returned without reading/decoding response data.
                    Default is True.
                _request_timeout (float/tuple): timeout setting for this request. If one
                    number provided, it will be total request timeout. It can also
                    be a pair (tuple) of (connection, read) timeouts.
                    Default is None.
                _check_input_type (bool): specifies if type checking
                    should be done one the data sent to the server.
                    Default is True.
                _check_return_type (bool): specifies if type checking
                    should be done one the data received from the server.
                    Default is True.
                _host_index (int/None): specifies the index of the server
                    that we want to use.
                    Default is read from the configuration.
                async_req (bool): execute request asynchronously

            Returns:
                ListModelsResponse
                    If the method is called asynchronously, returns the request
                    thread.
            """
            kwargs["async_req"] = kwargs.get("async_req", False)
            kwargs["_return_http_data_only"] = kwargs.get(
                "_return_http_data_only", True
            )
            kwargs["_preload_content"] = kwargs.get("_preload_content", True)
            kwargs["_request_timeout"] = kwargs.get("_request_timeout", None)
            kwargs["_check_input_type"] = kwargs.get("_check_input_type", True)
            kwargs["_check_return_type"] = kwargs.get("_check_return_type", True)
            kwargs["_host_index"] = kwargs.get("_host_index")
            return self.call_with_http_info(**kwargs)

        self.list_models = _Endpoint(
            settings={
                "response_type": (ListModelsResponse,),
                "auth": [],
                "endpoint_path": "/v1/models",
                "operation_id": "list_models",
                "http_method": "GET",
                "servers": None,
            },
            params_map={
                "all": [
                    "project_id",
                ],
                "required": [],
                "nullable": [],
                "enum": [],
                "validation": [],
            },
            root_map={
                "validations": {},
                "allowed_values": {},
                "openapi_types": {
                    "project_id": (str,),
                },
                "attribute_map": {
                    "project_id": "project_id",
                },
                "location_map": {
                    "project_id": "query",
                },
                "collection_format_map": {},
            },
            headers_map={
                "accept": ["application/json"],
                "content_type": [],
            },
            api_client=api_client,
            callable=__list_models,
        )

        def __search_model_runs(self, **kwargs):
            """search_model_runs  # noqa: E501

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.search_model_runs(async_req=True)
            >>> result = thread.get()


            Keyword Args:
                query (str): [optional]
                expand ([str]): [optional]
                limit (int): [optional]
                next_page (str): [optional]
                _return_http_data_only (bool): response data without head status
                    code and headers. Default is True.
                _preload_content (bool): if False, the urllib3.HTTPResponse object
                    will be returned without reading/decoding response data.
                    Default is True.
                _request_timeout (float/tuple): timeout setting for this request. If one
                    number provided, it will be total request timeout. It can also
                    be a pair (tuple) of (connection, read) timeouts.
                    Default is None.
                _check_input_type (bool): specifies if type checking
                    should be done one the data sent to the server.
                    Default is True.
                _check_return_type (bool): specifies if type checking
                    should be done one the data received from the server.
                    Default is True.
                _host_index (int/None): specifies the index of the server
                    that we want to use.
                    Default is read from the configuration.
                async_req (bool): execute request asynchronously

            Returns:
                SearchModelRunsResponse
                    If the method is called asynchronously, returns the request
                    thread.
            """
            kwargs["async_req"] = kwargs.get("async_req", False)
            kwargs["_return_http_data_only"] = kwargs.get(
                "_return_http_data_only", True
            )
            kwargs["_preload_content"] = kwargs.get("_preload_content", True)
            kwargs["_request_timeout"] = kwargs.get("_request_timeout", None)
            kwargs["_check_input_type"] = kwargs.get("_check_input_type", True)
            kwargs["_check_return_type"] = kwargs.get("_check_return_type", True)
            kwargs["_host_index"] = kwargs.get("_host_index")
            return self.call_with_http_info(**kwargs)

        self.search_model_runs = _Endpoint(
            settings={
                "response_type": (SearchModelRunsResponse,),
                "auth": [],
                "endpoint_path": "/v1/models/runs/search",
                "operation_id": "search_model_runs",
                "http_method": "GET",
                "servers": None,
            },
            params_map={
                "all": [
                    "query",
                    "expand",
                    "limit",
                    "next_page",
                ],
                "required": [],
                "nullable": [],
                "enum": [
                    "expand",
                ],
                "validation": [],
            },
            root_map={
                "validations": {},
                "allowed_values": {
                    ("expand",): {
                        "LOGS": "EXPAND_OPTIONS_LOGS",
                        "HISTORY": "EXPAND_OPTIONS_HISTORY",
                        "INPUTS": "EXPAND_OPTIONS_INPUTS",
                        "OUTPUTS": "EXPAND_OPTIONS_OUTPUTS",
                        "LINEAGE": "EXPAND_OPTIONS_LINEAGE",
                    },
                },
                "openapi_types": {
                    "query": (str,),
                    "expand": ([str],),
                    "limit": (int,),
                    "next_page": (str,),
                },
                "attribute_map": {
                    "query": "query",
                    "expand": "expand",
                    "limit": "limit",
                    "next_page": "next_page",
                },
                "location_map": {
                    "query": "query",
                    "expand": "query",
                    "limit": "query",
                    "next_page": "query",
                },
                "collection_format_map": {
                    "expand": "multi",
                },
            },
            headers_map={
                "accept": ["application/json"],
                "content_type": [],
            },
            api_client=api_client,
            callable=__search_model_runs,
        )

        def __update_model(self, model_id, model, **kwargs):
            """update_model  # noqa: E501

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.update_model(model_id, model, async_req=True)
            >>> result = thread.get()

            Args:
                model_id (str):
                model (Model):

            Keyword Args:
                _return_http_data_only (bool): response data without head status
                    code and headers. Default is True.
                _preload_content (bool): if False, the urllib3.HTTPResponse object
                    will be returned without reading/decoding response data.
                    Default is True.
                _request_timeout (float/tuple): timeout setting for this request. If one
                    number provided, it will be total request timeout. It can also
                    be a pair (tuple) of (connection, read) timeouts.
                    Default is None.
                _check_input_type (bool): specifies if type checking
                    should be done one the data sent to the server.
                    Default is True.
                _check_return_type (bool): specifies if type checking
                    should be done one the data received from the server.
                    Default is True.
                _host_index (int/None): specifies the index of the server
                    that we want to use.
                    Default is read from the configuration.
                async_req (bool): execute request asynchronously

            Returns:
                Model
                    If the method is called asynchronously, returns the request
                    thread.
            """
            kwargs["async_req"] = kwargs.get("async_req", False)
            kwargs["_return_http_data_only"] = kwargs.get(
                "_return_http_data_only", True
            )
            kwargs["_preload_content"] = kwargs.get("_preload_content", True)
            kwargs["_request_timeout"] = kwargs.get("_request_timeout", None)
            kwargs["_check_input_type"] = kwargs.get("_check_input_type", True)
            kwargs["_check_return_type"] = kwargs.get("_check_return_type", True)
            kwargs["_host_index"] = kwargs.get("_host_index")
            kwargs["model_id"] = model_id
            kwargs["model"] = model
            return self.call_with_http_info(**kwargs)

        self.update_model = _Endpoint(
            settings={
                "response_type": (Model,),
                "auth": [],
                "endpoint_path": "/v1/models/{model_id}",
                "operation_id": "update_model",
                "http_method": "PATCH",
                "servers": None,
            },
            params_map={
                "all": [
                    "model_id",
                    "model",
                ],
                "required": [
                    "model_id",
                    "model",
                ],
                "nullable": [],
                "enum": [],
                "validation": [],
            },
            root_map={
                "validations": {},
                "allowed_values": {},
                "openapi_types": {
                    "model_id": (str,),
                    "model": (Model,),
                },
                "attribute_map": {
                    "model_id": "model_id",
                },
                "location_map": {
                    "model_id": "path",
                    "model": "body",
                },
                "collection_format_map": {},
            },
            headers_map={
                "accept": ["application/json"],
                "content_type": ["application/json"],
            },
            api_client=api_client,
            callable=__update_model,
        )

        def __update_model_run_status(
            self, model_run_id, update_model_run_status_request, **kwargs
        ):
            """update_model_run_status  # noqa: E501

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.update_model_run_status(model_run_id, update_model_run_status_request, async_req=True)
            >>> result = thread.get()

            Args:
                model_run_id (str):
                update_model_run_status_request (UpdateModelRunStatusRequest):

            Keyword Args:
                _return_http_data_only (bool): response data without head status
                    code and headers. Default is True.
                _preload_content (bool): if False, the urllib3.HTTPResponse object
                    will be returned without reading/decoding response data.
                    Default is True.
                _request_timeout (float/tuple): timeout setting for this request. If one
                    number provided, it will be total request timeout. It can also
                    be a pair (tuple) of (connection, read) timeouts.
                    Default is None.
                _check_input_type (bool): specifies if type checking
                    should be done one the data sent to the server.
                    Default is True.
                _check_return_type (bool): specifies if type checking
                    should be done one the data received from the server.
                    Default is True.
                _host_index (int/None): specifies the index of the server
                    that we want to use.
                    Default is read from the configuration.
                async_req (bool): execute request asynchronously

            Returns:
                ModelRun
                    If the method is called asynchronously, returns the request
                    thread.
            """
            kwargs["async_req"] = kwargs.get("async_req", False)
            kwargs["_return_http_data_only"] = kwargs.get(
                "_return_http_data_only", True
            )
            kwargs["_preload_content"] = kwargs.get("_preload_content", True)
            kwargs["_request_timeout"] = kwargs.get("_request_timeout", None)
            kwargs["_check_input_type"] = kwargs.get("_check_input_type", True)
            kwargs["_check_return_type"] = kwargs.get("_check_return_type", True)
            kwargs["_host_index"] = kwargs.get("_host_index")
            kwargs["model_run_id"] = model_run_id
            kwargs["update_model_run_status_request"] = update_model_run_status_request
            return self.call_with_http_info(**kwargs)

        self.update_model_run_status = _Endpoint(
            settings={
                "response_type": (ModelRun,),
                "auth": [],
                "endpoint_path": "/v1/model/runs/{model_run_id}/status",
                "operation_id": "update_model_run_status",
                "http_method": "PUT",
                "servers": None,
            },
            params_map={
                "all": [
                    "model_run_id",
                    "update_model_run_status_request",
                ],
                "required": [
                    "model_run_id",
                    "update_model_run_status_request",
                ],
                "nullable": [],
                "enum": [],
                "validation": [],
            },
            root_map={
                "validations": {},
                "allowed_values": {},
                "openapi_types": {
                    "model_run_id": (str,),
                    "update_model_run_status_request": (UpdateModelRunStatusRequest,),
                },
                "attribute_map": {
                    "model_run_id": "model_run_id",
                },
                "location_map": {
                    "model_run_id": "path",
                    "update_model_run_status_request": "body",
                },
                "collection_format_map": {},
            },
            headers_map={
                "accept": ["application/json"],
                "content_type": ["application/json"],
            },
            api_client=api_client,
            callable=__update_model_run_status,
        )
