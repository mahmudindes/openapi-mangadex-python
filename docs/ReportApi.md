# mangadex_openapi.ReportApi

All URIs are relative to *https://api.mangadex.org*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_report_reasons_by_category**](ReportApi.md#get_report_reasons_by_category) | **GET** /report/reasons/{category} | Get a list of report reasons
[**get_reports**](ReportApi.md#get_reports) | **GET** /report | Get a list of reports by the user
[**post_report**](ReportApi.md#post_report) | **POST** /report | Create a new Report


# **get_report_reasons_by_category**
> GetReportReasonsByCategory200Response get_report_reasons_by_category(category)

Get a list of report reasons

### Example

* Bearer Authentication (Bearer):

```python
import mangadex_openapi
from mangadex_openapi.models.get_report_reasons_by_category200_response import GetReportReasonsByCategory200Response
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
    api_instance = mangadex_openapi.ReportApi(api_client)
    category = 'category_example' # str | 

    try:
        # Get a list of report reasons
        api_response = api_instance.get_report_reasons_by_category(category)
        print("The response of ReportApi->get_report_reasons_by_category:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReportApi->get_report_reasons_by_category: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **category** | **str**|  | 

### Return type

[**GetReportReasonsByCategory200Response**](GetReportReasonsByCategory200Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad request |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_reports**
> ReportListResponse get_reports(limit=limit, offset=offset, category=category, reason_id=reason_id, object_id=object_id, status=status, order=order, includes=includes)

Get a list of reports by the user

### Example

* Bearer Authentication (Bearer):

```python
import mangadex_openapi
from mangadex_openapi.models.get_reports_order_parameter import GetReportsOrderParameter
from mangadex_openapi.models.report_list_response import ReportListResponse
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
    api_instance = mangadex_openapi.ReportApi(api_client)
    limit = 10 # int |  (optional) (default to 10)
    offset = 56 # int |  (optional)
    category = 'category_example' # str |  (optional)
    reason_id = 'reason_id_example' # str |  (optional)
    object_id = 'object_id_example' # str |  (optional)
    status = 'status_example' # str |  (optional)
    order = mangadex_openapi.GetReportsOrderParameter() # GetReportsOrderParameter |  (optional)
    includes = ['includes_example'] # List[str] |  (optional)

    try:
        # Get a list of reports by the user
        api_response = api_instance.get_reports(limit=limit, offset=offset, category=category, reason_id=reason_id, object_id=object_id, status=status, order=order, includes=includes)
        print("The response of ReportApi->get_reports:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReportApi->get_reports: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**|  | [optional] [default to 10]
 **offset** | **int**|  | [optional] 
 **category** | **str**|  | [optional] 
 **reason_id** | **str**|  | [optional] 
 **object_id** | **str**|  | [optional] 
 **status** | **str**|  | [optional] 
 **order** | [**GetReportsOrderParameter**](.md)|  | [optional] 
 **includes** | [**List[str]**](str.md)|  | [optional] 

### Return type

[**ReportListResponse**](ReportListResponse.md)

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

# **post_report**
> Response post_report(content_type, post_report_request=post_report_request)

Create a new Report

### Example

* Bearer Authentication (Bearer):

```python
import mangadex_openapi
from mangadex_openapi.models.post_report_request import PostReportRequest
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
    api_instance = mangadex_openapi.ReportApi(api_client)
    content_type = 'application/json' # str |  (default to 'application/json')
    post_report_request = mangadex_openapi.PostReportRequest() # PostReportRequest | The size of the body is limited to 8KB. (optional)

    try:
        # Create a new Report
        api_response = api_instance.post_report(content_type, post_report_request=post_report_request)
        print("The response of ReportApi->post_report:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReportApi->post_report: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **content_type** | **str**|  | [default to &#39;application/json&#39;]
 **post_report_request** | [**PostReportRequest**](PostReportRequest.md)| The size of the body is limited to 8KB. | [optional] 

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
**201** | Created |  -  |
**400** | Bad request |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

