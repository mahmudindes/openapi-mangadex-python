# mangadex_openapi.ReadMarkerApi

All URIs are relative to *https://api.mangadex.org*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_manga_chapter_readmarkers**](ReadMarkerApi.md#get_manga_chapter_readmarkers) | **GET** /manga/{id}/read | Manga read markers
[**get_manga_chapter_readmarkers2**](ReadMarkerApi.md#get_manga_chapter_readmarkers2) | **GET** /manga/read | Manga read markers
[**get_reading_history**](ReadMarkerApi.md#get_reading_history) | **GET** /user/history | Get users reading history
[**post_manga_chapter_readmarkers**](ReadMarkerApi.md#post_manga_chapter_readmarkers) | **POST** /manga/{id}/read | Manga read markers batch


# **get_manga_chapter_readmarkers**
> GetMangaChapterReadmarkers200Response get_manga_chapter_readmarkers(id)

Manga read markers

A list of chapter ids that are marked as read for the specified manga

### Example

* Bearer Authentication (Bearer):

```python
import mangadex_openapi
from mangadex_openapi.models.get_manga_chapter_readmarkers200_response import GetMangaChapterReadmarkers200Response
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
    api_instance = mangadex_openapi.ReadMarkerApi(api_client)
    id = 'id_example' # str | 

    try:
        # Manga read markers
        api_response = api_instance.get_manga_chapter_readmarkers(id)
        print("The response of ReadMarkerApi->get_manga_chapter_readmarkers:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReadMarkerApi->get_manga_chapter_readmarkers: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**GetMangaChapterReadmarkers200Response**](GetMangaChapterReadmarkers200Response.md)

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

# **get_manga_chapter_readmarkers2**
> GetMangaChapterReadmarkers2200Response get_manga_chapter_readmarkers2(ids, grouped=grouped)

Manga read markers

A list of chapter ids that are marked as read for the given manga ids

### Example

* Bearer Authentication (Bearer):

```python
import mangadex_openapi
from mangadex_openapi.models.get_manga_chapter_readmarkers2200_response import GetMangaChapterReadmarkers2200Response
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
    api_instance = mangadex_openapi.ReadMarkerApi(api_client)
    ids = ['ids_example'] # List[str] | Manga ids
    grouped = True # bool | Group results by manga ids (optional)

    try:
        # Manga read markers
        api_response = api_instance.get_manga_chapter_readmarkers2(ids, grouped=grouped)
        print("The response of ReadMarkerApi->get_manga_chapter_readmarkers2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReadMarkerApi->get_manga_chapter_readmarkers2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ids** | [**List[str]**](str.md)| Manga ids | 
 **grouped** | **bool**| Group results by manga ids | [optional] 

### Return type

[**GetMangaChapterReadmarkers2200Response**](GetMangaChapterReadmarkers2200Response.md)

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

# **get_reading_history**
> GetReadingHistory200Response get_reading_history()

Get users reading history

### Example

* Bearer Authentication (Bearer):

```python
import mangadex_openapi
from mangadex_openapi.models.get_reading_history200_response import GetReadingHistory200Response
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
    api_instance = mangadex_openapi.ReadMarkerApi(api_client)

    try:
        # Get users reading history
        api_response = api_instance.get_reading_history()
        print("The response of ReadMarkerApi->get_reading_history:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReadMarkerApi->get_reading_history: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**GetReadingHistory200Response**](GetReadingHistory200Response.md)

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

# **post_manga_chapter_readmarkers**
> FollowListId200Response post_manga_chapter_readmarkers(id, update_history=update_history, chapter_read_marker_batch=chapter_read_marker_batch)

Manga read markers batch

Send a lot of chapter ids for one manga to mark as read and/or unread

### Example

* Bearer Authentication (Bearer):

```python
import mangadex_openapi
from mangadex_openapi.models.chapter_read_marker_batch import ChapterReadMarkerBatch
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
    api_instance = mangadex_openapi.ReadMarkerApi(api_client)
    id = 'id_example' # str | 
    update_history = True # bool | Adding this will cause the chapter to be stored in the user's reading history (optional)
    chapter_read_marker_batch = mangadex_openapi.ChapterReadMarkerBatch() # ChapterReadMarkerBatch | The size of the body is limited to 10KB. (optional)

    try:
        # Manga read markers batch
        api_response = api_instance.post_manga_chapter_readmarkers(id, update_history=update_history, chapter_read_marker_batch=chapter_read_marker_batch)
        print("The response of ReadMarkerApi->post_manga_chapter_readmarkers:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReadMarkerApi->post_manga_chapter_readmarkers: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **update_history** | **bool**| Adding this will cause the chapter to be stored in the user&#39;s reading history | [optional] 
 **chapter_read_marker_batch** | [**ChapterReadMarkerBatch**](ChapterReadMarkerBatch.md)| The size of the body is limited to 10KB. | [optional] 

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

