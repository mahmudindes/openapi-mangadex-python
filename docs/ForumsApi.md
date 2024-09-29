# mangadex_openapi.ForumsApi

All URIs are relative to *https://api.mangadex.org*

Method | HTTP request | Description
------------- | ------------- | -------------
[**forums_thread_create**](ForumsApi.md#forums_thread_create) | **POST** /forums/thread | Create forums thread


# **forums_thread_create**
> ForumsThreadResponse forums_thread_create(forums_thread_create_request=forums_thread_create_request)

Create forums thread

Creates a thread in the forums for the given resource, which backs the comments functionality. A thread is only created if it doesn't exist yet; otherwise the preexisting thread is returned. 

### Example

* Bearer Authentication (Bearer):

```python
import mangadex_openapi
from mangadex_openapi.models.forums_thread_create_request import ForumsThreadCreateRequest
from mangadex_openapi.models.forums_thread_response import ForumsThreadResponse
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
    api_instance = mangadex_openapi.ForumsApi(api_client)
    forums_thread_create_request = mangadex_openapi.ForumsThreadCreateRequest() # ForumsThreadCreateRequest |  (optional)

    try:
        # Create forums thread
        api_response = api_instance.forums_thread_create(forums_thread_create_request=forums_thread_create_request)
        print("The response of ForumsApi->forums_thread_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ForumsApi->forums_thread_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **forums_thread_create_request** | [**ForumsThreadCreateRequest**](ForumsThreadCreateRequest.md)|  | [optional] 

### Return type

[**ForumsThreadResponse**](ForumsThreadResponse.md)

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
**404** | If the resource for which the thread creation was requested does not exist |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

