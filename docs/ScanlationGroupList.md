# ScanlationGroupList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**result** | **str** |  | [optional] [default to 'ok']
**response** | **str** |  | [optional] [default to 'collection']
**data** | [**List[ScanlationGroup]**](ScanlationGroup.md) |  | [optional] 
**limit** | **int** |  | [optional] 
**offset** | **int** |  | [optional] 
**total** | **int** |  | [optional] 

## Example

```python
from mangadex_openapi.models.scanlation_group_list import ScanlationGroupList

# TODO update the JSON string below
json = "{}"
# create an instance of ScanlationGroupList from a JSON string
scanlation_group_list_instance = ScanlationGroupList.from_json(json)
# print the JSON string representation of the object
print(ScanlationGroupList.to_json())

# convert the object into a dict
scanlation_group_list_dict = scanlation_group_list_instance.to_dict()
# create an instance of ScanlationGroupList from a dict
scanlation_group_list_form_dict = scanlation_group_list.from_dict(scanlation_group_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


