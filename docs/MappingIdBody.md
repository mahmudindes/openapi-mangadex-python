# MappingIdBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] 
**ids** | **List[int]** |  | [optional] 

## Example

```python
from mangadex_openapi.models.mapping_id_body import MappingIdBody

# TODO update the JSON string below
json = "{}"
# create an instance of MappingIdBody from a JSON string
mapping_id_body_instance = MappingIdBody.from_json(json)
# print the JSON string representation of the object
print(MappingIdBody.to_json())

# convert the object into a dict
mapping_id_body_dict = mapping_id_body_instance.to_dict()
# create an instance of MappingIdBody from a dict
mapping_id_body_form_dict = mapping_id_body.from_dict(mapping_id_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


