# mangadex_openapi.CaptchaApi

All URIs are relative to *https://api.mangadex.org*

Method | HTTP request | Description
------------- | ------------- | -------------
[**post_captcha_solve**](CaptchaApi.md#post_captcha_solve) | **POST** /captcha/solve | Solve Captcha


# **post_captcha_solve**
> PostCaptchaSolve200Response post_captcha_solve(content_type, post_captcha_solve_request=post_captcha_solve_request)

Solve Captcha

Captchas can be solved explicitly through this endpoint, another way is to add a `X-Captcha-Result` header to any request. The same logic will verify the captcha and is probably more convenient because it takes one less request.  Authentication is optional. Captchas are tracked for both the client ip and for the user id, if you are logged in you want to send your session token but that is not required.

### Example

* Bearer Authentication (Bearer):

```python
import mangadex_openapi
from mangadex_openapi.models.post_captcha_solve200_response import PostCaptchaSolve200Response
from mangadex_openapi.models.post_captcha_solve_request import PostCaptchaSolveRequest
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
    api_instance = mangadex_openapi.CaptchaApi(api_client)
    content_type = 'application/json' # str |  (default to 'application/json')
    post_captcha_solve_request = {"captchaChallenge":"string"} # PostCaptchaSolveRequest |  (optional)

    try:
        # Solve Captcha
        api_response = api_instance.post_captcha_solve(content_type, post_captcha_solve_request=post_captcha_solve_request)
        print("The response of CaptchaApi->post_captcha_solve:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CaptchaApi->post_captcha_solve: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **content_type** | **str**|  | [default to &#39;application/json&#39;]
 **post_captcha_solve_request** | [**PostCaptchaSolveRequest**](PostCaptchaSolveRequest.md)|  | [optional] 

### Return type

[**PostCaptchaSolve200Response**](PostCaptchaSolve200Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK: Captcha has been solved |  -  |
**400** | Bad Request: Captcha challenge result was wrong, the Captcha Verification service was down or other, refer to the error message and the errorCode inside the error context |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

