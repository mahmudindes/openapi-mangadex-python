# mangadex_openapi.MangaApi

All URIs are relative to *https://api.mangadex.org*

Method | HTTP request | Description
------------- | ------------- | -------------
[**commit_manga_draft**](MangaApi.md#commit_manga_draft) | **POST** /manga/draft/{id}/commit | Submit a Manga Draft
[**delete_manga_id**](MangaApi.md#delete_manga_id) | **DELETE** /manga/{id} | Delete Manga
[**delete_manga_id_follow**](MangaApi.md#delete_manga_id_follow) | **DELETE** /manga/{id}/follow | Unfollow Manga
[**delete_manga_relation_id**](MangaApi.md#delete_manga_relation_id) | **DELETE** /manga/{mangaId}/relation/{id} | Delete Manga relation
[**get_manga_aggregate**](MangaApi.md#get_manga_aggregate) | **GET** /manga/{id}/aggregate | Get Manga volumes &amp; chapters
[**get_manga_drafts**](MangaApi.md#get_manga_drafts) | **GET** /manga/draft | Get a list of Manga Drafts
[**get_manga_id**](MangaApi.md#get_manga_id) | **GET** /manga/{id} | Get Manga
[**get_manga_id_draft**](MangaApi.md#get_manga_id_draft) | **GET** /manga/draft/{id} | Get a specific Manga Draft
[**get_manga_id_feed**](MangaApi.md#get_manga_id_feed) | **GET** /manga/{id}/feed | Manga feed
[**get_manga_id_status**](MangaApi.md#get_manga_id_status) | **GET** /manga/{id}/status | Get a Manga reading status
[**get_manga_random**](MangaApi.md#get_manga_random) | **GET** /manga/random | Get a random Manga
[**get_manga_relation**](MangaApi.md#get_manga_relation) | **GET** /manga/{mangaId}/relation | Manga relation list
[**get_manga_status**](MangaApi.md#get_manga_status) | **GET** /manga/status | Get all Manga reading status for logged User
[**get_manga_tag**](MangaApi.md#get_manga_tag) | **GET** /manga/tag | Tag list
[**get_search_manga**](MangaApi.md#get_search_manga) | **GET** /manga | Manga list
[**post_manga**](MangaApi.md#post_manga) | **POST** /manga | Create Manga
[**post_manga_id_follow**](MangaApi.md#post_manga_id_follow) | **POST** /manga/{id}/follow | Follow Manga
[**post_manga_id_status**](MangaApi.md#post_manga_id_status) | **POST** /manga/{id}/status | Update Manga reading status
[**post_manga_relation**](MangaApi.md#post_manga_relation) | **POST** /manga/{mangaId}/relation | Create Manga relation
[**put_manga_id**](MangaApi.md#put_manga_id) | **PUT** /manga/{id} | Update Manga


# **commit_manga_draft**
> MangaResponse commit_manga_draft(id, commit_manga_draft_request=commit_manga_draft_request)

Submit a Manga Draft

### Example

* Bearer Authentication (Bearer):

```python
import mangadex_openapi
from mangadex_openapi.models.commit_manga_draft_request import CommitMangaDraftRequest
from mangadex_openapi.models.manga_response import MangaResponse
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
    api_instance = mangadex_openapi.MangaApi(api_client)
    id = 'id_example' # str | 
    commit_manga_draft_request = mangadex_openapi.CommitMangaDraftRequest() # CommitMangaDraftRequest | A Manga Draft that is to be submitted must have at least one cover in the original language, must be in the \"draft\" state and must be passed the correct version in the request body. (optional)

    try:
        # Submit a Manga Draft
        api_response = api_instance.commit_manga_draft(id, commit_manga_draft_request=commit_manga_draft_request)
        print("The response of MangaApi->commit_manga_draft:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MangaApi->commit_manga_draft: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **commit_manga_draft_request** | [**CommitMangaDraftRequest**](CommitMangaDraftRequest.md)| A Manga Draft that is to be submitted must have at least one cover in the original language, must be in the \&quot;draft\&quot; state and must be passed the correct version in the request body. | [optional] 

### Return type

[**MangaResponse**](MangaResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | OK |  -  |
**400** | BadRequest |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_manga_id**
> Response delete_manga_id(id)

Delete Manga

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
    api_instance = mangadex_openapi.MangaApi(api_client)
    id = 'id_example' # str | Manga ID

    try:
        # Delete Manga
        api_response = api_instance.delete_manga_id(id)
        print("The response of MangaApi->delete_manga_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MangaApi->delete_manga_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Manga ID | 

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
**200** | Manga has been deleted. |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_manga_id_follow**
> Response delete_manga_id_follow(id)

Unfollow Manga

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
    api_instance = mangadex_openapi.MangaApi(api_client)
    id = 'id_example' # str | 

    try:
        # Unfollow Manga
        api_response = api_instance.delete_manga_id_follow(id)
        print("The response of MangaApi->delete_manga_id_follow:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MangaApi->delete_manga_id_follow: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

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
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_manga_relation_id**
> Response delete_manga_relation_id(manga_id, id)

Delete Manga relation

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
    api_instance = mangadex_openapi.MangaApi(api_client)
    manga_id = 'manga_id_example' # str | 
    id = 'id_example' # str | 

    try:
        # Delete Manga relation
        api_response = api_instance.delete_manga_relation_id(manga_id, id)
        print("The response of MangaApi->delete_manga_relation_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MangaApi->delete_manga_relation_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **manga_id** | **str**|  | 
 **id** | **str**|  | 

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
**200** | Manga relation has been deleted. |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_manga_aggregate**
> GetMangaAggregate200Response get_manga_aggregate(id, translated_language=translated_language, groups=groups)

Get Manga volumes & chapters

### Example


```python
import mangadex_openapi
from mangadex_openapi.models.get_manga_aggregate200_response import GetMangaAggregate200Response
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
    api_instance = mangadex_openapi.MangaApi(api_client)
    id = 'id_example' # str | Manga ID
    translated_language = ['translated_language_example'] # List[str] |  (optional)
    groups = ['groups_example'] # List[str] |  (optional)

    try:
        # Get Manga volumes & chapters
        api_response = api_instance.get_manga_aggregate(id, translated_language=translated_language, groups=groups)
        print("The response of MangaApi->get_manga_aggregate:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MangaApi->get_manga_aggregate: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Manga ID | 
 **translated_language** | [**List[str]**](str.md)|  | [optional] 
 **groups** | [**List[str]**](str.md)|  | [optional] 

### Return type

[**GetMangaAggregate200Response**](GetMangaAggregate200Response.md)

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

# **get_manga_drafts**
> MangaResponse get_manga_drafts(limit=limit, offset=offset, state=state, order=order, includes=includes)

Get a list of Manga Drafts

### Example

* Bearer Authentication (Bearer):

```python
import mangadex_openapi
from mangadex_openapi.models.get_manga_drafts_order_parameter import GetMangaDraftsOrderParameter
from mangadex_openapi.models.manga_response import MangaResponse
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
    api_instance = mangadex_openapi.MangaApi(api_client)
    limit = 10 # int |  (optional) (default to 10)
    offset = 56 # int |  (optional)
    state = 'state_example' # str |  (optional)
    order = mangadex_openapi.GetMangaDraftsOrderParameter() # GetMangaDraftsOrderParameter |  (optional)
    includes = ['includes_example'] # List[str] |  (optional)

    try:
        # Get a list of Manga Drafts
        api_response = api_instance.get_manga_drafts(limit=limit, offset=offset, state=state, order=order, includes=includes)
        print("The response of MangaApi->get_manga_drafts:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MangaApi->get_manga_drafts: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**|  | [optional] [default to 10]
 **offset** | **int**|  | [optional] 
 **state** | **str**|  | [optional] 
 **order** | [**GetMangaDraftsOrderParameter**](.md)|  | [optional] 
 **includes** | [**List[str]**](str.md)|  | [optional] 

### Return type

[**MangaResponse**](MangaResponse.md)

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
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_manga_id**
> MangaResponse get_manga_id(id, includes=includes)

Get Manga

Get Manga.

### Example


```python
import mangadex_openapi
from mangadex_openapi.models.manga_response import MangaResponse
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
    api_instance = mangadex_openapi.MangaApi(api_client)
    id = 'id_example' # str | Manga ID
    includes = ['includes_example'] # List[str] |  (optional)

    try:
        # Get Manga
        api_response = api_instance.get_manga_id(id, includes=includes)
        print("The response of MangaApi->get_manga_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MangaApi->get_manga_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Manga ID | 
 **includes** | [**List[str]**](str.md)|  | [optional] 

### Return type

[**MangaResponse**](MangaResponse.md)

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
**404** | Manga no content |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_manga_id_draft**
> MangaResponse get_manga_id_draft(id, includes=includes)

Get a specific Manga Draft

### Example

* Bearer Authentication (Bearer):

```python
import mangadex_openapi
from mangadex_openapi.models.manga_response import MangaResponse
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
    api_instance = mangadex_openapi.MangaApi(api_client)
    id = 'id_example' # str | 
    includes = ['includes_example'] # List[str] |  (optional)

    try:
        # Get a specific Manga Draft
        api_response = api_instance.get_manga_id_draft(id, includes=includes)
        print("The response of MangaApi->get_manga_id_draft:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MangaApi->get_manga_id_draft: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **includes** | [**List[str]**](str.md)|  | [optional] 

### Return type

[**MangaResponse**](MangaResponse.md)

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
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_manga_id_feed**
> ChapterList get_manga_id_feed(id, limit=limit, offset=offset, translated_language=translated_language, original_language=original_language, excluded_original_language=excluded_original_language, content_rating=content_rating, excluded_groups=excluded_groups, excluded_uploaders=excluded_uploaders, include_future_updates=include_future_updates, created_at_since=created_at_since, updated_at_since=updated_at_since, publish_at_since=publish_at_since, order=order, includes=includes, include_empty_pages=include_empty_pages, include_future_publish_at=include_future_publish_at, include_external_url=include_external_url)

Manga feed

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
    api_instance = mangadex_openapi.MangaApi(api_client)
    id = 'id_example' # str | Manga ID
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
        # Manga feed
        api_response = api_instance.get_manga_id_feed(id, limit=limit, offset=offset, translated_language=translated_language, original_language=original_language, excluded_original_language=excluded_original_language, content_rating=content_rating, excluded_groups=excluded_groups, excluded_uploaders=excluded_uploaders, include_future_updates=include_future_updates, created_at_since=created_at_since, updated_at_since=updated_at_since, publish_at_since=publish_at_since, order=order, includes=includes, include_empty_pages=include_empty_pages, include_future_publish_at=include_future_publish_at, include_external_url=include_external_url)
        print("The response of MangaApi->get_manga_id_feed:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MangaApi->get_manga_id_feed: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Manga ID | 
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_manga_id_status**
> GetMangaIdStatus200Response get_manga_id_status(id)

Get a Manga reading status

### Example

* Bearer Authentication (Bearer):

```python
import mangadex_openapi
from mangadex_openapi.models.get_manga_id_status200_response import GetMangaIdStatus200Response
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
    api_instance = mangadex_openapi.MangaApi(api_client)
    id = 'id_example' # str | 

    try:
        # Get a Manga reading status
        api_response = api_instance.get_manga_id_status(id)
        print("The response of MangaApi->get_manga_id_status:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MangaApi->get_manga_id_status: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**GetMangaIdStatus200Response**](GetMangaIdStatus200Response.md)

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
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_manga_random**
> MangaResponse get_manga_random(includes=includes, content_rating=content_rating, included_tags=included_tags, included_tags_mode=included_tags_mode, excluded_tags=excluded_tags, excluded_tags_mode=excluded_tags_mode)

Get a random Manga

### Example


```python
import mangadex_openapi
from mangadex_openapi.models.manga_response import MangaResponse
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
    api_instance = mangadex_openapi.MangaApi(api_client)
    includes = ['includes_example'] # List[str] |  (optional)
    content_rating = ["safe","suggestive","erotica"] # List[str] |  (optional) (default to ["safe","suggestive","erotica"])
    included_tags = ['included_tags_example'] # List[str] |  (optional)
    included_tags_mode = 'AND' # str |  (optional) (default to 'AND')
    excluded_tags = ['excluded_tags_example'] # List[str] |  (optional)
    excluded_tags_mode = 'OR' # str |  (optional) (default to 'OR')

    try:
        # Get a random Manga
        api_response = api_instance.get_manga_random(includes=includes, content_rating=content_rating, included_tags=included_tags, included_tags_mode=included_tags_mode, excluded_tags=excluded_tags, excluded_tags_mode=excluded_tags_mode)
        print("The response of MangaApi->get_manga_random:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MangaApi->get_manga_random: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **includes** | [**List[str]**](str.md)|  | [optional] 
 **content_rating** | [**List[str]**](str.md)|  | [optional] [default to [&quot;safe&quot;,&quot;suggestive&quot;,&quot;erotica&quot;]]
 **included_tags** | [**List[str]**](str.md)|  | [optional] 
 **included_tags_mode** | **str**|  | [optional] [default to &#39;AND&#39;]
 **excluded_tags** | [**List[str]**](str.md)|  | [optional] 
 **excluded_tags_mode** | **str**|  | [optional] [default to &#39;OR&#39;]

### Return type

[**MangaResponse**](MangaResponse.md)

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

# **get_manga_relation**
> MangaRelationList get_manga_relation(manga_id, includes=includes)

Manga relation list

### Example


```python
import mangadex_openapi
from mangadex_openapi.models.manga_relation_list import MangaRelationList
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
    api_instance = mangadex_openapi.MangaApi(api_client)
    manga_id = 'manga_id_example' # str | 
    includes = ['includes_example'] # List[str] |  (optional)

    try:
        # Manga relation list
        api_response = api_instance.get_manga_relation(manga_id, includes=includes)
        print("The response of MangaApi->get_manga_relation:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MangaApi->get_manga_relation: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **manga_id** | **str**|  | 
 **includes** | [**List[str]**](str.md)|  | [optional] 

### Return type

[**MangaRelationList**](MangaRelationList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Manga relation list |  -  |
**400** | Bad Request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_manga_status**
> GetMangaStatus200Response get_manga_status(status=status)

Get all Manga reading status for logged User

### Example

* Bearer Authentication (Bearer):

```python
import mangadex_openapi
from mangadex_openapi.models.get_manga_status200_response import GetMangaStatus200Response
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
    api_instance = mangadex_openapi.MangaApi(api_client)
    status = 'status_example' # str | Used to filter the list by given status (optional)

    try:
        # Get all Manga reading status for logged User
        api_response = api_instance.get_manga_status(status=status)
        print("The response of MangaApi->get_manga_status:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MangaApi->get_manga_status: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **status** | **str**| Used to filter the list by given status | [optional] 

### Return type

[**GetMangaStatus200Response**](GetMangaStatus200Response.md)

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

# **get_manga_tag**
> TagResponse get_manga_tag()

Tag list

### Example


```python
import mangadex_openapi
from mangadex_openapi.models.tag_response import TagResponse
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
    api_instance = mangadex_openapi.MangaApi(api_client)

    try:
        # Tag list
        api_response = api_instance.get_manga_tag()
        print("The response of MangaApi->get_manga_tag:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MangaApi->get_manga_tag: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**TagResponse**](TagResponse.md)

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

# **get_search_manga**
> MangaList get_search_manga(limit=limit, offset=offset, title=title, author_or_artist=author_or_artist, authors=authors, artists=artists, year=year, included_tags=included_tags, included_tags_mode=included_tags_mode, excluded_tags=excluded_tags, excluded_tags_mode=excluded_tags_mode, status=status, original_language=original_language, excluded_original_language=excluded_original_language, available_translated_language=available_translated_language, publication_demographic=publication_demographic, ids=ids, content_rating=content_rating, created_at_since=created_at_since, updated_at_since=updated_at_since, order=order, includes=includes, has_available_chapters=has_available_chapters, group=group)

Manga list

Search a list of Manga.

### Example


```python
import mangadex_openapi
from mangadex_openapi.models.get_search_manga_order_parameter import GetSearchMangaOrderParameter
from mangadex_openapi.models.manga_list import MangaList
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
    api_instance = mangadex_openapi.MangaApi(api_client)
    limit = 10 # int |  (optional) (default to 10)
    offset = 56 # int |  (optional)
    title = 'title_example' # str |  (optional)
    author_or_artist = 'author_or_artist_example' # str |  (optional)
    authors = ['authors_example'] # List[str] |  (optional)
    artists = ['artists_example'] # List[str] |  (optional)
    year = mangadex_openapi.GetSearchMangaYearParameter() # GetSearchMangaYearParameter | Year of release or none (optional)
    included_tags = ['included_tags_example'] # List[str] |  (optional)
    included_tags_mode = 'AND' # str |  (optional) (default to 'AND')
    excluded_tags = ['excluded_tags_example'] # List[str] |  (optional)
    excluded_tags_mode = 'OR' # str |  (optional) (default to 'OR')
    status = ['status_example'] # List[str] |  (optional)
    original_language = ['original_language_example'] # List[str] |  (optional)
    excluded_original_language = ['excluded_original_language_example'] # List[str] |  (optional)
    available_translated_language = ['available_translated_language_example'] # List[str] |  (optional)
    publication_demographic = ['publication_demographic_example'] # List[str] |  (optional)
    ids = ['ids_example'] # List[str] | Manga ids (limited to 100 per request) (optional)
    content_rating = ["safe","suggestive","erotica"] # List[str] |  (optional) (default to ["safe","suggestive","erotica"])
    created_at_since = 'created_at_since_example' # str |  (optional)
    updated_at_since = 'updated_at_since_example' # str |  (optional)
    order = mangadex_openapi.GetSearchMangaOrderParameter() # GetSearchMangaOrderParameter |  (optional)
    includes = ['includes_example'] # List[str] |  (optional)
    has_available_chapters = 'has_available_chapters_example' # str |  (optional)
    group = 'group_example' # str |  (optional)

    try:
        # Manga list
        api_response = api_instance.get_search_manga(limit=limit, offset=offset, title=title, author_or_artist=author_or_artist, authors=authors, artists=artists, year=year, included_tags=included_tags, included_tags_mode=included_tags_mode, excluded_tags=excluded_tags, excluded_tags_mode=excluded_tags_mode, status=status, original_language=original_language, excluded_original_language=excluded_original_language, available_translated_language=available_translated_language, publication_demographic=publication_demographic, ids=ids, content_rating=content_rating, created_at_since=created_at_since, updated_at_since=updated_at_since, order=order, includes=includes, has_available_chapters=has_available_chapters, group=group)
        print("The response of MangaApi->get_search_manga:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MangaApi->get_search_manga: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**|  | [optional] [default to 10]
 **offset** | **int**|  | [optional] 
 **title** | **str**|  | [optional] 
 **author_or_artist** | **str**|  | [optional] 
 **authors** | [**List[str]**](str.md)|  | [optional] 
 **artists** | [**List[str]**](str.md)|  | [optional] 
 **year** | [**GetSearchMangaYearParameter**](.md)| Year of release or none | [optional] 
 **included_tags** | [**List[str]**](str.md)|  | [optional] 
 **included_tags_mode** | **str**|  | [optional] [default to &#39;AND&#39;]
 **excluded_tags** | [**List[str]**](str.md)|  | [optional] 
 **excluded_tags_mode** | **str**|  | [optional] [default to &#39;OR&#39;]
 **status** | [**List[str]**](str.md)|  | [optional] 
 **original_language** | [**List[str]**](str.md)|  | [optional] 
 **excluded_original_language** | [**List[str]**](str.md)|  | [optional] 
 **available_translated_language** | [**List[str]**](str.md)|  | [optional] 
 **publication_demographic** | [**List[str]**](str.md)|  | [optional] 
 **ids** | [**List[str]**](str.md)| Manga ids (limited to 100 per request) | [optional] 
 **content_rating** | [**List[str]**](str.md)|  | [optional] [default to [&quot;safe&quot;,&quot;suggestive&quot;,&quot;erotica&quot;]]
 **created_at_since** | **str**|  | [optional] 
 **updated_at_since** | **str**|  | [optional] 
 **order** | [**GetSearchMangaOrderParameter**](.md)|  | [optional] 
 **includes** | [**List[str]**](str.md)|  | [optional] 
 **has_available_chapters** | **str**|  | [optional] 
 **group** | **str**|  | [optional] 

### Return type

[**MangaList**](MangaList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Manga list |  -  |
**400** | Bad Request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_manga**
> MangaResponse post_manga(content_type, manga_create=manga_create)

Create Manga

Create a new Manga.

### Example

* Bearer Authentication (Bearer):

```python
import mangadex_openapi
from mangadex_openapi.models.manga_create import MangaCreate
from mangadex_openapi.models.manga_response import MangaResponse
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
    api_instance = mangadex_openapi.MangaApi(api_client)
    content_type = 'application/json' # str |  (default to 'application/json')
    manga_create = mangadex_openapi.MangaCreate() # MangaCreate | The size of the body is limited to 64KB. (optional)

    try:
        # Create Manga
        api_response = api_instance.post_manga(content_type, manga_create=manga_create)
        print("The response of MangaApi->post_manga:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MangaApi->post_manga: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **content_type** | **str**|  | [default to &#39;application/json&#39;]
 **manga_create** | [**MangaCreate**](MangaCreate.md)| The size of the body is limited to 64KB. | [optional] 

### Return type

[**MangaResponse**](MangaResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Manga Created |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_manga_id_follow**
> Response post_manga_id_follow(id)

Follow Manga

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
    api_instance = mangadex_openapi.MangaApi(api_client)
    id = 'id_example' # str | 

    try:
        # Follow Manga
        api_response = api_instance.post_manga_id_follow(id)
        print("The response of MangaApi->post_manga_id_follow:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MangaApi->post_manga_id_follow: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

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
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_manga_id_status**
> Response post_manga_id_status(id, content_type, update_manga_status=update_manga_status)

Update Manga reading status

### Example

* Bearer Authentication (Bearer):

```python
import mangadex_openapi
from mangadex_openapi.models.response import Response
from mangadex_openapi.models.update_manga_status import UpdateMangaStatus
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
    api_instance = mangadex_openapi.MangaApi(api_client)
    id = 'id_example' # str | 
    content_type = 'application/json' # str |  (default to 'application/json')
    update_manga_status = mangadex_openapi.UpdateMangaStatus() # UpdateMangaStatus | Using a `null` value in `status` field will remove the Manga reading status. The size of the body is limited to 2KB. (optional)

    try:
        # Update Manga reading status
        api_response = api_instance.post_manga_id_status(id, content_type, update_manga_status=update_manga_status)
        print("The response of MangaApi->post_manga_id_status:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MangaApi->post_manga_id_status: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **content_type** | **str**|  | [default to &#39;application/json&#39;]
 **update_manga_status** | [**UpdateMangaStatus**](UpdateMangaStatus.md)| Using a &#x60;null&#x60; value in &#x60;status&#x60; field will remove the Manga reading status. The size of the body is limited to 2KB. | [optional] 

### Return type

[**Response**](Response.md)

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
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_manga_relation**
> MangaRelationResponse post_manga_relation(manga_id, content_type, manga_relation_create=manga_relation_create)

Create Manga relation

Create a new Manga relation.

### Example

* Bearer Authentication (Bearer):

```python
import mangadex_openapi
from mangadex_openapi.models.manga_relation_create import MangaRelationCreate
from mangadex_openapi.models.manga_relation_response import MangaRelationResponse
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
    api_instance = mangadex_openapi.MangaApi(api_client)
    manga_id = 'manga_id_example' # str | 
    content_type = 'application/json' # str |  (default to 'application/json')
    manga_relation_create = mangadex_openapi.MangaRelationCreate() # MangaRelationCreate | The size of the body is limited to 8KB. (optional)

    try:
        # Create Manga relation
        api_response = api_instance.post_manga_relation(manga_id, content_type, manga_relation_create=manga_relation_create)
        print("The response of MangaApi->post_manga_relation:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MangaApi->post_manga_relation: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **manga_id** | **str**|  | 
 **content_type** | **str**|  | [default to &#39;application/json&#39;]
 **manga_relation_create** | [**MangaRelationCreate**](MangaRelationCreate.md)| The size of the body is limited to 8KB. | [optional] 

### Return type

[**MangaRelationResponse**](MangaRelationResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Manga relation created |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_manga_id**
> MangaResponse put_manga_id(id, content_type, put_manga_id_request=put_manga_id_request)

Update Manga

### Example

* Bearer Authentication (Bearer):

```python
import mangadex_openapi
from mangadex_openapi.models.manga_response import MangaResponse
from mangadex_openapi.models.put_manga_id_request import PutMangaIdRequest
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
    api_instance = mangadex_openapi.MangaApi(api_client)
    id = 'id_example' # str | Manga ID
    content_type = 'application/json' # str |  (default to 'application/json')
    put_manga_id_request = mangadex_openapi.PutMangaIdRequest() # PutMangaIdRequest | The size of the body is limited to 64KB. (optional)

    try:
        # Update Manga
        api_response = api_instance.put_manga_id(id, content_type, put_manga_id_request=put_manga_id_request)
        print("The response of MangaApi->put_manga_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MangaApi->put_manga_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Manga ID | 
 **content_type** | **str**|  | [default to &#39;application/json&#39;]
 **put_manga_id_request** | [**PutMangaIdRequest**](PutMangaIdRequest.md)| The size of the body is limited to 64KB. | [optional] 

### Return type

[**MangaResponse**](MangaResponse.md)

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

