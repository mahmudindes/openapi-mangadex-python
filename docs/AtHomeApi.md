# mangadex_openapi.AtHomeApi

All URIs are relative to *https://api.mangadex.org*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_at_home_server_chapter_id**](AtHomeApi.md#get_at_home_server_chapter_id) | **GET** /at-home/server/{chapterId} | Get MangaDex@Home server URL


# **get_at_home_server_chapter_id**
> GetAtHomeServerChapterId200Response get_at_home_server_chapter_id(chapter_id, force_port443=force_port443)

Get MangaDex@Home server URL

### Example


```python
import mangadex_openapi
from mangadex_openapi.models.get_at_home_server_chapter_id200_response import GetAtHomeServerChapterId200Response
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
    api_instance = mangadex_openapi.AtHomeApi(api_client)
    chapter_id = 'chapter_id_example' # str | Chapter ID
    force_port443 = False # bool | Force selecting from MangaDex@Home servers that use the standard HTTPS port 443.  While the conventional port for HTTPS traffic is 443 and servers are encouraged to use it, it is not a hard requirement as it technically isn't anything special.  However, some misbehaving school/office network will at time block traffic to non-standard ports, and setting this flag to `true` will ensure selection of a server that uses these. (optional) (default to False)

    try:
        # Get MangaDex@Home server URL
        api_response = api_instance.get_at_home_server_chapter_id(chapter_id, force_port443=force_port443)
        print("The response of AtHomeApi->get_at_home_server_chapter_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AtHomeApi->get_at_home_server_chapter_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **chapter_id** | **str**| Chapter ID | 
 **force_port443** | **bool**| Force selecting from MangaDex@Home servers that use the standard HTTPS port 443.  While the conventional port for HTTPS traffic is 443 and servers are encouraged to use it, it is not a hard requirement as it technically isn&#39;t anything special.  However, some misbehaving school/office network will at time block traffic to non-standard ports, and setting this flag to &#x60;true&#x60; will ensure selection of a server that uses these. | [optional] [default to False]

### Return type

[**GetAtHomeServerChapterId200Response**](GetAtHomeServerChapterId200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

