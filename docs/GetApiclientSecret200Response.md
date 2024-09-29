# GetApiclientSecret200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**result** | **str** |  | [optional] 
**data** | **str** |  | [optional] 

## Example

```python
from mangadex_openapi.models.get_apiclient_secret200_response import GetApiclientSecret200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetApiclientSecret200Response from a JSON string
get_apiclient_secret200_response_instance = GetApiclientSecret200Response.from_json(json)
# print the JSON string representation of the object
print(GetApiclientSecret200Response.to_json())

# convert the object into a dict
get_apiclient_secret200_response_dict = get_apiclient_secret200_response_instance.to_dict()
# create an instance of GetApiclientSecret200Response from a dict
get_apiclient_secret200_response_form_dict = get_apiclient_secret200_response.from_dict(get_apiclient_secret200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


