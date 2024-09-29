# ForumsThreadResponseDataAttributes


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**replies_count** | **int** | The number of replies so far in the forums thread returned | [optional] 

## Example

```python
from mangadex_openapi.models.forums_thread_response_data_attributes import ForumsThreadResponseDataAttributes

# TODO update the JSON string below
json = "{}"
# create an instance of ForumsThreadResponseDataAttributes from a JSON string
forums_thread_response_data_attributes_instance = ForumsThreadResponseDataAttributes.from_json(json)
# print the JSON string representation of the object
print(ForumsThreadResponseDataAttributes.to_json())

# convert the object into a dict
forums_thread_response_data_attributes_dict = forums_thread_response_data_attributes_instance.to_dict()
# create an instance of ForumsThreadResponseDataAttributes from a dict
forums_thread_response_data_attributes_form_dict = forums_thread_response_data_attributes.from_dict(forums_thread_response_data_attributes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


