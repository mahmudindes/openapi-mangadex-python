# mangadex_openapi.LegacyApi

All URIs are relative to *https://api.mangadex.org*

Method | HTTP request | Description
------------- | ------------- | -------------
[**post_legacy_mapping**](LegacyApi.md#post_legacy_mapping) | **POST** /legacy/mapping | Legacy ID mapping


# **post_legacy_mapping**
> MappingIdResponse post_legacy_mapping(content_type, mapping_id_body=mapping_id_body)

Legacy ID mapping

### Example


```python
import mangadex_openapi
from mangadex_openapi.models.mapping_id_body import MappingIdBody
from mangadex_openapi.models.mapping_id_response import MappingIdResponse
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
    api_instance = mangadex_openapi.LegacyApi(api_client)
    content_type = 'application/json' # str |  (default to 'application/json')
    mapping_id_body = mangadex_openapi.MappingIdBody() # MappingIdBody | The size of the body is limited to 10KB. (optional)

    try:
        # Legacy ID mapping
        api_response = api_instance.post_legacy_mapping(content_type, mapping_id_body=mapping_id_body)
        print("The response of LegacyApi->post_legacy_mapping:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LegacyApi->post_legacy_mapping: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **content_type** | **str**|  | [default to &#39;application/json&#39;]
 **mapping_id_body** | [**MappingIdBody**](MappingIdBody.md)| The size of the body is limited to 10KB. | [optional] 

### Return type

[**MappingIdResponse**](MappingIdResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | This response will give you an array of mappings of resource identifiers ; the &#x60;data.attributes.newId&#x60; field corresponds to the new UUID. |  -  |
**400** | Bad Request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

