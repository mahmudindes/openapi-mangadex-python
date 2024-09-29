# CustomListAttributes


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**visibility** | **str** |  | [optional] 
**version** | **int** |  | [optional] 

## Example

```python
from mangadex_openapi.models.custom_list_attributes import CustomListAttributes

# TODO update the JSON string below
json = "{}"
# create an instance of CustomListAttributes from a JSON string
custom_list_attributes_instance = CustomListAttributes.from_json(json)
# print the JSON string representation of the object
print(CustomListAttributes.to_json())

# convert the object into a dict
custom_list_attributes_dict = custom_list_attributes_instance.to_dict()
# create an instance of CustomListAttributes from a dict
custom_list_attributes_form_dict = custom_list_attributes.from_dict(custom_list_attributes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


