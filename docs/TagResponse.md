# TagResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**result** | **str** |  | [optional] [default to 'ok']
**response** | **str** |  | [optional] [default to 'collection']
**data** | [**List[Tag]**](Tag.md) |  | [optional] 
**limit** | **int** |  | [optional] 
**offset** | **int** |  | [optional] 
**total** | **int** |  | [optional] 

## Example

```python
from mangadex_openapi.models.tag_response import TagResponse

# TODO update the JSON string below
json = "{}"
# create an instance of TagResponse from a JSON string
tag_response_instance = TagResponse.from_json(json)
# print the JSON string representation of the object
print(TagResponse.to_json())

# convert the object into a dict
tag_response_dict = tag_response_instance.to_dict()
# create an instance of TagResponse from a dict
tag_response_form_dict = tag_response.from_dict(tag_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


