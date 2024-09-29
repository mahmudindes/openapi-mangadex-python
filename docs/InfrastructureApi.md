# mangadex_openapi.InfrastructureApi

All URIs are relative to *https://api.mangadex.org*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_ping**](InfrastructureApi.md#get_ping) | **GET** /ping | Ping healthcheck


# **get_ping**
> str get_ping()

Ping healthcheck

Returns a plaintext response containing only the word \"pong\" if the API is healthy

### Example


```python
import mangadex_openapi
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
    api_instance = mangadex_openapi.InfrastructureApi(api_client)

    try:
        # Ping healthcheck
        api_response = api_instance.get_ping()
        print("The response of InfrastructureApi->get_ping:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InfrastructureApi->get_ping: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Pong |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

