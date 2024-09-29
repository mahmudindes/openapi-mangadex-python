# CustomListCreate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**visibility** | **str** |  | [optional] 
**manga** | **List[str]** |  | [optional] 
**version** | **int** |  | [optional] 

## Example

```python
from mangadex_openapi.models.custom_list_create import CustomListCreate

# TODO update the JSON string below
json = "{}"
# create an instance of CustomListCreate from a JSON string
custom_list_create_instance = CustomListCreate.from_json(json)
# print the JSON string representation of the object
print(CustomListCreate.to_json())

# convert the object into a dict
custom_list_create_dict = custom_list_create_instance.to_dict()
# create an instance of CustomListCreate from a dict
custom_list_create_form_dict = custom_list_create.from_dict(custom_list_create_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


