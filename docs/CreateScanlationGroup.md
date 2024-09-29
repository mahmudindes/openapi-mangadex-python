# CreateScanlationGroup


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**website** | **str** |  | [optional] 
**irc_server** | **str** |  | [optional] 
**irc_channel** | **str** |  | [optional] 
**discord** | **str** |  | [optional] 
**contact_email** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**twitter** | **str** |  | [optional] 
**manga_updates** | **str** |  | [optional] 
**inactive** | **bool** |  | [optional] 
**publish_delay** | **str** |  | [optional] 

## Example

```python
from mangadex_openapi.models.create_scanlation_group import CreateScanlationGroup

# TODO update the JSON string below
json = "{}"
# create an instance of CreateScanlationGroup from a JSON string
create_scanlation_group_instance = CreateScanlationGroup.from_json(json)
# print the JSON string representation of the object
print(CreateScanlationGroup.to_json())

# convert the object into a dict
create_scanlation_group_dict = create_scanlation_group_instance.to_dict()
# create an instance of CreateScanlationGroup from a dict
create_scanlation_group_form_dict = create_scanlation_group.from_dict(create_scanlation_group_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


