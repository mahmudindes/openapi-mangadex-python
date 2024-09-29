# CoverEdit


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**volume** | **str** |  | 
**description** | **str** |  | [optional] 
**locale** | **str** |  | [optional] 
**version** | **int** |  | 

## Example

```python
from mangadex_openapi.models.cover_edit import CoverEdit

# TODO update the JSON string below
json = "{}"
# create an instance of CoverEdit from a JSON string
cover_edit_instance = CoverEdit.from_json(json)
# print the JSON string representation of the object
print(CoverEdit.to_json())

# convert the object into a dict
cover_edit_dict = cover_edit_instance.to_dict()
# create an instance of CoverEdit from a dict
cover_edit_form_dict = cover_edit.from_dict(cover_edit_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


