# CustomListList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**result** | **str** |  | [optional] [default to 'ok']
**response** | **str** |  | [optional] [default to 'collection']
**data** | [**List[CustomList]**](CustomList.md) |  | [optional] 
**limit** | **int** |  | [optional] 
**offset** | **int** |  | [optional] 
**total** | **int** |  | [optional] 

## Example

```python
from mangadex_openapi.models.custom_list_list import CustomListList

# TODO update the JSON string below
json = "{}"
# create an instance of CustomListList from a JSON string
custom_list_list_instance = CustomListList.from_json(json)
# print the JSON string representation of the object
print(CustomListList.to_json())

# convert the object into a dict
custom_list_list_dict = custom_list_list_instance.to_dict()
# create an instance of CustomListList from a dict
custom_list_list_form_dict = custom_list_list.from_dict(custom_list_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


