# TagAttributes


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **Dict[str, str]** |  | [optional] 
**description** | **Dict[str, str]** |  | [optional] 
**group** | **str** |  | [optional] 
**version** | **int** |  | [optional] 

## Example

```python
from mangadex_openapi.models.tag_attributes import TagAttributes

# TODO update the JSON string below
json = "{}"
# create an instance of TagAttributes from a JSON string
tag_attributes_instance = TagAttributes.from_json(json)
# print the JSON string representation of the object
print(TagAttributes.to_json())

# convert the object into a dict
tag_attributes_dict = tag_attributes_instance.to_dict()
# create an instance of TagAttributes from a dict
tag_attributes_form_dict = tag_attributes.from_dict(tag_attributes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


