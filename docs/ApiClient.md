# ApiClient


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**attributes** | [**ApiClientAttributes**](ApiClientAttributes.md) |  | [optional] 
**relationships** | [**List[Relationship]**](Relationship.md) |  | [optional] 

## Example

```python
from mangadex_openapi.models.api_client import ApiClient

# TODO update the JSON string below
json = "{}"
# create an instance of ApiClient from a JSON string
api_client_instance = ApiClient.from_json(json)
# print the JSON string representation of the object
print(ApiClient.to_json())

# convert the object into a dict
api_client_dict = api_client_instance.to_dict()
# create an instance of ApiClient from a dict
api_client_form_dict = api_client.from_dict(api_client_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


