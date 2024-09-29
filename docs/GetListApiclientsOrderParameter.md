# GetListApiclientsOrderParameter


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**created_at** | **str** |  | [optional] 
**updated_at** | **str** |  | [optional] 

## Example

```python
from mangadex_openapi.models.get_list_apiclients_order_parameter import GetListApiclientsOrderParameter

# TODO update the JSON string below
json = "{}"
# create an instance of GetListApiclientsOrderParameter from a JSON string
get_list_apiclients_order_parameter_instance = GetListApiclientsOrderParameter.from_json(json)
# print the JSON string representation of the object
print(GetListApiclientsOrderParameter.to_json())

# convert the object into a dict
get_list_apiclients_order_parameter_dict = get_list_apiclients_order_parameter_instance.to_dict()
# create an instance of GetListApiclientsOrderParameter from a dict
get_list_apiclients_order_parameter_form_dict = get_list_apiclients_order_parameter.from_dict(get_list_apiclients_order_parameter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


