# mangadex_openapi.StatisticsApi

All URIs are relative to *https://api.mangadex.org*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_statistics_chapter_uuid**](StatisticsApi.md#get_statistics_chapter_uuid) | **GET** /statistics/chapter/{uuid} | Get statistics about given chapter
[**get_statistics_chapters**](StatisticsApi.md#get_statistics_chapters) | **GET** /statistics/chapter | Get statistics about given chapters
[**get_statistics_group_uuid**](StatisticsApi.md#get_statistics_group_uuid) | **GET** /statistics/group/{uuid} | Get statistics about given scanlation group
[**get_statistics_groups**](StatisticsApi.md#get_statistics_groups) | **GET** /statistics/group | Get statistics about given groups
[**get_statistics_manga**](StatisticsApi.md#get_statistics_manga) | **GET** /statistics/manga | Find statistics about given Manga
[**get_statistics_manga_uuid**](StatisticsApi.md#get_statistics_manga_uuid) | **GET** /statistics/manga/{uuid} | Get statistics about given Manga


# **get_statistics_chapter_uuid**
> GetStatisticsChapterUuid200Response get_statistics_chapter_uuid(uuid)

Get statistics about given chapter

### Example

* Bearer Authentication (Bearer):

```python
import mangadex_openapi
from mangadex_openapi.models.get_statistics_chapter_uuid200_response import GetStatisticsChapterUuid200Response
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
    api_instance = mangadex_openapi.StatisticsApi(api_client)
    uuid = 'uuid_example' # str | 

    try:
        # Get statistics about given chapter
        api_response = api_instance.get_statistics_chapter_uuid(uuid)
        print("The response of StatisticsApi->get_statistics_chapter_uuid:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StatisticsApi->get_statistics_chapter_uuid: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**|  | 

### Return type

[**GetStatisticsChapterUuid200Response**](GetStatisticsChapterUuid200Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Statistics |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_statistics_chapters**
> GetStatisticsChapterUuid200Response get_statistics_chapters(chapter)

Get statistics about given chapters

### Example

* Bearer Authentication (Bearer):

```python
import mangadex_openapi
from mangadex_openapi.models.get_statistics_chapter_uuid200_response import GetStatisticsChapterUuid200Response
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
    api_instance = mangadex_openapi.StatisticsApi(api_client)
    chapter = ['chapter_example'] # List[str] | 

    try:
        # Get statistics about given chapters
        api_response = api_instance.get_statistics_chapters(chapter)
        print("The response of StatisticsApi->get_statistics_chapters:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StatisticsApi->get_statistics_chapters: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **chapter** | [**List[str]**](str.md)|  | 

### Return type

[**GetStatisticsChapterUuid200Response**](GetStatisticsChapterUuid200Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Statistics |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_statistics_group_uuid**
> GetStatisticsChapterUuid200Response get_statistics_group_uuid(uuid)

Get statistics about given scanlation group

### Example

* Bearer Authentication (Bearer):

```python
import mangadex_openapi
from mangadex_openapi.models.get_statistics_chapter_uuid200_response import GetStatisticsChapterUuid200Response
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
    api_instance = mangadex_openapi.StatisticsApi(api_client)
    uuid = 'uuid_example' # str | 

    try:
        # Get statistics about given scanlation group
        api_response = api_instance.get_statistics_group_uuid(uuid)
        print("The response of StatisticsApi->get_statistics_group_uuid:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StatisticsApi->get_statistics_group_uuid: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**|  | 

### Return type

[**GetStatisticsChapterUuid200Response**](GetStatisticsChapterUuid200Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Statistics |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_statistics_groups**
> GetStatisticsChapterUuid200Response get_statistics_groups(group)

Get statistics about given groups

### Example

* Bearer Authentication (Bearer):

```python
import mangadex_openapi
from mangadex_openapi.models.get_statistics_chapter_uuid200_response import GetStatisticsChapterUuid200Response
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
    api_instance = mangadex_openapi.StatisticsApi(api_client)
    group = ['group_example'] # List[str] | 

    try:
        # Get statistics about given groups
        api_response = api_instance.get_statistics_groups(group)
        print("The response of StatisticsApi->get_statistics_groups:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StatisticsApi->get_statistics_groups: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group** | [**List[str]**](str.md)|  | 

### Return type

[**GetStatisticsChapterUuid200Response**](GetStatisticsChapterUuid200Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Statistics |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_statistics_manga**
> GetStatisticsManga200Response get_statistics_manga(manga)

Find statistics about given Manga

### Example

* Bearer Authentication (Bearer):

```python
import mangadex_openapi
from mangadex_openapi.models.get_statistics_manga200_response import GetStatisticsManga200Response
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
    api_instance = mangadex_openapi.StatisticsApi(api_client)
    manga = ['manga_example'] # List[str] | 

    try:
        # Find statistics about given Manga
        api_response = api_instance.get_statistics_manga(manga)
        print("The response of StatisticsApi->get_statistics_manga:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StatisticsApi->get_statistics_manga: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **manga** | [**List[str]**](str.md)|  | 

### Return type

[**GetStatisticsManga200Response**](GetStatisticsManga200Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Statistics |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_statistics_manga_uuid**
> GetStatisticsMangaUuid200Response get_statistics_manga_uuid(uuid)

Get statistics about given Manga

### Example

* Bearer Authentication (Bearer):

```python
import mangadex_openapi
from mangadex_openapi.models.get_statistics_manga_uuid200_response import GetStatisticsMangaUuid200Response
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
    api_instance = mangadex_openapi.StatisticsApi(api_client)
    uuid = 'uuid_example' # str | 

    try:
        # Get statistics about given Manga
        api_response = api_instance.get_statistics_manga_uuid(uuid)
        print("The response of StatisticsApi->get_statistics_manga_uuid:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StatisticsApi->get_statistics_manga_uuid: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**|  | 

### Return type

[**GetStatisticsMangaUuid200Response**](GetStatisticsMangaUuid200Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Statistics |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

