# LoginResponseToken


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**session** | **str** |  | [optional] 
**refresh** | **str** |  | [optional] 

## Example

```python
from mangadex_openapi.models.login_response_token import LoginResponseToken

# TODO update the JSON string below
json = "{}"
# create an instance of LoginResponseToken from a JSON string
login_response_token_instance = LoginResponseToken.from_json(json)
# print the JSON string representation of the object
print(LoginResponseToken.to_json())

# convert the object into a dict
login_response_token_dict = login_response_token_instance.to_dict()
# create an instance of LoginResponseToken from a dict
login_response_token_form_dict = login_response_token.from_dict(login_response_token_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


