# ApiClientCreate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**description** | **str** |  | [optional] 
**profile** | **str** |  | 
**version** | **int** |  | [optional] 

## Example

```python
from mangadex_openapi.models.api_client_create import ApiClientCreate

# TODO update the JSON string below
json = "{}"
# create an instance of ApiClientCreate from a JSON string
api_client_create_instance = ApiClientCreate.from_json(json)
# print the JSON string representation of the object
print(ApiClientCreate.to_json())

# convert the object into a dict
api_client_create_dict = api_client_create_instance.to_dict()
# create an instance of ApiClientCreate from a dict
api_client_create_form_dict = api_client_create.from_dict(api_client_create_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


