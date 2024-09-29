# mangadex_openapi.UploadApi

All URIs are relative to *https://api.mangadex.org*

Method | HTTP request | Description
------------- | ------------- | -------------
[**abandon_upload_session**](UploadApi.md#abandon_upload_session) | **DELETE** /upload/{uploadSessionId} | Abandon upload session
[**begin_edit_session**](UploadApi.md#begin_edit_session) | **POST** /upload/begin/{chapterId} | Start an edit chapter session
[**begin_upload_session**](UploadApi.md#begin_upload_session) | **POST** /upload/begin | Start an upload session
[**commit_upload_session**](UploadApi.md#commit_upload_session) | **POST** /upload/{uploadSessionId}/commit | Commit the upload session and specify chapter data
[**delete_uploaded_session_file**](UploadApi.md#delete_uploaded_session_file) | **DELETE** /upload/{uploadSessionId}/{uploadSessionFileId} | Delete an uploaded image from the Upload Session
[**delete_uploaded_session_files**](UploadApi.md#delete_uploaded_session_files) | **DELETE** /upload/{uploadSessionId}/batch | Delete a set of uploaded images from the Upload Session
[**get_upload_session**](UploadApi.md#get_upload_session) | **GET** /upload | Get the current User upload session
[**put_upload_session_file**](UploadApi.md#put_upload_session_file) | **POST** /upload/{uploadSessionId} | Upload images to the upload session
[**upload_check_approval_required**](UploadApi.md#upload_check_approval_required) | **POST** /upload/check-approval-required | Check if a given manga / locale for a User needs moderation approval


# **abandon_upload_session**
> Response abandon_upload_session(upload_session_id)

Abandon upload session

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
    api_instance = mangadex_openapi.UploadApi(api_client)
    upload_session_id = 'upload_session_id_example' # str | 

    try:
        # Abandon upload session
        api_response = api_instance.abandon_upload_session(upload_session_id)
        print("The response of UploadApi->abandon_upload_session:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UploadApi->abandon_upload_session: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **upload_session_id** | **str**|  | 

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **begin_edit_session**
> UploadSession begin_edit_session(chapter_id, content_type, begin_edit_session=begin_edit_session)

Start an edit chapter session

### Example

* Bearer Authentication (Bearer):

```python
import mangadex_openapi
from mangadex_openapi.models.begin_edit_session import BeginEditSession
from mangadex_openapi.models.upload_session import UploadSession
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
    api_instance = mangadex_openapi.UploadApi(api_client)
    chapter_id = 'chapter_id_example' # str | 
    content_type = 'application/json' # str |  (default to 'application/json')
    begin_edit_session = mangadex_openapi.BeginEditSession() # BeginEditSession | The size of the body is limited to 1KB. (optional)

    try:
        # Start an edit chapter session
        api_response = api_instance.begin_edit_session(chapter_id, content_type, begin_edit_session=begin_edit_session)
        print("The response of UploadApi->begin_edit_session:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UploadApi->begin_edit_session: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **chapter_id** | **str**|  | 
 **content_type** | **str**|  | [default to &#39;application/json&#39;]
 **begin_edit_session** | [**BeginEditSession**](BeginEditSession.md)| The size of the body is limited to 1KB. | [optional] 

### Return type

[**UploadSession**](UploadSession.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request if Chapter&#39;s Manga is unpublished |  -  |
**401** | Unauthorized if user does not have upload permissions or has no rights to edit the chapter (needs to be uploader or group member) |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **begin_upload_session**
> UploadSession begin_upload_session(content_type, begin_upload_session=begin_upload_session)

Start an upload session

### Example

* Bearer Authentication (Bearer):

```python
import mangadex_openapi
from mangadex_openapi.models.begin_upload_session import BeginUploadSession
from mangadex_openapi.models.upload_session import UploadSession
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
    api_instance = mangadex_openapi.UploadApi(api_client)
    content_type = 'application/json' # str |  (default to 'application/json')
    begin_upload_session = mangadex_openapi.BeginUploadSession() # BeginUploadSession | The size of the body is limited to 4KB. (optional)

    try:
        # Start an upload session
        api_response = api_instance.begin_upload_session(content_type, begin_upload_session=begin_upload_session)
        print("The response of UploadApi->begin_upload_session:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UploadApi->begin_upload_session: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **content_type** | **str**|  | [default to &#39;application/json&#39;]
 **begin_upload_session** | [**BeginUploadSession**](BeginUploadSession.md)| The size of the body is limited to 4KB. | [optional] 

### Return type

[**UploadSession**](UploadSession.md)

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

# **commit_upload_session**
> Chapter commit_upload_session(upload_session_id, content_type, commit_upload_session=commit_upload_session)

Commit the upload session and specify chapter data

### Example

* Bearer Authentication (Bearer):

```python
import mangadex_openapi
from mangadex_openapi.models.chapter import Chapter
from mangadex_openapi.models.commit_upload_session import CommitUploadSession
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
    api_instance = mangadex_openapi.UploadApi(api_client)
    upload_session_id = 'upload_session_id_example' # str | 
    content_type = 'application/json' # str |  (default to 'application/json')
    commit_upload_session = mangadex_openapi.CommitUploadSession() # CommitUploadSession | The size of the body is limited to 4KB. (optional)

    try:
        # Commit the upload session and specify chapter data
        api_response = api_instance.commit_upload_session(upload_session_id, content_type, commit_upload_session=commit_upload_session)
        print("The response of UploadApi->commit_upload_session:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UploadApi->commit_upload_session: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **upload_session_id** | **str**|  | 
 **content_type** | **str**|  | [default to &#39;application/json&#39;]
 **commit_upload_session** | [**CommitUploadSession**](CommitUploadSession.md)| The size of the body is limited to 4KB. | [optional] 

### Return type

[**Chapter**](Chapter.md)

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

# **delete_uploaded_session_file**
> Response delete_uploaded_session_file(upload_session_id, upload_session_file_id)

Delete an uploaded image from the Upload Session

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
    api_instance = mangadex_openapi.UploadApi(api_client)
    upload_session_id = 'upload_session_id_example' # str | 
    upload_session_file_id = 'upload_session_file_id_example' # str | 

    try:
        # Delete an uploaded image from the Upload Session
        api_response = api_instance.delete_uploaded_session_file(upload_session_id, upload_session_file_id)
        print("The response of UploadApi->delete_uploaded_session_file:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UploadApi->delete_uploaded_session_file: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **upload_session_id** | **str**|  | 
 **upload_session_file_id** | **str**|  | 

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_uploaded_session_files**
> Response delete_uploaded_session_files(upload_session_id, content_type, request_body=request_body)

Delete a set of uploaded images from the Upload Session

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
    api_instance = mangadex_openapi.UploadApi(api_client)
    upload_session_id = 'upload_session_id_example' # str | 
    content_type = 'application/json' # str |  (default to 'application/json')
    request_body = ['request_body_example'] # List[str] | The size of the body is limited to 20KB. (optional)

    try:
        # Delete a set of uploaded images from the Upload Session
        api_response = api_instance.delete_uploaded_session_files(upload_session_id, content_type, request_body=request_body)
        print("The response of UploadApi->delete_uploaded_session_files:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UploadApi->delete_uploaded_session_files: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **upload_session_id** | **str**|  | 
 **content_type** | **str**|  | [default to &#39;application/json&#39;]
 **request_body** | [**List[str]**](str.md)| The size of the body is limited to 20KB. | [optional] 

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_upload_session**
> UploadSession get_upload_session()

Get the current User upload session

### Example

* Bearer Authentication (Bearer):

```python
import mangadex_openapi
from mangadex_openapi.models.upload_session import UploadSession
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
    api_instance = mangadex_openapi.UploadApi(api_client)

    try:
        # Get the current User upload session
        api_response = api_instance.get_upload_session()
        print("The response of UploadApi->get_upload_session:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UploadApi->get_upload_session: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**UploadSession**](UploadSession.md)

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

# **put_upload_session_file**
> PutUploadSessionFile200Response put_upload_session_file(upload_session_id, content_type, file=file)

Upload images to the upload session

### Example

* Bearer Authentication (Bearer):

```python
import mangadex_openapi
from mangadex_openapi.models.put_upload_session_file200_response import PutUploadSessionFile200Response
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
    api_instance = mangadex_openapi.UploadApi(api_client)
    upload_session_id = 'upload_session_id_example' # str | 
    content_type = 'application/json' # str |  (default to 'application/json')
    file = None # bytearray |  (optional)

    try:
        # Upload images to the upload session
        api_response = api_instance.put_upload_session_file(upload_session_id, content_type, file=file)
        print("The response of UploadApi->put_upload_session_file:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UploadApi->put_upload_session_file: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **upload_session_id** | **str**|  | 
 **content_type** | **str**|  | [default to &#39;application/json&#39;]
 **file** | **bytearray**|  | [optional] 

### Return type

[**PutUploadSessionFile200Response**](PutUploadSessionFile200Response.md)

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upload_check_approval_required**
> UploadCheckApprovalRequired200Response upload_check_approval_required(upload_check_approval_required_request=upload_check_approval_required_request)

Check if a given manga / locale for a User needs moderation approval

### Example

* Bearer Authentication (Bearer):

```python
import mangadex_openapi
from mangadex_openapi.models.upload_check_approval_required200_response import UploadCheckApprovalRequired200Response
from mangadex_openapi.models.upload_check_approval_required_request import UploadCheckApprovalRequiredRequest
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
    api_instance = mangadex_openapi.UploadApi(api_client)
    upload_check_approval_required_request = mangadex_openapi.UploadCheckApprovalRequiredRequest() # UploadCheckApprovalRequiredRequest | The size of the body is limited to 4KB. (optional)

    try:
        # Check if a given manga / locale for a User needs moderation approval
        api_response = api_instance.upload_check_approval_required(upload_check_approval_required_request=upload_check_approval_required_request)
        print("The response of UploadApi->upload_check_approval_required:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UploadApi->upload_check_approval_required: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **upload_check_approval_required_request** | [**UploadCheckApprovalRequiredRequest**](UploadCheckApprovalRequiredRequest.md)| The size of the body is limited to 4KB. | [optional] 

### Return type

[**UploadCheckApprovalRequired200Response**](UploadCheckApprovalRequired200Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**404** | Manga not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

