# ScanlationGroupEdit


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**leader** | **str** |  | [optional] 
**members** | **List[str]** |  | [optional] 
**website** | **str** |  | [optional] 
**irc_server** | **str** |  | [optional] 
**irc_channel** | **str** |  | [optional] 
**discord** | **str** |  | [optional] 
**contact_email** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**twitter** | **str** |  | [optional] 
**manga_updates** | **str** |  | [optional] 
**focused_languages** | **List[str]** |  | [optional] 
**inactive** | **bool** |  | [optional] 
**locked** | **bool** |  | [optional] 
**publish_delay** | **str** |  | [optional] 
**version** | **int** |  | 

## Example

```python
from mangadex_openapi.models.scanlation_group_edit import ScanlationGroupEdit

# TODO update the JSON string below
json = "{}"
# create an instance of ScanlationGroupEdit from a JSON string
scanlation_group_edit_instance = ScanlationGroupEdit.from_json(json)
# print the JSON string representation of the object
print(ScanlationGroupEdit.to_json())

# convert the object into a dict
scanlation_group_edit_dict = scanlation_group_edit_instance.to_dict()
# create an instance of ScanlationGroupEdit from a dict
scanlation_group_edit_form_dict = scanlation_group_edit.from_dict(scanlation_group_edit_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


