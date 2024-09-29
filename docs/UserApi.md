# mangadex_openapi.UserApi

All URIs are relative to *https://api.mangadex.org*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_user_id**](UserApi.md#delete_user_id) | **DELETE** /user/{id} | Delete User
[**get_user**](UserApi.md#get_user) | **GET** /user | User list
[**get_user_id**](UserApi.md#get_user_id) | **GET** /user/{id} | Get User
[**get_user_me**](UserApi.md#get_user_me) | **GET** /user/me | Logged User details
[**post_user_delete_code**](UserApi.md#post_user_delete_code) | **POST** /user/delete/{code} | Approve User deletion


# **delete_user_id**
> Response delete_user_id(id)

Delete User

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
    api_instance = mangadex_openapi.UserApi(api_client)
    id = 'id_example' # str | User ID

    try:
        # Delete User
        api_response = api_instance.delete_user_id(id)
        print("The response of UserApi->delete_user_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->delete_user_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| User ID | 

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user**
> UserList get_user(limit=limit, offset=offset, ids=ids, username=username, order=order)

User list

### Example

* Bearer Authentication (Bearer):

```python
import mangadex_openapi
from mangadex_openapi.models.get_user_order_parameter import GetUserOrderParameter
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
    api_instance = mangadex_openapi.UserApi(api_client)
    limit = 10 # int |  (optional) (default to 10)
    offset = 56 # int |  (optional)
    ids = ['ids_example'] # List[str] | User ids (limited to 100 per request) (optional)
    username = 'username_example' # str |  (optional)
    order = mangadex_openapi.GetUserOrderParameter() # GetUserOrderParameter |  (optional)

    try:
        # User list
        api_response = api_instance.get_user(limit=limit, offset=offset, ids=ids, username=username, order=order)
        print("The response of UserApi->get_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->get_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**|  | [optional] [default to 10]
 **offset** | **int**|  | [optional] 
 **ids** | [**List[str]**](str.md)| User ids (limited to 100 per request) | [optional] 
 **username** | **str**|  | [optional] 
 **order** | [**GetUserOrderParameter**](.md)|  | [optional] 

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

# **get_user_id**
> UserResponse get_user_id(id)

Get User

### Example


```python
import mangadex_openapi
from mangadex_openapi.models.user_response import UserResponse
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
    api_instance = mangadex_openapi.UserApi(api_client)
    id = 'id_example' # str | User ID

    try:
        # Get User
        api_response = api_instance.get_user_id(id)
        print("The response of UserApi->get_user_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->get_user_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| User ID | 

### Return type

[**UserResponse**](UserResponse.md)

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

# **get_user_me**
> UserResponse get_user_me()

Logged User details

### Example

* Bearer Authentication (Bearer):

```python
import mangadex_openapi
from mangadex_openapi.models.user_response import UserResponse
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
    api_instance = mangadex_openapi.UserApi(api_client)

    try:
        # Logged User details
        api_response = api_instance.get_user_me()
        print("The response of UserApi->get_user_me:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->get_user_me: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**UserResponse**](UserResponse.md)

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

# **post_user_delete_code**
> Response post_user_delete_code(code)

Approve User deletion

### Example


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


# Enter a context with an instance of the API client
with mangadex_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = mangadex_openapi.UserApi(api_client)
    code = 'code_example' # str | User delete code

    try:
        # Approve User deletion
        api_response = api_instance.post_user_delete_code(code)
        print("The response of UserApi->post_user_delete_code:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->post_user_delete_code: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **code** | **str**| User delete code | 

### Return type

[**Response**](Response.md)

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

