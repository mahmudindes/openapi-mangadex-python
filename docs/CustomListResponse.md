# CustomListResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**result** | **str** |  | [optional] 
**response** | **str** |  | [optional] [default to 'entity']
**data** | [**CustomList**](CustomList.md) |  | [optional] 

## Example

```python
from mangadex_openapi.models.custom_list_response import CustomListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CustomListResponse from a JSON string
custom_list_response_instance = CustomListResponse.from_json(json)
# print the JSON string representation of the object
print(CustomListResponse.to_json())

# convert the object into a dict
custom_list_response_dict = custom_list_response_instance.to_dict()
# create an instance of CustomListResponse from a dict
custom_list_response_form_dict = custom_list_response.from_dict(custom_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


