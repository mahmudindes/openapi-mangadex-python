# MappingIdResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**result** | **str** |  | [optional] [default to 'ok']
**response** | **str** |  | [optional] [default to 'collection']
**data** | [**List[MappingId]**](MappingId.md) |  | [optional] 
**limit** | **int** |  | [optional] 
**offset** | **int** |  | [optional] 
**total** | **int** |  | [optional] 

## Example

```python
from mangadex_openapi.models.mapping_id_response import MappingIdResponse

# TODO update the JSON string below
json = "{}"
# create an instance of MappingIdResponse from a JSON string
mapping_id_response_instance = MappingIdResponse.from_json(json)
# print the JSON string representation of the object
print(MappingIdResponse.to_json())

# convert the object into a dict
mapping_id_response_dict = mapping_id_response_instance.to_dict()
# create an instance of MappingIdResponse from a dict
mapping_id_response_form_dict = mapping_id_response.from_dict(mapping_id_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


