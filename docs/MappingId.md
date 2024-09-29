# MappingId


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**attributes** | [**MappingIdAttributes**](MappingIdAttributes.md) |  | [optional] 
**relationships** | [**List[Relationship]**](Relationship.md) |  | [optional] 

## Example

```python
from mangadex_openapi.models.mapping_id import MappingId

# TODO update the JSON string below
json = "{}"
# create an instance of MappingId from a JSON string
mapping_id_instance = MappingId.from_json(json)
# print the JSON string representation of the object
print(MappingId.to_json())

# convert the object into a dict
mapping_id_dict = mapping_id_instance.to_dict()
# create an instance of MappingId from a dict
mapping_id_form_dict = mapping_id.from_dict(mapping_id_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


