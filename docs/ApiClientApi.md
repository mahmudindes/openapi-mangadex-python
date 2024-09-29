# mangadex_openapi.ApiClientApi

All URIs are relative to *https://api.mangadex.org*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_apiclient**](ApiClientApi.md#delete_apiclient) | **DELETE** /client/{id} | Delete Api Client
[**get_apiclient**](ApiClientApi.md#get_apiclient) | **GET** /client/{id} | Get Api Client by ID
[**get_apiclient_secret**](ApiClientApi.md#get_apiclient_secret) | **GET** /client/{id}/secret | Get Secret for Client by ID
[**get_list_apiclients**](ApiClientApi.md#get_list_apiclients) | **GET** /client | List own Api Clients
[**post_create_apiclient**](ApiClientApi.md#post_create_apiclient) | **POST** /client | Create ApiClient
[**post_edit_apiclient**](ApiClientApi.md#post_edit_apiclient) | **POST** /client/{id} | Edit ApiClient
[**post_regenerate_apiclient_secret**](ApiClientApi.md#post_regenerate_apiclient_secret) | **POST** /client/{id}/secret | Regenerate Client Secret


# **delete_apiclient**
> DeleteApiclient200Response delete_apiclient(id, version=version)

Delete Api Client

### Example

* Bearer Authentication (Bearer):

```python
import mangadex_openapi
from mangadex_openapi.models.delete_apiclient200_response import DeleteApiclient200Response
from mangadex_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.mangadex.org
# See configuration.py for a list of all supported configuration parameters.
configuration = mangadex_openapi.Configuration(
    host = "https://api.mangadex.org"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: Bearer
configuration = mangadex_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with mangadex_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = mangadex_openapi.ApiClientApi(api_client)
    id = 'id_example' # str | ApiClient ID
    version = 'version_example' # str |  (optional)

    try:
        # Delete Api Client
        api_response = api_instance.delete_apiclient(id, version=version)
        print("The response of ApiClientApi->delete_apiclient:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApiClientApi->delete_apiclient: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ApiClient ID | 
 **version** | **str**|  | [optional] 

### Return type

[**DeleteApiclient200Response**](DeleteApiclient200Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_apiclient**
> ApiClientResponse get_apiclient(id, includes=includes)

Get Api Client by ID

### Example

* Bearer Authentication (Bearer):

```python
import mangadex_openapi
from mangadex_openapi.models.api_client_response import ApiClientResponse
from mangadex_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.mangadex.org
# See configuration.py for a list of all supported configuration parameters.
configuration = mangadex_openapi.Configuration(
    host = "https://api.mangadex.org"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: Bearer
configuration = mangadex_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with mangadex_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = mangadex_openapi.ApiClientApi(api_client)
    id = 'id_example' # str | ApiClient ID
    includes = ['includes_example'] # List[str] |  (optional)

    try:
        # Get Api Client by ID
        api_response = api_instance.get_apiclient(id, includes=includes)
        print("The response of ApiClientApi->get_apiclient:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApiClientApi->get_apiclient: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ApiClient ID | 
 **includes** | [**List[str]**](str.md)|  | [optional] 

### Return type

[**ApiClientResponse**](ApiClientResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_apiclient_secret**
> GetApiclientSecret200Response get_apiclient_secret(id)

Get Secret for Client by ID

### Example

* Bearer Authentication (Bearer):

```python
import mangadex_openapi
from mangadex_openapi.models.get_apiclient_secret200_response import GetApiclientSecret200Response
from mangadex_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.mangadex.org
# See configuration.py for a list of all supported configuration parameters.
configuration = mangadex_openapi.Configuration(
    host = "https://api.mangadex.org"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: Bearer
configuration = mangadex_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with mangadex_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = mangadex_openapi.ApiClientApi(api_client)
    id = 'id_example' # str | ApiClient ID

    try:
        # Get Secret for Client by ID
        api_response = api_instance.get_apiclient_secret(id)
        print("The response of ApiClientApi->get_apiclient_secret:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApiClientApi->get_apiclient_secret: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ApiClient ID | 

### Return type

[**GetApiclientSecret200Response**](GetApiclientSecret200Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**403** | Client not found, not active or user is not the owner |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_list_apiclients**
> ApiClientList get_list_apiclients(limit=limit, offset=offset, state=state, name=name, includes=includes, order=order)

List own Api Clients

### Example

* Bearer Authentication (Bearer):

```python
import mangadex_openapi
from mangadex_openapi.models.api_client_list import ApiClientList
from mangadex_openapi.models.get_list_apiclients_order_parameter import GetListApiclientsOrderParameter
from mangadex_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.mangadex.org
# See configuration.py for a list of all supported configuration parameters.
configuration = mangadex_openapi.Configuration(
    host = "https://api.mangadex.org"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: Bearer
configuration = mangadex_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with mangadex_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = mangadex_openapi.ApiClientApi(api_client)
    limit = 10 # int |  (optional) (default to 10)
    offset = 56 # int |  (optional)
    state = 'state_example' # str |  (optional)
    name = 'name_example' # str |  (optional)
    includes = ['includes_example'] # List[str] |  (optional)
    order = mangadex_openapi.GetListApiclientsOrderParameter() # GetListApiclientsOrderParameter |  (optional)

    try:
        # List own Api Clients
        api_response = api_instance.get_list_apiclients(limit=limit, offset=offset, state=state, name=name, includes=includes, order=order)
        print("The response of ApiClientApi->get_list_apiclients:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApiClientApi->get_list_apiclients: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**|  | [optional] [default to 10]
 **offset** | **int**|  | [optional] 
 **state** | **str**|  | [optional] 
 **name** | **str**|  | [optional] 
 **includes** | [**List[str]**](str.md)|  | [optional] 
 **order** | [**GetListApiclientsOrderParameter**](.md)|  | [optional] 

### Return type

[**ApiClientList**](ApiClientList.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_create_apiclient**
> ApiClientResponse post_create_apiclient(content_type, api_client_create=api_client_create)

Create ApiClient

### Example

* Bearer Authentication (Bearer):

```python
import mangadex_openapi
from mangadex_openapi.models.api_client_create import ApiClientCreate
from mangadex_openapi.models.api_client_response import ApiClientResponse
from mangadex_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.mangadex.org
# See configuration.py for a list of all supported configuration parameters.
configuration = mangadex_openapi.Configuration(
    host = "https://api.mangadex.org"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: Bearer
configuration = mangadex_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with mangadex_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = mangadex_openapi.ApiClientApi(api_client)
    content_type = 'application/json' # str |  (default to 'application/json')
    api_client_create = mangadex_openapi.ApiClientCreate() # ApiClientCreate |  (optional)

    try:
        # Create ApiClient
        api_response = api_instance.post_create_apiclient(content_type, api_client_create=api_client_create)
        print("The response of ApiClientApi->post_create_apiclient:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApiClientApi->post_create_apiclient: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **content_type** | **str**|  | [default to &#39;application/json&#39;]
 **api_client_create** | [**ApiClientCreate**](ApiClientCreate.md)|  | [optional] 

### Return type

[**ApiClientResponse**](ApiClientResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_edit_apiclient**
> ApiClientResponse post_edit_apiclient(id, content_type, api_client_edit=api_client_edit)

Edit ApiClient

### Example

* Bearer Authentication (Bearer):

```python
import mangadex_openapi
from mangadex_openapi.models.api_client_edit import ApiClientEdit
from mangadex_openapi.models.api_client_response import ApiClientResponse
from mangadex_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.mangadex.org
# See configuration.py for a list of all supported configuration parameters.
configuration = mangadex_openapi.Configuration(
    host = "https://api.mangadex.org"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: Bearer
configuration = mangadex_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with mangadex_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = mangadex_openapi.ApiClientApi(api_client)
    id = 'id_example' # str | ApiClient ID
    content_type = 'application/json' # str |  (default to 'application/json')
    api_client_edit = mangadex_openapi.ApiClientEdit() # ApiClientEdit |  (optional)

    try:
        # Edit ApiClient
        api_response = api_instance.post_edit_apiclient(id, content_type, api_client_edit=api_client_edit)
        print("The response of ApiClientApi->post_edit_apiclient:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApiClientApi->post_edit_apiclient: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ApiClient ID | 
 **content_type** | **str**|  | [default to &#39;application/json&#39;]
 **api_client_edit** | [**ApiClientEdit**](ApiClientEdit.md)|  | [optional] 

### Return type

[**ApiClientResponse**](ApiClientResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_regenerate_apiclient_secret**
> GetApiclientSecret200Response post_regenerate_apiclient_secret(id, content_type, body=body)

Regenerate Client Secret

### Example

* Bearer Authentication (Bearer):

```python
import mangadex_openapi
from mangadex_openapi.models.get_apiclient_secret200_response import GetApiclientSecret200Response
from mangadex_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.mangadex.org
# See configuration.py for a list of all supported configuration parameters.
configuration = mangadex_openapi.Configuration(
    host = "https://api.mangadex.org"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: Bearer
configuration = mangadex_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with mangadex_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = mangadex_openapi.ApiClientApi(api_client)
    id = 'id_example' # str | ApiClient ID
    content_type = 'application/json' # str |  (default to 'application/json')
    body = None # object |  (optional)

    try:
        # Regenerate Client Secret
        api_response = api_instance.post_regenerate_apiclient_secret(id, content_type, body=body)
        print("The response of ApiClientApi->post_regenerate_apiclient_secret:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApiClientApi->post_regenerate_apiclient_secret: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ApiClient ID | 
 **content_type** | **str**|  | [default to &#39;application/json&#39;]
 **body** | **object**|  | [optional] 

### Return type

[**GetApiclientSecret200Response**](GetApiclientSecret200Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**403** | Client not found, not active or user is not the owner |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

