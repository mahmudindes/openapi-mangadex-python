# AccountActivateResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**result** | **str** |  | [optional] 

## Example

```python
from mangadex_openapi.models.account_activate_response import AccountActivateResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AccountActivateResponse from a JSON string
account_activate_response_instance = AccountActivateResponse.from_json(json)
# print the JSON string representation of the object
print(AccountActivateResponse.to_json())

# convert the object into a dict
account_activate_response_dict = account_activate_response_instance.to_dict()
# create an instance of AccountActivateResponse from a dict
account_activate_response_form_dict = account_activate_response.from_dict(account_activate_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


