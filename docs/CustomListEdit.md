# CustomListEdit


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**visibility** | **str** |  | [optional] 
**manga** | **List[str]** |  | [optional] 
**version** | **int** |  | 

## Example

```python
from mangadex_openapi.models.custom_list_edit import CustomListEdit

# TODO update the JSON string below
json = "{}"
# create an instance of CustomListEdit from a JSON string
custom_list_edit_instance = CustomListEdit.from_json(json)
# print the JSON string representation of the object
print(CustomListEdit.to_json())

# convert the object into a dict
custom_list_edit_dict = custom_list_edit_instance.to_dict()
# create an instance of CustomListEdit from a dict
custom_list_edit_form_dict = custom_list_edit.from_dict(custom_list_edit_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


