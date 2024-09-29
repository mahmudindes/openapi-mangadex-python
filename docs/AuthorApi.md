# mangadex_openapi.AuthorApi

All URIs are relative to *https://api.mangadex.org*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_author_id**](AuthorApi.md#delete_author_id) | **DELETE** /author/{id} | Delete Author
[**get_author**](AuthorApi.md#get_author) | **GET** /author | Author list
[**get_author_id**](AuthorApi.md#get_author_id) | **GET** /author/{id} | Get Author
[**post_author**](AuthorApi.md#post_author) | **POST** /author | Create Author
[**put_author_id**](AuthorApi.md#put_author_id) | **PUT** /author/{id} | Update Author


# **delete_author_id**
> Response delete_author_id(id)

Delete Author

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
    api_instance = mangadex_openapi.AuthorApi(api_client)
    id = 'id_example' # str | Author ID

    try:
        # Delete Author
        api_response = api_instance.delete_author_id(id)
        print("The response of AuthorApi->delete_author_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthorApi->delete_author_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Author ID | 

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

# **get_author**
> AuthorList get_author(limit=limit, offset=offset, ids=ids, name=name, order=order, includes=includes)

Author list

### Example


```python
import mangadex_openapi
from mangadex_openapi.models.author_list import AuthorList
from mangadex_openapi.models.get_author_order_parameter import GetAuthorOrderParameter
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
    api_instance = mangadex_openapi.AuthorApi(api_client)
    limit = 10 # int |  (optional) (default to 10)
    offset = 56 # int |  (optional)
    ids = ['ids_example'] # List[str] | Author ids (limited to 100 per request) (optional)
    name = 'name_example' # str |  (optional)
    order = mangadex_openapi.GetAuthorOrderParameter() # GetAuthorOrderParameter |  (optional)
    includes = ['includes_example'] # List[str] |  (optional)

    try:
        # Author list
        api_response = api_instance.get_author(limit=limit, offset=offset, ids=ids, name=name, order=order, includes=includes)
        print("The response of AuthorApi->get_author:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthorApi->get_author: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**|  | [optional] [default to 10]
 **offset** | **int**|  | [optional] 
 **ids** | [**List[str]**](str.md)| Author ids (limited to 100 per request) | [optional] 
 **name** | **str**|  | [optional] 
 **order** | [**GetAuthorOrderParameter**](.md)|  | [optional] 
 **includes** | [**List[str]**](str.md)|  | [optional] 

### Return type

[**AuthorList**](AuthorList.md)

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

# **get_author_id**
> AuthorResponse get_author_id(id, includes=includes)

Get Author

### Example


```python
import mangadex_openapi
from mangadex_openapi.models.author_response import AuthorResponse
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
    api_instance = mangadex_openapi.AuthorApi(api_client)
    id = 'id_example' # str | Author ID
    includes = ['includes_example'] # List[str] |  (optional)

    try:
        # Get Author
        api_response = api_instance.get_author_id(id, includes=includes)
        print("The response of AuthorApi->get_author_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthorApi->get_author_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Author ID | 
 **includes** | [**List[str]**](str.md)|  | [optional] 

### Return type

[**AuthorResponse**](AuthorResponse.md)

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
**404** | Author no content |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_author**
> AuthorResponse post_author(content_type, author_create=author_create)

Create Author

### Example

* Bearer Authentication (Bearer):

```python
import mangadex_openapi
from mangadex_openapi.models.author_create import AuthorCreate
from mangadex_openapi.models.author_response import AuthorResponse
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
    api_instance = mangadex_openapi.AuthorApi(api_client)
    content_type = 'application/json' # str |  (default to 'application/json')
    author_create = mangadex_openapi.AuthorCreate() # AuthorCreate | The size of the body is limited to 8KB. (optional)

    try:
        # Create Author
        api_response = api_instance.post_author(content_type, author_create=author_create)
        print("The response of AuthorApi->post_author:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthorApi->post_author: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **content_type** | **str**|  | [default to &#39;application/json&#39;]
 **author_create** | [**AuthorCreate**](AuthorCreate.md)| The size of the body is limited to 8KB. | [optional] 

### Return type

[**AuthorResponse**](AuthorResponse.md)

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

# **put_author_id**
> AuthorResponse put_author_id(id, content_type, author_edit=author_edit)

Update Author

### Example

* Bearer Authentication (Bearer):

```python
import mangadex_openapi
from mangadex_openapi.models.author_edit import AuthorEdit
from mangadex_openapi.models.author_response import AuthorResponse
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
    api_instance = mangadex_openapi.AuthorApi(api_client)
    id = 'id_example' # str | Author ID
    content_type = 'application/json' # str |  (default to 'application/json')
    author_edit = mangadex_openapi.AuthorEdit() # AuthorEdit | The size of the body is limited to 8KB. (optional)

    try:
        # Update Author
        api_response = api_instance.put_author_id(id, content_type, author_edit=author_edit)
        print("The response of AuthorApi->put_author_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthorApi->put_author_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Author ID | 
 **content_type** | **str**|  | [default to &#39;application/json&#39;]
 **author_edit** | [**AuthorEdit**](AuthorEdit.md)| The size of the body is limited to 8KB. | [optional] 

### Return type

[**AuthorResponse**](AuthorResponse.md)

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

