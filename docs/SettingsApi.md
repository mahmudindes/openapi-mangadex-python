# mangadex_openapi.SettingsApi

All URIs are relative to *https://api.mangadex.org*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_settings**](SettingsApi.md#get_settings) | **GET** /settings | Get an User Settings
[**get_settings_template**](SettingsApi.md#get_settings_template) | **GET** /settings/template | Get latest Settings template
[**get_settings_template_version**](SettingsApi.md#get_settings_template_version) | **GET** /settings/template/{version} | Get Settings template by version id
[**post_settings**](SettingsApi.md#post_settings) | **POST** /settings | Create or update an User Settings
[**post_settings_template**](SettingsApi.md#post_settings_template) | **POST** /settings/template | Create Settings template


# **get_settings**
> GetSettings200Response get_settings()

Get an User Settings

### Example

* Bearer Authentication (Bearer):

```python
import mangadex_openapi
from mangadex_openapi.models.get_settings200_response import GetSettings200Response
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
    api_instance = mangadex_openapi.SettingsApi(api_client)

    try:
        # Get an User Settings
        api_response = api_instance.get_settings()
        print("The response of SettingsApi->get_settings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SettingsApi->get_settings: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**GetSettings200Response**](GetSettings200Response.md)

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
**404** | Manga no content |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_settings_template**
> object get_settings_template()

Get latest Settings template

### Example

* Bearer Authentication (Bearer):

```python
import mangadex_openapi
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
    api_instance = mangadex_openapi.SettingsApi(api_client)

    try:
        # Get latest Settings template
        api_response = api_instance.get_settings_template()
        print("The response of SettingsApi->get_settings_template:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SettingsApi->get_settings_template: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

**object**

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
**404** | Manga no content |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_settings_template_version**
> object get_settings_template_version(version)

Get Settings template by version id

### Example

* Bearer Authentication (Bearer):

```python
import mangadex_openapi
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
    api_instance = mangadex_openapi.SettingsApi(api_client)
    version = 'version_example' # str | 

    try:
        # Get Settings template by version id
        api_response = api_instance.get_settings_template_version(version)
        print("The response of SettingsApi->get_settings_template_version:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SettingsApi->get_settings_template_version: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**|  | 

### Return type

**object**

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
**404** | Manga no content |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_settings**
> PostSettings200Response post_settings(post_settings_request=post_settings_request)

Create or update an User Settings

### Example

* Bearer Authentication (Bearer):

```python
import mangadex_openapi
from mangadex_openapi.models.post_settings200_response import PostSettings200Response
from mangadex_openapi.models.post_settings_request import PostSettingsRequest
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
    api_instance = mangadex_openapi.SettingsApi(api_client)
    post_settings_request = mangadex_openapi.PostSettingsRequest() # PostSettingsRequest |  (optional)

    try:
        # Create or update an User Settings
        api_response = api_instance.post_settings(post_settings_request=post_settings_request)
        print("The response of SettingsApi->post_settings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SettingsApi->post_settings: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **post_settings_request** | [**PostSettingsRequest**](PostSettingsRequest.md)|  | [optional] 

### Return type

[**PostSettings200Response**](PostSettings200Response.md)

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
**404** | Manga no content |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_settings_template**
> object post_settings_template(body=body)

Create Settings template

### Example

* Bearer Authentication (Bearer):

```python
import mangadex_openapi
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
    api_instance = mangadex_openapi.SettingsApi(api_client)
    body = None # object |  (optional)

    try:
        # Create Settings template
        api_response = api_instance.post_settings_template(body=body)
        print("The response of SettingsApi->post_settings_template:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SettingsApi->post_settings_template: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **object**|  | [optional] 

### Return type

**object**

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

