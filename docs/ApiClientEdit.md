# ApiClientEdit


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** |  | [optional] 
**version** | **int** |  | 

## Example

```python
from mangadex_openapi.models.api_client_edit import ApiClientEdit

# TODO update the JSON string below
json = "{}"
# create an instance of ApiClientEdit from a JSON string
api_client_edit_instance = ApiClientEdit.from_json(json)
# print the JSON string representation of the object
print(ApiClientEdit.to_json())

# convert the object into a dict
api_client_edit_dict = api_client_edit_instance.to_dict()
# create an instance of ApiClientEdit from a dict
api_client_edit_form_dict = api_client_edit.from_dict(api_client_edit_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


