# mangadex_openapi.FollowsApi

All URIs are relative to *https://api.mangadex.org*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_user_follows_group**](FollowsApi.md#get_user_follows_group) | **GET** /user/follows/group | Get logged User followed Groups
[**get_user_follows_group_id**](FollowsApi.md#get_user_follows_group_id) | **GET** /user/follows/group/{id} | Check if logged User follows a Group
[**get_user_follows_list**](FollowsApi.md#get_user_follows_list) | **GET** /user/follows/list | Get logged User followed CustomList list
[**get_user_follows_list_id**](FollowsApi.md#get_user_follows_list_id) | **GET** /user/follows/list/{id} | Check if logged User follows a CustomList
[**get_user_follows_manga**](FollowsApi.md#get_user_follows_manga) | **GET** /user/follows/manga | Get logged User followed Manga list
[**get_user_follows_manga_id**](FollowsApi.md#get_user_follows_manga_id) | **GET** /user/follows/manga/{id} | Check if logged User follows a Manga
[**get_user_follows_user**](FollowsApi.md#get_user_follows_user) | **GET** /user/follows/user | Get logged User followed User list
[**get_user_follows_user_id**](FollowsApi.md#get_user_follows_user_id) | **GET** /user/follows/user/{id} | Check if logged User follows a User


# **get_user_follows_group**
> ScanlationGroupList get_user_follows_group(limit=limit, offset=offset, includes=includes)

Get logged User followed Groups

### Example

* Bearer Authentication (Bearer):

```python
import mangadex_openapi
from mangadex_openapi.models.scanlation_group_list import ScanlationGroupList
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
    api_instance = mangadex_openapi.FollowsApi(api_client)
    limit = 10 # int |  (optional) (default to 10)
    offset = 56 # int |  (optional)
    includes = ['includes_example'] # List[str] |  (optional)

    try:
        # Get logged User followed Groups
        api_response = api_instance.get_user_follows_group(limit=limit, offset=offset, includes=includes)
        print("The response of FollowsApi->get_user_follows_group:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FollowsApi->get_user_follows_group: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**|  | [optional] [default to 10]
 **offset** | **int**|  | [optional] 
 **includes** | [**List[str]**](str.md)|  | [optional] 

### Return type

[**ScanlationGroupList**](ScanlationGroupList.md)

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

# **get_user_follows_group_id**
> Response get_user_follows_group_id(id)

Check if logged User follows a Group

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
    api_instance = mangadex_openapi.FollowsApi(api_client)
    id = 'id_example' # str | Scanlation Group id

    try:
        # Check if logged User follows a Group
        api_response = api_instance.get_user_follows_group_id(id)
        print("The response of FollowsApi->get_user_follows_group_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FollowsApi->get_user_follows_group_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Scanlation Group id | 

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
**200** | The User follow that Group |  -  |
**404** | The User doesn&#39;t follow that Group |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_follows_list**
> CustomListList get_user_follows_list(limit=limit, offset=offset)

Get logged User followed CustomList list

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
    api_instance = mangadex_openapi.FollowsApi(api_client)
    limit = 10 # int |  (optional) (default to 10)
    offset = 56 # int |  (optional)

    try:
        # Get logged User followed CustomList list
        api_response = api_instance.get_user_follows_list(limit=limit, offset=offset)
        print("The response of FollowsApi->get_user_follows_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FollowsApi->get_user_follows_list: %s\n" % e)
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

# **get_user_follows_list_id**
> Response get_user_follows_list_id(id)

Check if logged User follows a CustomList

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
    api_instance = mangadex_openapi.FollowsApi(api_client)
    id = 'id_example' # str | CustomList id

    try:
        # Check if logged User follows a CustomList
        api_response = api_instance.get_user_follows_list_id(id)
        print("The response of FollowsApi->get_user_follows_list_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FollowsApi->get_user_follows_list_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| CustomList id | 

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
**200** | The User follow that CustomList |  -  |
**404** | The User doesn&#39;t follow that CustomList |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_follows_manga**
> MangaList get_user_follows_manga(limit=limit, offset=offset, includes=includes)

Get logged User followed Manga list

### Example

* Bearer Authentication (Bearer):

```python
import mangadex_openapi
from mangadex_openapi.models.manga_list import MangaList
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
    api_instance = mangadex_openapi.FollowsApi(api_client)
    limit = 10 # int |  (optional) (default to 10)
    offset = 56 # int |  (optional)
    includes = ['includes_example'] # List[str] |  (optional)

    try:
        # Get logged User followed Manga list
        api_response = api_instance.get_user_follows_manga(limit=limit, offset=offset, includes=includes)
        print("The response of FollowsApi->get_user_follows_manga:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FollowsApi->get_user_follows_manga: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**|  | [optional] [default to 10]
 **offset** | **int**|  | [optional] 
 **includes** | [**List[str]**](str.md)|  | [optional] 

### Return type

[**MangaList**](MangaList.md)

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

# **get_user_follows_manga_id**
> Response get_user_follows_manga_id(id)

Check if logged User follows a Manga

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
    api_instance = mangadex_openapi.FollowsApi(api_client)
    id = 'id_example' # str | Manga id

    try:
        # Check if logged User follows a Manga
        api_response = api_instance.get_user_follows_manga_id(id)
        print("The response of FollowsApi->get_user_follows_manga_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FollowsApi->get_user_follows_manga_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Manga id | 

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
**200** | The User follow that Manga |  -  |
**404** | The User doesn&#39;t follow that Manga |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_follows_user**
> UserList get_user_follows_user(limit=limit, offset=offset)

Get logged User followed User list

### Example

* Bearer Authentication (Bearer):

```python
import mangadex_openapi
from mangadex_openapi.models.user_list import UserList
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
    api_instance = mangadex_openapi.FollowsApi(api_client)
    limit = 10 # int |  (optional) (default to 10)
    offset = 56 # int |  (optional)

    try:
        # Get logged User followed User list
        api_response = api_instance.get_user_follows_user(limit=limit, offset=offset)
        print("The response of FollowsApi->get_user_follows_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FollowsApi->get_user_follows_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**|  | [optional] [default to 10]
 **offset** | **int**|  | [optional] 

### Return type

[**UserList**](UserList.md)

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

# **get_user_follows_user_id**
> Response get_user_follows_user_id(id)

Check if logged User follows a User

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
    api_instance = mangadex_openapi.FollowsApi(api_client)
    id = 'id_example' # str | User id

    try:
        # Check if logged User follows a User
        api_response = api_instance.get_user_follows_user_id(id)
        print("The response of FollowsApi->get_user_follows_user_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FollowsApi->get_user_follows_user_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| User id | 

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
**200** | The User follow that User |  -  |
**404** | The User doesn&#39;t follow that User |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

