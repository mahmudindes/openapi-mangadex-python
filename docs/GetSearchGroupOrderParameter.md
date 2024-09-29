# GetSearchGroupOrderParameter


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**created_at** | **str** |  | [optional] 
**updated_at** | **str** |  | [optional] 
**followed_count** | **str** |  | [optional] 
**relevance** | **str** |  | [optional] 

## Example

```python
from mangadex_openapi.models.get_search_group_order_parameter import GetSearchGroupOrderParameter

# TODO update the JSON string below
json = "{}"
# create an instance of GetSearchGroupOrderParameter from a JSON string
get_search_group_order_parameter_instance = GetSearchGroupOrderParameter.from_json(json)
# print the JSON string representation of the object
print(GetSearchGroupOrderParameter.to_json())

# convert the object into a dict
get_search_group_order_parameter_dict = get_search_group_order_parameter_instance.to_dict()
# create an instance of GetSearchGroupOrderParameter from a dict
get_search_group_order_parameter_form_dict = get_search_group_order_parameter.from_dict(get_search_group_order_parameter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


