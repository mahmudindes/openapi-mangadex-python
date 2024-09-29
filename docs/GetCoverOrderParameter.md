# GetCoverOrderParameter


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **str** |  | [optional] 
**updated_at** | **str** |  | [optional] 
**volume** | **str** |  | [optional] 

## Example

```python
from mangadex_openapi.models.get_cover_order_parameter import GetCoverOrderParameter

# TODO update the JSON string below
json = "{}"
# create an instance of GetCoverOrderParameter from a JSON string
get_cover_order_parameter_instance = GetCoverOrderParameter.from_json(json)
# print the JSON string representation of the object
print(GetCoverOrderParameter.to_json())

# convert the object into a dict
get_cover_order_parameter_dict = get_cover_order_parameter_instance.to_dict()
# create an instance of GetCoverOrderParameter from a dict
get_cover_order_parameter_form_dict = get_cover_order_parameter.from_dict(get_cover_order_parameter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


