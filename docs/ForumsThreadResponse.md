# ForumsThreadResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**result** | **str** |  | [optional] [default to 'ok']
**response** | **str** |  | [optional] [default to 'entity']
**data** | [**ForumsThreadResponseData**](ForumsThreadResponseData.md) |  | [optional] 

## Example

```python
from mangadex_openapi.models.forums_thread_response import ForumsThreadResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ForumsThreadResponse from a JSON string
forums_thread_response_instance = ForumsThreadResponse.from_json(json)
# print the JSON string representation of the object
print(ForumsThreadResponse.to_json())

# convert the object into a dict
forums_thread_response_dict = forums_thread_response_instance.to_dict()
# create an instance of ForumsThreadResponse from a dict
forums_thread_response_form_dict = forums_thread_response.from_dict(forums_thread_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


