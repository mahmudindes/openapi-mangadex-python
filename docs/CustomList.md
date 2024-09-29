# CustomList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**attributes** | [**CustomListAttributes**](CustomListAttributes.md) |  | [optional] 
**relationships** | [**List[Relationship]**](Relationship.md) |  | [optional] 

## Example

```python
from mangadex_openapi.models.custom_list import CustomList

# TODO update the JSON string below
json = "{}"
# create an instance of CustomList from a JSON string
custom_list_instance = CustomList.from_json(json)
# print the JSON string representation of the object
print(CustomList.to_json())

# convert the object into a dict
custom_list_dict = custom_list_instance.to_dict()
# create an instance of CustomList from a dict
custom_list_form_dict = custom_list.from_dict(custom_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


