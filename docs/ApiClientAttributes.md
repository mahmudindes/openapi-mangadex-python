# ApiClientAttributes


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**profile** | **str** |  | [optional] 
**external_client_id** | **str** |  | [optional] 
**is_active** | **bool** |  | [optional] 
**state** | **str** |  | [optional] 
**created_at** | **str** |  | [optional] 
**updated_at** | **str** |  | [optional] 
**version** | **int** |  | [optional] 

## Example

```python
from mangadex_openapi.models.api_client_attributes import ApiClientAttributes

# TODO update the JSON string below
json = "{}"
# create an instance of ApiClientAttributes from a JSON string
api_client_attributes_instance = ApiClientAttributes.from_json(json)
# print the JSON string representation of the object
print(ApiClientAttributes.to_json())

# convert the object into a dict
api_client_attributes_dict = api_client_attributes_instance.to_dict()
# create an instance of ApiClientAttributes from a dict
api_client_attributes_form_dict = api_client_attributes.from_dict(api_client_attributes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


