# mangadex_openapi.CustomListApi

All URIs are relative to *https://api.mangadex.org*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_list_id**](CustomListApi.md#delete_list_id) | **DELETE** /list/{id} | Delete CustomList
[**delete_manga_id_list_list_id**](CustomListApi.md#delete_manga_id_list_list_id) | **DELETE** /manga/{id}/list/{listId} | Remove Manga in CustomList
[**follow_list_id**](CustomListApi.md#follow_list_id) | **POST** /list/{id}/follow | Follow CustomList
[**get_list_id**](CustomListApi.md#get_list_id) | **GET** /list/{id} | Get CustomList
[**get_user_id_list**](CustomListApi.md#get_user_id_list) | **GET** /user/{id}/list | Get User&#39;s CustomList list
[**get_user_list**](CustomListApi.md#get_user_list) | **GET** /user/list | Get logged User CustomList list
[**post_list**](CustomListApi.md#post_list) | **POST** /list | Create CustomList
[**post_manga_id_list_list_id**](CustomListApi.md#post_manga_id_list_list_id) | **POST** /manga/{id}/list/{listId} | Add Manga in CustomList
[**put_list_id**](CustomListApi.md#put_list_id) | **PUT** /list/{id} | Update CustomList
[**unfollow_list_id**](CustomListApi.md#unfollow_list_id) | **DELETE** /list/{id}/follow | Unfollow CustomList


# **delete_list_id**
> Response delete_list_id(id)

Delete CustomList

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
    api_instance = mangadex_openapi.CustomListApi(api_client)
    id = 'id_example' # str | CustomList ID

    try:
        # Delete CustomList
        api_response = api_instance.delete_list_id(id)
        print("The response of CustomListApi->delete_list_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomListApi->delete_list_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| CustomList ID | 

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

# **delete_manga_id_list_list_id**
> Response delete_manga_id_list_list_id(id, list_id)

Remove Manga in CustomList

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
    api_instance = mangadex_openapi.CustomListApi(api_client)
    id = 'id_example' # str | Manga ID
    list_id = 'list_id_example' # str | CustomList ID

    try:
        # Remove Manga in CustomList
        api_response = api_instance.delete_manga_id_list_list_id(id, list_id)
        print("The response of CustomListApi->delete_manga_id_list_list_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomListApi->delete_manga_id_list_list_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Manga ID | 
 **list_id** | **str**| CustomList ID | 

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

# **follow_list_id**
> FollowListId200Response follow_list_id(id, content_type, body=body)

Follow CustomList

The request body is empty

### Example

* Bearer Authentication (Bearer):

```python
import mangadex_openapi
from mangadex_openapi.models.follow_list_id200_response import FollowListId200Response
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
    api_instance = mangadex_openapi.CustomListApi(api_client)
    id = 'id_example' # str | CustomList ID
    content_type = 'application/json' # str |  (default to 'application/json')
    body = None # object |  (optional)

    try:
        # Follow CustomList
        api_response = api_instance.follow_list_id(id, content_type, body=body)
        print("The response of CustomListApi->follow_list_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomListApi->follow_list_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| CustomList ID | 
 **content_type** | **str**|  | [default to &#39;application/json&#39;]
 **body** | **object**|  | [optional] 

### Return type

[**FollowListId200Response**](FollowListId200Response.md)

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

# **get_list_id**
> CustomListResponse get_list_id(id)

Get CustomList

### Example


```python
import mangadex_openapi
from mangadex_openapi.models.custom_list_response import CustomListResponse
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
    api_instance = mangadex_openapi.CustomListApi(api_client)
    id = 'id_example' # str | CustomList ID

    try:
        # Get CustomList
        api_response = api_instance.get_list_id(id)
        print("The response of CustomListApi->get_list_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomListApi->get_list_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| CustomList ID | 

### Return type

[**CustomListResponse**](CustomListResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**404** | CustomList not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_id_list**
> CustomListList get_user_id_list(id, limit=limit, offset=offset)

Get User's CustomList list

This will list only public CustomList

### Example


```python
import mangadex_openapi
from mangadex_openapi.models.custom_list_list import CustomListList
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
    api_instance = mangadex_openapi.CustomListApi(api_client)
    id = 'id_example' # str | User ID
    limit = 10 # int |  (optional) (default to 10)
    offset = 56 # int |  (optional)

    try:
        # Get User's CustomList list
        api_response = api_instance.get_user_id_list(id, limit=limit, offset=offset)
        print("The response of CustomListApi->get_user_id_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomListApi->get_user_id_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| User ID | 
 **limit** | **int**|  | [optional] [default to 10]
 **offset** | **int**|  | [optional] 

### Return type

[**CustomListList**](CustomListList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_list**
> CustomListList get_user_list(limit=limit, offset=offset)

Get logged User CustomList list

This will list public and private CustomList

### Example

* Bearer Authentication (Bearer):

```python
import mangadex_openapi
from mangadex_openapi.models.custom_list_list import CustomListList
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
    api_instance = mangadex_openapi.CustomListApi(api_client)
    limit = 10 # int |  (optional) (default to 10)
    offset = 56 # int |  (optional)

    try:
        # Get logged User CustomList list
        api_response = api_instance.get_user_list(limit=limit, offset=offset)
        print("The response of CustomListApi->get_user_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomListApi->get_user_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**|  | [optional] [default to 10]
 **offset** | **int**|  | [optional] 

### Return type

[**CustomListList**](CustomListList.md)

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

# **post_list**
> CustomListResponse post_list(content_type, custom_list_create=custom_list_create)

Create CustomList

### Example

* Bearer Authentication (Bearer):

```python
import mangadex_openapi
from mangadex_openapi.models.custom_list_create import CustomListCreate
from mangadex_openapi.models.custom_list_response import CustomListResponse
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
    api_instance = mangadex_openapi.CustomListApi(api_client)
    content_type = 'application/json' # str |  (default to 'application/json')
    custom_list_create = mangadex_openapi.CustomListCreate() # CustomListCreate | The size of the body is limited to 8KB. (optional)

    try:
        # Create CustomList
        api_response = api_instance.post_list(content_type, custom_list_create=custom_list_create)
        print("The response of CustomListApi->post_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomListApi->post_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **content_type** | **str**|  | [default to &#39;application/json&#39;]
 **custom_list_create** | [**CustomListCreate**](CustomListCreate.md)| The size of the body is limited to 8KB. | [optional] 

### Return type

[**CustomListResponse**](CustomListResponse.md)

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
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_manga_id_list_list_id**
> Response post_manga_id_list_list_id(id, list_id)

Add Manga in CustomList

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
    api_instance = mangadex_openapi.CustomListApi(api_client)
    id = 'id_example' # str | Manga ID
    list_id = 'list_id_example' # str | CustomList ID

    try:
        # Add Manga in CustomList
        api_response = api_instance.post_manga_id_list_list_id(id, list_id)
        print("The response of CustomListApi->post_manga_id_list_list_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomListApi->post_manga_id_list_list_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Manga ID | 
 **list_id** | **str**| CustomList ID | 

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

# **put_list_id**
> CustomListResponse put_list_id(id, content_type, custom_list_edit=custom_list_edit)

Update CustomList

The size of the body is limited to 8KB.

### Example

* Bearer Authentication (Bearer):

```python
import mangadex_openapi
from mangadex_openapi.models.custom_list_edit import CustomListEdit
from mangadex_openapi.models.custom_list_response import CustomListResponse
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
    api_instance = mangadex_openapi.CustomListApi(api_client)
    id = 'id_example' # str | CustomList ID
    content_type = 'application/json' # str |  (default to 'application/json')
    custom_list_edit = mangadex_openapi.CustomListEdit() # CustomListEdit |  (optional)

    try:
        # Update CustomList
        api_response = api_instance.put_list_id(id, content_type, custom_list_edit=custom_list_edit)
        print("The response of CustomListApi->put_list_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomListApi->put_list_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| CustomList ID | 
 **content_type** | **str**|  | [default to &#39;application/json&#39;]
 **custom_list_edit** | [**CustomListEdit**](CustomListEdit.md)|  | [optional] 

### Return type

[**CustomListResponse**](CustomListResponse.md)

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

# **unfollow_list_id**
> FollowListId200Response unfollow_list_id(id, body=body)

Unfollow CustomList

The request body is empty

### Example

* Bearer Authentication (Bearer):

```python
import mangadex_openapi
from mangadex_openapi.models.follow_list_id200_response import FollowListId200Response
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
    api_instance = mangadex_openapi.CustomListApi(api_client)
    id = 'id_example' # str | CustomList ID
    body = None # object |  (optional)

    try:
        # Unfollow CustomList
        api_response = api_instance.unfollow_list_id(id, body=body)
        print("The response of CustomListApi->unfollow_list_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomListApi->unfollow_list_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| CustomList ID | 
 **body** | **object**|  | [optional] 

### Return type

[**FollowListId200Response**](FollowListId200Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

