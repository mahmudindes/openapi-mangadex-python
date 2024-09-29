# SendAccountActivationCode


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** |  | 

## Example

```python
from mangadex_openapi.models.send_account_activation_code import SendAccountActivationCode

# TODO update the JSON string below
json = "{}"
# create an instance of SendAccountActivationCode from a JSON string
send_account_activation_code_instance = SendAccountActivationCode.from_json(json)
# print the JSON string representation of the object
print(SendAccountActivationCode.to_json())

# convert the object into a dict
send_account_activation_code_dict = send_account_activation_code_instance.to_dict()
# create an instance of SendAccountActivationCode from a dict
send_account_activation_code_form_dict = send_account_activation_code.from_dict(send_account_activation_code_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


