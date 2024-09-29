# GetRating200ResponseRatingsValue


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rating** | **int** |  | [optional] 
**created_at** | **datetime** |  | [optional] 

## Example

```python
from mangadex_openapi.models.get_rating200_response_ratings_value import GetRating200ResponseRatingsValue

# TODO update the JSON string below
json = "{}"
# create an instance of GetRating200ResponseRatingsValue from a JSON string
get_rating200_response_ratings_value_instance = GetRating200ResponseRatingsValue.from_json(json)
# print the JSON string representation of the object
print(GetRating200ResponseRatingsValue.to_json())

# convert the object into a dict
get_rating200_response_ratings_value_dict = get_rating200_response_ratings_value_instance.to_dict()
# create an instance of GetRating200ResponseRatingsValue from a dict
get_rating200_response_ratings_value_form_dict = get_rating200_response_ratings_value.from_dict(get_rating200_response_ratings_value_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


