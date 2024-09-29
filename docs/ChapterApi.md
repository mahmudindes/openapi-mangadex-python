# mangadex_openapi.ChapterApi

All URIs are relative to *https://api.mangadex.org*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_chapter_id**](ChapterApi.md#delete_chapter_id) | **DELETE** /chapter/{id} | Delete Chapter
[**get_chapter**](ChapterApi.md#get_chapter) | **GET** /chapter | Chapter list
[**get_chapter_id**](ChapterApi.md#get_chapter_id) | **GET** /chapter/{id} | Get Chapter
[**put_chapter_id**](ChapterApi.md#put_chapter_id) | **PUT** /chapter/{id} | Update Chapter


# **delete_chapter_id**
> Response delete_chapter_id(id)

Delete Chapter

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
    api_instance = mangadex_openapi.ChapterApi(api_client)
    id = 'id_example' # str | Chapter ID

    try:
        # Delete Chapter
        api_response = api_instance.delete_chapter_id(id)
        print("The response of ChapterApi->delete_chapter_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ChapterApi->delete_chapter_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Chapter ID | 

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
**200** | Chapter has been deleted. |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_chapter**
> ChapterList get_chapter(limit=limit, offset=offset, ids=ids, title=title, groups=groups, uploader=uploader, manga=manga, volume=volume, chapter=chapter, translated_language=translated_language, original_language=original_language, excluded_original_language=excluded_original_language, content_rating=content_rating, excluded_groups=excluded_groups, excluded_uploaders=excluded_uploaders, include_future_updates=include_future_updates, include_empty_pages=include_empty_pages, include_future_publish_at=include_future_publish_at, include_external_url=include_external_url, created_at_since=created_at_since, updated_at_since=updated_at_since, publish_at_since=publish_at_since, order=order, includes=includes)

Chapter list

Chapter list. If you want the Chapters of a given Manga, please check the feed endpoints.

### Example


```python
import mangadex_openapi
from mangadex_openapi.models.chapter_list import ChapterList
from mangadex_openapi.models.get_chapter_order_parameter import GetChapterOrderParameter
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
    api_instance = mangadex_openapi.ChapterApi(api_client)
    limit = 10 # int |  (optional) (default to 10)
    offset = 56 # int |  (optional)
    ids = ['ids_example'] # List[str] | Chapter ids (limited to 100 per request) (optional)
    title = 'title_example' # str |  (optional)
    groups = ['groups_example'] # List[str] |  (optional)
    uploader = mangadex_openapi.GetChapterUploaderParameter() # GetChapterUploaderParameter |  (optional)
    manga = 'manga_example' # str |  (optional)
    volume = mangadex_openapi.GetChapterVolumeParameter() # GetChapterVolumeParameter |  (optional)
    chapter = mangadex_openapi.GetChapterVolumeParameter() # GetChapterVolumeParameter |  (optional)
    translated_language = ['translated_language_example'] # List[str] |  (optional)
    original_language = ['original_language_example'] # List[str] |  (optional)
    excluded_original_language = ['excluded_original_language_example'] # List[str] |  (optional)
    content_rating = ["safe","suggestive","erotica"] # List[str] |  (optional) (default to ["safe","suggestive","erotica"])
    excluded_groups = ['excluded_groups_example'] # List[str] |  (optional)
    excluded_uploaders = ['excluded_uploaders_example'] # List[str] |  (optional)
    include_future_updates = '1' # str |  (optional) (default to '1')
    include_empty_pages = 56 # int |  (optional)
    include_future_publish_at = 56 # int |  (optional)
    include_external_url = 56 # int |  (optional)
    created_at_since = 'created_at_since_example' # str |  (optional)
    updated_at_since = 'updated_at_since_example' # str |  (optional)
    publish_at_since = 'publish_at_since_example' # str |  (optional)
    order = mangadex_openapi.GetChapterOrderParameter() # GetChapterOrderParameter |  (optional)
    includes = ['includes_example'] # List[str] |  (optional)

    try:
        # Chapter list
        api_response = api_instance.get_chapter(limit=limit, offset=offset, ids=ids, title=title, groups=groups, uploader=uploader, manga=manga, volume=volume, chapter=chapter, translated_language=translated_language, original_language=original_language, excluded_original_language=excluded_original_language, content_rating=content_rating, excluded_groups=excluded_groups, excluded_uploaders=excluded_uploaders, include_future_updates=include_future_updates, include_empty_pages=include_empty_pages, include_future_publish_at=include_future_publish_at, include_external_url=include_external_url, created_at_since=created_at_since, updated_at_since=updated_at_since, publish_at_since=publish_at_since, order=order, includes=includes)
        print("The response of ChapterApi->get_chapter:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ChapterApi->get_chapter: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**|  | [optional] [default to 10]
 **offset** | **int**|  | [optional] 
 **ids** | [**List[str]**](str.md)| Chapter ids (limited to 100 per request) | [optional] 
 **title** | **str**|  | [optional] 
 **groups** | [**List[str]**](str.md)|  | [optional] 
 **uploader** | [**GetChapterUploaderParameter**](.md)|  | [optional] 
 **manga** | **str**|  | [optional] 
 **volume** | [**GetChapterVolumeParameter**](.md)|  | [optional] 
 **chapter** | [**GetChapterVolumeParameter**](.md)|  | [optional] 
 **translated_language** | [**List[str]**](str.md)|  | [optional] 
 **original_language** | [**List[str]**](str.md)|  | [optional] 
 **excluded_original_language** | [**List[str]**](str.md)|  | [optional] 
 **content_rating** | [**List[str]**](str.md)|  | [optional] [default to [&quot;safe&quot;,&quot;suggestive&quot;,&quot;erotica&quot;]]
 **excluded_groups** | [**List[str]**](str.md)|  | [optional] 
 **excluded_uploaders** | [**List[str]**](str.md)|  | [optional] 
 **include_future_updates** | **str**|  | [optional] [default to &#39;1&#39;]
 **include_empty_pages** | **int**|  | [optional] 
 **include_future_publish_at** | **int**|  | [optional] 
 **include_external_url** | **int**|  | [optional] 
 **created_at_since** | **str**|  | [optional] 
 **updated_at_since** | **str**|  | [optional] 
 **publish_at_since** | **str**|  | [optional] 
 **order** | [**GetChapterOrderParameter**](.md)|  | [optional] 
 **includes** | [**List[str]**](str.md)|  | [optional] 

### Return type

[**ChapterList**](ChapterList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Chapter list |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_chapter_id**
> ChapterResponse get_chapter_id(id, includes=includes)

Get Chapter

### Example


```python
import mangadex_openapi
from mangadex_openapi.models.chapter_response import ChapterResponse
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
    api_instance = mangadex_openapi.ChapterApi(api_client)
    id = 'id_example' # str | Chapter ID
    includes = ['includes_example'] # List[str] |  (optional)

    try:
        # Get Chapter
        api_response = api_instance.get_chapter_id(id, includes=includes)
        print("The response of ChapterApi->get_chapter_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ChapterApi->get_chapter_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Chapter ID | 
 **includes** | [**List[str]**](str.md)|  | [optional] 

### Return type

[**ChapterResponse**](ChapterResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**403** | Forbidden |  -  |
**404** | Chapter not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_chapter_id**
> ChapterResponse put_chapter_id(id, content_type, chapter_edit=chapter_edit)

Update Chapter

### Example

* Bearer Authentication (Bearer):

```python
import mangadex_openapi
from mangadex_openapi.models.chapter_edit import ChapterEdit
from mangadex_openapi.models.chapter_response import ChapterResponse
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
    api_instance = mangadex_openapi.ChapterApi(api_client)
    id = 'id_example' # str | Chapter ID
    content_type = 'application/json' # str |  (default to 'application/json')
    chapter_edit = mangadex_openapi.ChapterEdit() # ChapterEdit | The size of the body is limited to 32KB. (optional)

    try:
        # Update Chapter
        api_response = api_instance.put_chapter_id(id, content_type, chapter_edit=chapter_edit)
        print("The response of ChapterApi->put_chapter_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ChapterApi->put_chapter_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Chapter ID | 
 **content_type** | **str**|  | [default to &#39;application/json&#39;]
 **chapter_edit** | [**ChapterEdit**](ChapterEdit.md)| The size of the body is limited to 32KB. | [optional] 

### Return type

[**ChapterResponse**](ChapterResponse.md)

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

