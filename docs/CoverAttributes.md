# CoverAttributes


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**volume** | **str** |  | [optional] 
**file_name** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**locale** | **str** |  | [optional] 
**version** | **int** |  | [optional] 
**created_at** | **str** |  | [optional] 
**updated_at** | **str** |  | [optional] 

## Example

```python
from mangadex_openapi.models.cover_attributes import CoverAttributes

# TODO update the JSON string below
json = "{}"
# create an instance of CoverAttributes from a JSON string
cover_attributes_instance = CoverAttributes.from_json(json)
# print the JSON string representation of the object
print(CoverAttributes.to_json())

# convert the object into a dict
cover_attributes_dict = cover_attributes_instance.to_dict()
# create an instance of CoverAttributes from a dict
cover_attributes_form_dict = cover_attributes.from_dict(cover_attributes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


