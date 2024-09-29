# GetChapterOrderParameter


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **str** |  | [optional] 
**updated_at** | **str** |  | [optional] 
**publish_at** | **str** |  | [optional] 
**readable_at** | **str** |  | [optional] 
**volume** | **str** |  | [optional] 
**chapter** | **str** |  | [optional] 

## Example

```python
from mangadex_openapi.models.get_chapter_order_parameter import GetChapterOrderParameter

# TODO update the JSON string below
json = "{}"
# create an instance of GetChapterOrderParameter from a JSON string
get_chapter_order_parameter_instance = GetChapterOrderParameter.from_json(json)
# print the JSON string representation of the object
print(GetChapterOrderParameter.to_json())

# convert the object into a dict
get_chapter_order_parameter_dict = get_chapter_order_parameter_instance.to_dict()
# create an instance of GetChapterOrderParameter from a dict
get_chapter_order_parameter_form_dict = get_chapter_order_parameter.from_dict(get_chapter_order_parameter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


