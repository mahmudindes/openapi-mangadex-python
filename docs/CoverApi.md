# mangadex_openapi.CoverApi

All URIs are relative to *https://api.mangadex.org*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_cover**](CoverApi.md#delete_cover) | **DELETE** /cover/{mangaOrCoverId} | Delete Cover
[**edit_cover**](CoverApi.md#edit_cover) | **PUT** /cover/{mangaOrCoverId} | Edit Cover
[**get_cover**](CoverApi.md#get_cover) | **GET** /cover | CoverArt list
[**get_cover_id**](CoverApi.md#get_cover_id) | **GET** /cover/{mangaOrCoverId} | Get Cover
[**upload_cover**](CoverApi.md#upload_cover) | **POST** /cover/{mangaOrCoverId} | Upload Cover


# **delete_cover**
> Response delete_cover(manga_or_cover_id)

Delete Cover

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
    api_instance = mangadex_openapi.CoverApi(api_client)
    manga_or_cover_id = 'manga_or_cover_id_example' # str | Is Manga UUID on POST

    try:
        # Delete Cover
        api_response = api_instance.delete_cover(manga_or_cover_id)
        print("The response of CoverApi->delete_cover:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoverApi->delete_cover: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **manga_or_cover_id** | **str**| Is Manga UUID on POST | 

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
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **edit_cover**
> CoverResponse edit_cover(manga_or_cover_id, content_type, cover_edit=cover_edit)

Edit Cover

### Example

* Bearer Authentication (Bearer):

```python
import mangadex_openapi
from mangadex_openapi.models.cover_edit import CoverEdit
from mangadex_openapi.models.cover_response import CoverResponse
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
    api_instance = mangadex_openapi.CoverApi(api_client)
    manga_or_cover_id = 'manga_or_cover_id_example' # str | Is Manga UUID on POST
    content_type = 'application/json' # str |  (default to 'application/json')
    cover_edit = mangadex_openapi.CoverEdit() # CoverEdit | The size of the body is limited to 2KB. (optional)

    try:
        # Edit Cover
        api_response = api_instance.edit_cover(manga_or_cover_id, content_type, cover_edit=cover_edit)
        print("The response of CoverApi->edit_cover:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoverApi->edit_cover: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **manga_or_cover_id** | **str**| Is Manga UUID on POST | 
 **content_type** | **str**|  | [default to &#39;application/json&#39;]
 **cover_edit** | [**CoverEdit**](CoverEdit.md)| The size of the body is limited to 2KB. | [optional] 

### Return type

[**CoverResponse**](CoverResponse.md)

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_cover**
> CoverList get_cover(limit=limit, offset=offset, manga=manga, ids=ids, uploaders=uploaders, locales=locales, order=order, includes=includes)

CoverArt list

### Example


```python
import mangadex_openapi
from mangadex_openapi.models.cover_list import CoverList
from mangadex_openapi.models.get_cover_order_parameter import GetCoverOrderParameter
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
    api_instance = mangadex_openapi.CoverApi(api_client)
    limit = 10 # int |  (optional) (default to 10)
    offset = 56 # int |  (optional)
    manga = ['manga_example'] # List[str] | Manga ids (limited to 100 per request) (optional)
    ids = ['ids_example'] # List[str] | Covers ids (limited to 100 per request) (optional)
    uploaders = ['uploaders_example'] # List[str] | User ids (limited to 100 per request) (optional)
    locales = ['locales_example'] # List[str] | Locales of cover art (limited to 100 per request) (optional)
    order = mangadex_openapi.GetCoverOrderParameter() # GetCoverOrderParameter |  (optional)
    includes = ['includes_example'] # List[str] |  (optional)

    try:
        # CoverArt list
        api_response = api_instance.get_cover(limit=limit, offset=offset, manga=manga, ids=ids, uploaders=uploaders, locales=locales, order=order, includes=includes)
        print("The response of CoverApi->get_cover:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoverApi->get_cover: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**|  | [optional] [default to 10]
 **offset** | **int**|  | [optional] 
 **manga** | [**List[str]**](str.md)| Manga ids (limited to 100 per request) | [optional] 
 **ids** | [**List[str]**](str.md)| Covers ids (limited to 100 per request) | [optional] 
 **uploaders** | [**List[str]**](str.md)| User ids (limited to 100 per request) | [optional] 
 **locales** | [**List[str]**](str.md)| Locales of cover art (limited to 100 per request) | [optional] 
 **order** | [**GetCoverOrderParameter**](.md)|  | [optional] 
 **includes** | [**List[str]**](str.md)|  | [optional] 

### Return type

[**CoverList**](CoverList.md)

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
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_cover_id**
> CoverResponse get_cover_id(manga_or_cover_id, includes=includes)

Get Cover

### Example


```python
import mangadex_openapi
from mangadex_openapi.models.cover_response import CoverResponse
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
    api_instance = mangadex_openapi.CoverApi(api_client)
    manga_or_cover_id = 'manga_or_cover_id_example' # str | Is Manga UUID on POST
    includes = ['includes_example'] # List[str] |  (optional)

    try:
        # Get Cover
        api_response = api_instance.get_cover_id(manga_or_cover_id, includes=includes)
        print("The response of CoverApi->get_cover_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoverApi->get_cover_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **manga_or_cover_id** | **str**| Is Manga UUID on POST | 
 **includes** | [**List[str]**](str.md)|  | [optional] 

### Return type

[**CoverResponse**](CoverResponse.md)

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
**403** | Forbidden |  -  |
**404** | CoverArt not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upload_cover**
> CoverResponse upload_cover(manga_or_cover_id, content_type, file=file, volume=volume, description=description, locale=locale)

Upload Cover

### Example

* Bearer Authentication (Bearer):

```python
import mangadex_openapi
from mangadex_openapi.models.cover_response import CoverResponse
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
    api_instance = mangadex_openapi.CoverApi(api_client)
    manga_or_cover_id = 'manga_or_cover_id_example' # str | Is Manga UUID on POST
    content_type = 'multipart/form-data' # str |  (default to 'multipart/form-data')
    file = None # bytearray |  (optional)
    volume = 'volume_example' # str |  (optional)
    description = 'description_example' # str |  (optional)
    locale = 'locale_example' # str |  (optional)

    try:
        # Upload Cover
        api_response = api_instance.upload_cover(manga_or_cover_id, content_type, file=file, volume=volume, description=description, locale=locale)
        print("The response of CoverApi->upload_cover:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CoverApi->upload_cover: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **manga_or_cover_id** | **str**| Is Manga UUID on POST | 
 **content_type** | **str**|  | [default to &#39;multipart/form-data&#39;]
 **file** | **bytearray**|  | [optional] 
 **volume** | **str**|  | [optional] 
 **description** | **str**|  | [optional] 
 **locale** | **str**|  | [optional] 

### Return type

[**CoverResponse**](CoverResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

