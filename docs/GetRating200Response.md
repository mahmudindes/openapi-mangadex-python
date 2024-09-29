# GetRating200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**result** | **str** |  | [optional] [default to 'ok']
**ratings** | [**Dict[str, GetRating200ResponseRatingsValue]**](GetRating200ResponseRatingsValue.md) |  | [optional] 

## Example

```python
from mangadex_openapi.models.get_rating200_response import GetRating200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetRating200Response from a JSON string
get_rating200_response_instance = GetRating200Response.from_json(json)
# print the JSON string representation of the object
print(GetRating200Response.to_json())

# convert the object into a dict
get_rating200_response_dict = get_rating200_response_instance.to_dict()
# create an instance of GetRating200Response from a dict
get_rating200_response_form_dict = get_rating200_response.from_dict(get_rating200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


