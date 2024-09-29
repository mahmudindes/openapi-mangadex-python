# CoverList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**result** | **str** |  | [optional] [default to 'ok']
**response** | **str** |  | [optional] [default to 'collection']
**data** | [**List[Cover]**](Cover.md) |  | [optional] 
**limit** | **int** |  | [optional] 
**offset** | **int** |  | [optional] 
**total** | **int** |  | [optional] 

## Example

```python
from mangadex_openapi.models.cover_list import CoverList

# TODO update the JSON string below
json = "{}"
# create an instance of CoverList from a JSON string
cover_list_instance = CoverList.from_json(json)
# print the JSON string representation of the object
print(CoverList.to_json())

# convert the object into a dict
cover_list_dict = cover_list_instance.to_dict()
# create an instance of CoverList from a dict
cover_list_form_dict = cover_list.from_dict(cover_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


