# mangadex_openapi.FeedApi

All URIs are relative to *https://api.mangadex.org*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_list_id_feed**](FeedApi.md#get_list_id_feed) | **GET** /list/{id}/feed | CustomList Manga feed
[**get_user_follows_manga_feed**](FeedApi.md#get_user_follows_manga_feed) | **GET** /user/follows/manga/feed | Get logged User followed Manga feed (Chapter list)


# **get_list_id_feed**
> ChapterList get_list_id_feed(id, limit=limit, offset=offset, translated_language=translated_language, original_language=original_language, excluded_original_language=excluded_original_language, content_rating=content_rating, excluded_groups=excluded_groups, excluded_uploaders=excluded_uploaders, include_future_updates=include_future_updates, created_at_since=created_at_since, updated_at_since=updated_at_since, publish_at_since=publish_at_since, order=order, includes=includes, include_empty_pages=include_empty_pages, include_future_publish_at=include_future_publish_at, include_external_url=include_external_url)

CustomList Manga feed

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
    api_instance = mangadex_openapi.FeedApi(api_client)
    id = 'id_example' # str | 
    limit = 100 # int |  (optional) (default to 100)
    offset = 56 # int |  (optional)
    translated_language = ['translated_language_example'] # List[str] |  (optional)
    original_language = ['original_language_example'] # List[str] |  (optional)
    excluded_original_language = ['excluded_original_language_example'] # List[str] |  (optional)
    content_rating = ["safe","suggestive","erotica"] # List[str] |  (optional) (default to ["safe","suggestive","erotica"])
    excluded_groups = ['excluded_groups_example'] # List[str] |  (optional)
    excluded_uploaders = ['excluded_uploaders_example'] # List[str] |  (optional)
    include_future_updates = '1' # str |  (optional) (default to '1')
    created_at_since = 'created_at_since_example' # str |  (optional)
    updated_at_since = 'updated_at_since_example' # str |  (optional)
    publish_at_since = 'publish_at_since_example' # str |  (optional)
    order = mangadex_openapi.GetChapterOrderParameter() # GetChapterOrderParameter |  (optional)
    includes = ['includes_example'] # List[str] |  (optional)
    include_empty_pages = 56 # int |  (optional)
    include_future_publish_at = 56 # int |  (optional)
    include_external_url = 56 # int |  (optional)

    try:
        # CustomList Manga feed
        api_response = api_instance.get_list_id_feed(id, limit=limit, offset=offset, translated_language=translated_language, original_language=original_language, excluded_original_language=excluded_original_language, content_rating=content_rating, excluded_groups=excluded_groups, excluded_uploaders=excluded_uploaders, include_future_updates=include_future_updates, created_at_since=created_at_since, updated_at_since=updated_at_since, publish_at_since=publish_at_since, order=order, includes=includes, include_empty_pages=include_empty_pages, include_future_publish_at=include_future_publish_at, include_external_url=include_external_url)
        print("The response of FeedApi->get_list_id_feed:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FeedApi->get_list_id_feed: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **limit** | **int**|  | [optional] [default to 100]
 **offset** | **int**|  | [optional] 
 **translated_language** | [**List[str]**](str.md)|  | [optional] 
 **original_language** | [**List[str]**](str.md)|  | [optional] 
 **excluded_original_language** | [**List[str]**](str.md)|  | [optional] 
 **content_rating** | [**List[str]**](str.md)|  | [optional] [default to [&quot;safe&quot;,&quot;suggestive&quot;,&quot;erotica&quot;]]
 **excluded_groups** | [**List[str]**](str.md)|  | [optional] 
 **excluded_uploaders** | [**List[str]**](str.md)|  | [optional] 
 **include_future_updates** | **str**|  | [optional] [default to &#39;1&#39;]
 **created_at_since** | **str**|  | [optional] 
 **updated_at_since** | **str**|  | [optional] 
 **publish_at_since** | **str**|  | [optional] 
 **order** | [**GetChapterOrderParameter**](.md)|  | [optional] 
 **includes** | [**List[str]**](str.md)|  | [optional] 
 **include_empty_pages** | **int**|  | [optional] 
 **include_future_publish_at** | **int**|  | [optional] 
 **include_external_url** | **int**|  | [optional] 

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
**200** | OK |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_follows_manga_feed**
> ChapterList get_user_follows_manga_feed(limit=limit, offset=offset, translated_language=translated_language, original_language=original_language, excluded_original_language=excluded_original_language, content_rating=content_rating, excluded_groups=excluded_groups, excluded_uploaders=excluded_uploaders, include_future_updates=include_future_updates, created_at_since=created_at_since, updated_at_since=updated_at_since, publish_at_since=publish_at_since, order=order, includes=includes, include_empty_pages=include_empty_pages, include_future_publish_at=include_future_publish_at, include_external_url=include_external_url)

Get logged User followed Manga feed (Chapter list)

### Example

* Bearer Authentication (Bearer):

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
    api_instance = mangadex_openapi.FeedApi(api_client)
    limit = 100 # int |  (optional) (default to 100)
    offset = 56 # int |  (optional)
    translated_language = ['translated_language_example'] # List[str] |  (optional)
    original_language = ['original_language_example'] # List[str] |  (optional)
    excluded_original_language = ['excluded_original_language_example'] # List[str] |  (optional)
    content_rating = ["safe","suggestive","erotica"] # List[str] |  (optional) (default to ["safe","suggestive","erotica"])
    excluded_groups = ['excluded_groups_example'] # List[str] |  (optional)
    excluded_uploaders = ['excluded_uploaders_example'] # List[str] |  (optional)
    include_future_updates = '1' # str |  (optional) (default to '1')
    created_at_since = 'created_at_since_example' # str |  (optional)
    updated_at_since = 'updated_at_since_example' # str |  (optional)
    publish_at_since = 'publish_at_since_example' # str |  (optional)
    order = mangadex_openapi.GetChapterOrderParameter() # GetChapterOrderParameter |  (optional)
    includes = ['includes_example'] # List[str] |  (optional)
    include_empty_pages = 56 # int |  (optional)
    include_future_publish_at = 56 # int |  (optional)
    include_external_url = 56 # int |  (optional)

    try:
        # Get logged User followed Manga feed (Chapter list)
        api_response = api_instance.get_user_follows_manga_feed(limit=limit, offset=offset, translated_language=translated_language, original_language=original_language, excluded_original_language=excluded_original_language, content_rating=content_rating, excluded_groups=excluded_groups, excluded_uploaders=excluded_uploaders, include_future_updates=include_future_updates, created_at_since=created_at_since, updated_at_since=updated_at_since, publish_at_since=publish_at_since, order=order, includes=includes, include_empty_pages=include_empty_pages, include_future_publish_at=include_future_publish_at, include_external_url=include_external_url)
        print("The response of FeedApi->get_user_follows_manga_feed:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FeedApi->get_user_follows_manga_feed: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**|  | [optional] [default to 100]
 **offset** | **int**|  | [optional] 
 **translated_language** | [**List[str]**](str.md)|  | [optional] 
 **original_language** | [**List[str]**](str.md)|  | [optional] 
 **excluded_original_language** | [**List[str]**](str.md)|  | [optional] 
 **content_rating** | [**List[str]**](str.md)|  | [optional] [default to [&quot;safe&quot;,&quot;suggestive&quot;,&quot;erotica&quot;]]
 **excluded_groups** | [**List[str]**](str.md)|  | [optional] 
 **excluded_uploaders** | [**List[str]**](str.md)|  | [optional] 
 **include_future_updates** | **str**|  | [optional] [default to &#39;1&#39;]
 **created_at_since** | **str**|  | [optional] 
 **updated_at_since** | **str**|  | [optional] 
 **publish_at_since** | **str**|  | [optional] 
 **order** | [**GetChapterOrderParameter**](.md)|  | [optional] 
 **includes** | [**List[str]**](str.md)|  | [optional] 
 **include_empty_pages** | **int**|  | [optional] 
 **include_future_publish_at** | **int**|  | [optional] 
 **include_external_url** | **int**|  | [optional] 

### Return type

[**ChapterList**](ChapterList.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**404** | User not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

