# ForumsThreadResponseData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] [default to 'thread']
**id** | **int** | The id for the thread on the forums, accessible at &#x60;https://forums.mangadex.org/threads/:id&#x60; | [optional] 
**attributes** | [**ForumsThreadResponseDataAttributes**](ForumsThreadResponseDataAttributes.md) |  | [optional] 

## Example

```python
from mangadex_openapi.models.forums_thread_response_data import ForumsThreadResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of ForumsThreadResponseData from a JSON string
forums_thread_response_data_instance = ForumsThreadResponseData.from_json(json)
# print the JSON string representation of the object
print(ForumsThreadResponseData.to_json())

# convert the object into a dict
forums_thread_response_data_dict = forums_thread_response_data_instance.to_dict()
# create an instance of ForumsThreadResponseData from a dict
forums_thread_response_data_form_dict = forums_thread_response_data.from_dict(forums_thread_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


