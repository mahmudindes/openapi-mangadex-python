# ForumsThreadCreateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The type of the resource | [optional] 
**id** | **str** | The id of the resource | [optional] 

## Example

```python
from mangadex_openapi.models.forums_thread_create_request import ForumsThreadCreateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ForumsThreadCreateRequest from a JSON string
forums_thread_create_request_instance = ForumsThreadCreateRequest.from_json(json)
# print the JSON string representation of the object
print(ForumsThreadCreateRequest.to_json())

# convert the object into a dict
forums_thread_create_request_dict = forums_thread_create_request_instance.to_dict()
# create an instance of ForumsThreadCreateRequest from a dict
forums_thread_create_request_form_dict = forums_thread_create_request.from_dict(forums_thread_create_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


