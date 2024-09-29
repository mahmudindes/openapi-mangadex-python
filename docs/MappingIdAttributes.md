# MappingIdAttributes


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] 
**legacy_id** | **int** |  | [optional] 
**new_id** | **str** |  | [optional] 

## Example

```python
from mangadex_openapi.models.mapping_id_attributes import MappingIdAttributes

# TODO update the JSON string below
json = "{}"
# create an instance of MappingIdAttributes from a JSON string
mapping_id_attributes_instance = MappingIdAttributes.from_json(json)
# print the JSON string representation of the object
print(MappingIdAttributes.to_json())

# convert the object into a dict
mapping_id_attributes_dict = mapping_id_attributes_instance.to_dict()
# create an instance of MappingIdAttributes from a dict
mapping_id_attributes_form_dict = mapping_id_attributes.from_dict(mapping_id_attributes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


