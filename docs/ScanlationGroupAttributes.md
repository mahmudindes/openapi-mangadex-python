# ScanlationGroupAttributes


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**alt_names** | **List[Dict[str, str]]** |  | [optional] 
**website** | **str** |  | [optional] 
**irc_server** | **str** |  | [optional] 
**irc_channel** | **str** |  | [optional] 
**discord** | **str** |  | [optional] 
**contact_email** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**twitter** | **str** |  | [optional] 
**manga_updates** | **str** |  | [optional] 
**focused_language** | **List[str]** |  | [optional] 
**locked** | **bool** |  | [optional] 
**official** | **bool** |  | [optional] 
**verified** | **bool** |  | [optional] 
**inactive** | **bool** |  | [optional] 
**ex_licensed** | **bool** |  | [optional] 
**publish_delay** | **str** | Should respected ISO 8601 duration specification: https://en.wikipedia.org/wiki/ISO_8601#Durations | [optional] 
**version** | **int** |  | [optional] 
**created_at** | **str** |  | [optional] 
**updated_at** | **str** |  | [optional] 

## Example

```python
from mangadex_openapi.models.scanlation_group_attributes import ScanlationGroupAttributes

# TODO update the JSON string below
json = "{}"
# create an instance of ScanlationGroupAttributes from a JSON string
scanlation_group_attributes_instance = ScanlationGroupAttributes.from_json(json)
# print the JSON string representation of the object
print(ScanlationGroupAttributes.to_json())

# convert the object into a dict
scanlation_group_attributes_dict = scanlation_group_attributes_instance.to_dict()
# create an instance of ScanlationGroupAttributes from a dict
scanlation_group_attributes_form_dict = scanlation_group_attributes.from_dict(scanlation_group_attributes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


