# CheckResponse



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**result** | **str** |  | [optional] [default to 'ok']
**is_authenticated** | **bool** |  | [optional] 
**roles** | **List[str]** |  | [optional] 
**permissions** | **List[str]** |  | [optional] 

## Example

```python
from mangadex_openapi.models.check_response import CheckResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CheckResponse from a JSON string
check_response_instance = CheckResponse.from_json(json)
# print the JSON string representation of the object
print(CheckResponse.to_json())

# convert the object into a dict
check_response_dict = check_response_instance.to_dict()
# create an instance of CheckResponse from a dict
check_response_form_dict = check_response.from_dict(check_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


