# mangadex_openapi.ScanlationGroupApi

All URIs are relative to *https://api.mangadex.org*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_group_id**](ScanlationGroupApi.md#delete_group_id) | **DELETE** /group/{id} | Delete Scanlation Group
[**delete_group_id_follow**](ScanlationGroupApi.md#delete_group_id_follow) | **DELETE** /group/{id}/follow | Unfollow Scanlation Group
[**get_group_id**](ScanlationGroupApi.md#get_group_id) | **GET** /group/{id} | Get Scanlation Group
[**get_search_group**](ScanlationGroupApi.md#get_search_group) | **GET** /group | Scanlation Group list
[**post_group**](ScanlationGroupApi.md#post_group) | **POST** /group | Create Scanlation Group
[**post_group_id_follow**](ScanlationGroupApi.md#post_group_id_follow) | **POST** /group/{id}/follow | Follow Scanlation Group
[**put_group_id**](ScanlationGroupApi.md#put_group_id) | **PUT** /group/{id} | Update Scanlation Group


# **delete_group_id**
> Response delete_group_id(id)

Delete Scanlation Group

### Example

* Bearer Authentication (Bearer):

```python
import mangadex_openapi
from mangadex_openapi.models.response import Response
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
    api_instance = mangadex_openapi.ScanlationGroupApi(api_client)
    id = 'id_example' # str | Scanlation Group ID

    try:
        # Delete Scanlation Group
        api_response = api_instance.delete_group_id(id)
        print("The response of ScanlationGroupApi->delete_group_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ScanlationGroupApi->delete_group_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Scanlation Group ID | 

### Return type

[**Response**](Response.md)

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

# **delete_group_id_follow**
> Response delete_group_id_follow(id)

Unfollow Scanlation Group

### Example

* Bearer Authentication (Bearer):

```python
import mangadex_openapi
from mangadex_openapi.models.response import Response
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
    api_instance = mangadex_openapi.ScanlationGroupApi(api_client)
    id = 'id_example' # str | 

    try:
        # Unfollow Scanlation Group
        api_response = api_instance.delete_group_id_follow(id)
        print("The response of ScanlationGroupApi->delete_group_id_follow:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ScanlationGroupApi->delete_group_id_follow: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**Response**](Response.md)

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

# **get_group_id**
> ScanlationGroupResponse get_group_id(id, includes=includes)

Get Scanlation Group

### Example


```python
import mangadex_openapi
from mangadex_openapi.models.scanlation_group_response import ScanlationGroupResponse
from mangadex_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.mangadex.org
# See configuration.py for a list of all supported configuration parameters.
configuration = mangadex_openapi.Configuration(
    host = "https://api.mangadex.org"
)


# Enter a context with an instance of the API client
with mangadex_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = mangadex_openapi.ScanlationGroupApi(api_client)
    id = 'id_example' # str | Scanlation Group ID
    includes = ['includes_example'] # List[str] |  (optional)

    try:
        # Get Scanlation Group
        api_response = api_instance.get_group_id(id, includes=includes)
        print("The response of ScanlationGroupApi->get_group_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ScanlationGroupApi->get_group_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Scanlation Group ID | 
 **includes** | [**List[str]**](str.md)|  | [optional] 

### Return type

[**ScanlationGroupResponse**](ScanlationGroupResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**403** | Forbidden |  -  |
**404** | ScanlationGroup not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_search_group**
> ScanlationGroupList get_search_group(limit=limit, offset=offset, ids=ids, name=name, focused_language=focused_language, includes=includes, order=order)

Scanlation Group list

### Example


```python
import mangadex_openapi
from mangadex_openapi.models.get_search_group_order_parameter import GetSearchGroupOrderParameter
from mangadex_openapi.models.scanlation_group_list import ScanlationGroupList
from mangadex_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.mangadex.org
# See configuration.py for a list of all supported configuration parameters.
configuration = mangadex_openapi.Configuration(
    host = "https://api.mangadex.org"
)


# Enter a context with an instance of the API client
with mangadex_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = mangadex_openapi.ScanlationGroupApi(api_client)
    limit = 10 # int |  (optional) (default to 10)
    offset = 56 # int |  (optional)
    ids = ['ids_example'] # List[str] | ScanlationGroup ids (limited to 100 per request) (optional)
    name = 'name_example' # str |  (optional)
    focused_language = 'focused_language_example' # str |  (optional)
    includes = ['includes_example'] # List[str] |  (optional)
    order = mangadex_openapi.GetSearchGroupOrderParameter() # GetSearchGroupOrderParameter |  (optional)

    try:
        # Scanlation Group list
        api_response = api_instance.get_search_group(limit=limit, offset=offset, ids=ids, name=name, focused_language=focused_language, includes=includes, order=order)
        print("The response of ScanlationGroupApi->get_search_group:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ScanlationGroupApi->get_search_group: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**|  | [optional] [default to 10]
 **offset** | **int**|  | [optional] 
 **ids** | [**List[str]**](str.md)| ScanlationGroup ids (limited to 100 per request) | [optional] 
 **name** | **str**|  | [optional] 
 **focused_language** | **str**|  | [optional] 
 **includes** | [**List[str]**](str.md)|  | [optional] 
 **order** | [**GetSearchGroupOrderParameter**](.md)|  | [optional] 

### Return type

[**ScanlationGroupList**](ScanlationGroupList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_group**
> ScanlationGroupResponse post_group(content_type, create_scanlation_group=create_scanlation_group)

Create Scanlation Group

### Example

* Bearer Authentication (Bearer):

```python
import mangadex_openapi
from mangadex_openapi.models.create_scanlation_group import CreateScanlationGroup
from mangadex_openapi.models.scanlation_group_response import ScanlationGroupResponse
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
    api_instance = mangadex_openapi.ScanlationGroupApi(api_client)
    content_type = 'application/json' # str |  (default to 'application/json')
    create_scanlation_group = mangadex_openapi.CreateScanlationGroup() # CreateScanlationGroup | The size of the body is limited to 16KB. (optional)

    try:
        # Create Scanlation Group
        api_response = api_instance.post_group(content_type, create_scanlation_group=create_scanlation_group)
        print("The response of ScanlationGroupApi->post_group:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ScanlationGroupApi->post_group: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **content_type** | **str**|  | [default to &#39;application/json&#39;]
 **create_scanlation_group** | [**CreateScanlationGroup**](CreateScanlationGroup.md)| The size of the body is limited to 16KB. | [optional] 

### Return type

[**ScanlationGroupResponse**](ScanlationGroupResponse.md)

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

# **post_group_id_follow**
> Response post_group_id_follow(id)

Follow Scanlation Group

### Example

* Bearer Authentication (Bearer):

```python
import mangadex_openapi
from mangadex_openapi.models.response import Response
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
    api_instance = mangadex_openapi.ScanlationGroupApi(api_client)
    id = 'id_example' # str | 

    try:
        # Follow Scanlation Group
        api_response = api_instance.post_group_id_follow(id)
        print("The response of ScanlationGroupApi->post_group_id_follow:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ScanlationGroupApi->post_group_id_follow: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**Response**](Response.md)

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

# **put_group_id**
> ScanlationGroupResponse put_group_id(id, content_type, scanlation_group_edit=scanlation_group_edit)

Update Scanlation Group

### Example

* Bearer Authentication (Bearer):

```python
import mangadex_openapi
from mangadex_openapi.models.scanlation_group_edit import ScanlationGroupEdit
from mangadex_openapi.models.scanlation_group_response import ScanlationGroupResponse
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
    api_instance = mangadex_openapi.ScanlationGroupApi(api_client)
    id = 'id_example' # str | Scanlation Group ID
    content_type = 'application/json' # str |  (default to 'application/json')
    scanlation_group_edit = mangadex_openapi.ScanlationGroupEdit() # ScanlationGroupEdit | The size of the body is limited to 8KB. (optional)

    try:
        # Update Scanlation Group
        api_response = api_instance.put_group_id(id, content_type, scanlation_group_edit=scanlation_group_edit)
        print("The response of ScanlationGroupApi->put_group_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ScanlationGroupApi->put_group_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Scanlation Group ID | 
 **content_type** | **str**|  | [default to &#39;application/json&#39;]
 **scanlation_group_edit** | [**ScanlationGroupEdit**](ScanlationGroupEdit.md)| The size of the body is limited to 8KB. | [optional] 

### Return type

[**ScanlationGroupResponse**](ScanlationGroupResponse.md)

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

