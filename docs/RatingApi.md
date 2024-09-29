# mangadex_openapi.RatingApi

All URIs are relative to *https://api.mangadex.org*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_rating_manga_id**](RatingApi.md#delete_rating_manga_id) | **DELETE** /rating/{mangaId} | Delete Manga rating
[**get_rating**](RatingApi.md#get_rating) | **GET** /rating | Get your ratings
[**post_rating_manga_id**](RatingApi.md#post_rating_manga_id) | **POST** /rating/{mangaId} | Create or update Manga rating


# **delete_rating_manga_id**
> Response delete_rating_manga_id(manga_id)

Delete Manga rating

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
    api_instance = mangadex_openapi.RatingApi(api_client)
    manga_id = 'manga_id_example' # str | 

    try:
        # Delete Manga rating
        api_response = api_instance.delete_rating_manga_id(manga_id)
        print("The response of RatingApi->delete_rating_manga_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RatingApi->delete_rating_manga_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **manga_id** | **str**|  | 

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
**200** | Manga rating was deleted |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_rating**
> GetRating200Response get_rating(manga)

Get your ratings

### Example

* Bearer Authentication (Bearer):

```python
import mangadex_openapi
from mangadex_openapi.models.get_rating200_response import GetRating200Response
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
    api_instance = mangadex_openapi.RatingApi(api_client)
    manga = ['manga_example'] # List[str] | 

    try:
        # Get your ratings
        api_response = api_instance.get_rating(manga)
        print("The response of RatingApi->get_rating:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RatingApi->get_rating: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **manga** | [**List[str]**](str.md)|  | 

### Return type

[**GetRating200Response**](GetRating200Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Self-rating list |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_rating_manga_id**
> Response post_rating_manga_id(manga_id, post_rating_manga_id_request=post_rating_manga_id_request)

Create or update Manga rating

### Example

* Bearer Authentication (Bearer):

```python
import mangadex_openapi
from mangadex_openapi.models.post_rating_manga_id_request import PostRatingMangaIdRequest
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
    api_instance = mangadex_openapi.RatingApi(api_client)
    manga_id = 'manga_id_example' # str | 
    post_rating_manga_id_request = mangadex_openapi.PostRatingMangaIdRequest() # PostRatingMangaIdRequest |  (optional)

    try:
        # Create or update Manga rating
        api_response = api_instance.post_rating_manga_id(manga_id, post_rating_manga_id_request=post_rating_manga_id_request)
        print("The response of RatingApi->post_rating_manga_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RatingApi->post_rating_manga_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **manga_id** | **str**|  | 
 **post_rating_manga_id_request** | [**PostRatingMangaIdRequest**](PostRatingMangaIdRequest.md)|  | [optional] 

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
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

