# ApiClientList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**result** | **str** |  | [optional] [default to 'ok']
**response** | **str** |  | [optional] [default to 'collection']
**data** | [**List[ApiClient]**](ApiClient.md) |  | [optional] 
**limit** | **int** |  | [optional] 
**offset** | **int** |  | [optional] 
**total** | **int** |  | [optional] 

## Example

```python
from mangadex_openapi.models.api_client_list import ApiClientList

# TODO update the JSON string below
json = "{}"
# create an instance of ApiClientList from a JSON string
api_client_list_instance = ApiClientList.from_json(json)
# print the JSON string representation of the object
print(ApiClientList.to_json())

# convert the object into a dict
api_client_list_dict = api_client_list_instance.to_dict()
# create an instance of ApiClientList from a dict
api_client_list_form_dict = api_client_list.from_dict(api_client_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


