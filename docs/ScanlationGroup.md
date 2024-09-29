# ScanlationGroup


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**attributes** | [**ScanlationGroupAttributes**](ScanlationGroupAttributes.md) |  | [optional] 
**relationships** | [**List[Relationship]**](Relationship.md) |  | [optional] 

## Example

```python
from mangadex_openapi.models.scanlation_group import ScanlationGroup

# TODO update the JSON string below
json = "{}"
# create an instance of ScanlationGroup from a JSON string
scanlation_group_instance = ScanlationGroup.from_json(json)
# print the JSON string representation of the object
print(ScanlationGroup.to_json())

# convert the object into a dict
scanlation_group_dict = scanlation_group_instance.to_dict()
# create an instance of ScanlationGroup from a dict
scanlation_group_form_dict = scanlation_group.from_dict(scanlation_group_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


