# CoverResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**result** | **str** |  | [optional] 
**response** | **str** |  | [optional] [default to 'entity']
**data** | [**Cover**](Cover.md) |  | [optional] 

## Example

```python
from mangadex_openapi.models.cover_response import CoverResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CoverResponse from a JSON string
cover_response_instance = CoverResponse.from_json(json)
# print the JSON string representation of the object
print(CoverResponse.to_json())

# convert the object into a dict
cover_response_dict = cover_response_instance.to_dict()
# create an instance of CoverResponse from a dict
cover_response_form_dict = cover_response.from_dict(cover_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


