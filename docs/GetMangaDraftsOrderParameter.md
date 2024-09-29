# GetMangaDraftsOrderParameter


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** |  | [optional] 
**year** | **str** |  | [optional] 
**created_at** | **str** |  | [optional] 
**updated_at** | **str** |  | [optional] 

## Example

```python
from mangadex_openapi.models.get_manga_drafts_order_parameter import GetMangaDraftsOrderParameter

# TODO update the JSON string below
json = "{}"
# create an instance of GetMangaDraftsOrderParameter from a JSON string
get_manga_drafts_order_parameter_instance = GetMangaDraftsOrderParameter.from_json(json)
# print the JSON string representation of the object
print(GetMangaDraftsOrderParameter.to_json())

# convert the object into a dict
get_manga_drafts_order_parameter_dict = get_manga_drafts_order_parameter_instance.to_dict()
# create an instance of GetMangaDraftsOrderParameter from a dict
get_manga_drafts_order_parameter_form_dict = get_manga_drafts_order_parameter.from_dict(get_manga_drafts_order_parameter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


