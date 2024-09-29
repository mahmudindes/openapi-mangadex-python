# mangadex_openapi.AuthenticationApi

All URIs are relative to *https://api.mangadex.org*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_auth_check**](AuthenticationApi.md#get_auth_check) | **GET** /auth/check | Check the set of permissions associated with the current token
[**post_auth_login**](AuthenticationApi.md#post_auth_login) | **POST** /auth/login | Login
[**post_auth_logout**](AuthenticationApi.md#post_auth_logout) | **POST** /auth/logout | Logout
[**post_auth_refresh**](AuthenticationApi.md#post_auth_refresh) | **POST** /auth/refresh | Refresh token


# **get_auth_check**
> CheckResponse get_auth_check()

Check the set of permissions associated with the current token

The returned list of permissions is computed depending on the generic role permissions that the token user has, their personal overrides, and the OpenID scopes of the token (we do not offer granular token permissions yet) 

### Example

* Bearer Authentication (Bearer):

```python
import mangadex_openapi
from mangadex_openapi.models.check_response import CheckResponse
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
    api_instance = mangadex_openapi.AuthenticationApi(api_client)

    try:
        # Check the set of permissions associated with the current token
        api_response = api_instance.get_auth_check()
        print("The response of AuthenticationApi->get_auth_check:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthenticationApi->get_auth_check: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**CheckResponse**](CheckResponse.md)

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

# **post_auth_login**
> LoginResponse post_auth_login(content_type, login=login)

Login

### Example


```python
import mangadex_openapi
from mangadex_openapi.models.login import Login
from mangadex_openapi.models.login_response import LoginResponse
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
    api_instance = mangadex_openapi.AuthenticationApi(api_client)
    content_type = 'application/json' # str |  (default to 'application/json')
    login = mangadex_openapi.Login() # Login | The size of the body is limited to 2KB. (optional)

    try:
        # Login
        api_response = api_instance.post_auth_login(content_type, login=login)
        print("The response of AuthenticationApi->post_auth_login:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthenticationApi->post_auth_login: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **content_type** | **str**|  | [default to &#39;application/json&#39;]
 **login** | [**Login**](Login.md)| The size of the body is limited to 2KB. | [optional] 

### Return type

[**LoginResponse**](LoginResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_auth_logout**
> LogoutResponse post_auth_logout()

Logout

### Example

* Bearer Authentication (Bearer):

```python
import mangadex_openapi
from mangadex_openapi.models.logout_response import LogoutResponse
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
    api_instance = mangadex_openapi.AuthenticationApi(api_client)

    try:
        # Logout
        api_response = api_instance.post_auth_logout()
        print("The response of AuthenticationApi->post_auth_logout:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthenticationApi->post_auth_logout: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**LogoutResponse**](LogoutResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**503** | Service Unavailable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_auth_refresh**
> RefreshResponse post_auth_refresh(content_type, refresh_token=refresh_token)

Refresh token

### Example


```python
import mangadex_openapi
from mangadex_openapi.models.refresh_response import RefreshResponse
from mangadex_openapi.models.refresh_token import RefreshToken
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
    api_instance = mangadex_openapi.AuthenticationApi(api_client)
    content_type = 'application/json' # str |  (default to 'application/json')
    refresh_token = mangadex_openapi.RefreshToken() # RefreshToken | The size of the body is limited to 2KB. (optional)

    try:
        # Refresh token
        api_response = api_instance.post_auth_refresh(content_type, refresh_token=refresh_token)
        print("The response of AuthenticationApi->post_auth_refresh:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthenticationApi->post_auth_refresh: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **content_type** | **str**|  | [default to &#39;application/json&#39;]
 **refresh_token** | [**RefreshToken**](RefreshToken.md)| The size of the body is limited to 2KB. | [optional] 

### Return type

[**RefreshResponse**](RefreshResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

