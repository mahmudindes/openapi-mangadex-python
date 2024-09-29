# PostCaptchaSolveRequest



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**captcha_challenge** | **str** |  | 

## Example

```python
from mangadex_openapi.models.post_captcha_solve_request import PostCaptchaSolveRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PostCaptchaSolveRequest from a JSON string
post_captcha_solve_request_instance = PostCaptchaSolveRequest.from_json(json)
# print the JSON string representation of the object
print(PostCaptchaSolveRequest.to_json())

# convert the object into a dict
post_captcha_solve_request_dict = post_captcha_solve_request_instance.to_dict()
# create an instance of PostCaptchaSolveRequest from a dict
post_captcha_solve_request_form_dict = post_captcha_solve_request.from_dict(post_captcha_solve_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


