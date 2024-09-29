# ApiClientResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**result** | **str** |  | [optional] 
**response** | **str** |  | [optional] [default to 'entity']
**data** | [**ApiClient**](ApiClient.md) |  | [optional] 

## Example

```python
from mangadex_openapi.models.api_client_response import ApiClientResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ApiClientResponse from a JSON string
api_client_response_instance = ApiClientResponse.from_json(json)
# print the JSON string representation of the object
print(ApiClientResponse.to_json())

# convert the object into a dict
api_client_response_dict = api_client_response_instance.to_dict()
# create an instance of ApiClientResponse from a dict
api_client_response_form_dict = api_client_response.from_dict(api_client_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


