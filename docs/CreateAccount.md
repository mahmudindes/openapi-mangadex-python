# CreateAccount


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**username** | **str** |  | 
**password** | **str** |  | 
**email** | **str** |  | 

## Example

```python
from mangadex_openapi.models.create_account import CreateAccount

# TODO update the JSON string below
json = "{}"
# create an instance of CreateAccount from a JSON string
create_account_instance = CreateAccount.from_json(json)
# print the JSON string representation of the object
print(CreateAccount.to_json())

# convert the object into a dict
create_account_dict = create_account_instance.to_dict()
# create an instance of CreateAccount from a dict
create_account_form_dict = create_account.from_dict(create_account_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


