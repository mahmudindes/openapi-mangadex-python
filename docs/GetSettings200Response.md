# GetSettings200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**result** | **str** |  | [optional] [default to 'ok']
**updated_at** | **datetime** |  | [optional] 
**settings** | **object** | Settings that were validated by linked template | [optional] 
**template** | **str** | Settings template UUID | [optional] 

## Example

```python
from mangadex_openapi.models.get_settings200_response import GetSettings200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetSettings200Response from a JSON string
get_settings200_response_instance = GetSettings200Response.from_json(json)
# print the JSON string representation of the object
print(GetSettings200Response.to_json())

# convert the object into a dict
get_settings200_response_dict = get_settings200_response_instance.to_dict()
# create an instance of GetSettings200Response from a dict
get_settings200_response_form_dict = get_settings200_response.from_dict(get_settings200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


