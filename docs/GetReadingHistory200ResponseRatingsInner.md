# GetReadingHistory200ResponseRatingsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**chapter_id** | **str** |  | [optional] 
**read_date** | **datetime** |  | [optional] 

## Example

```python
from mangadex_openapi.models.get_reading_history200_response_ratings_inner import GetReadingHistory200ResponseRatingsInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetReadingHistory200ResponseRatingsInner from a JSON string
get_reading_history200_response_ratings_inner_instance = GetReadingHistory200ResponseRatingsInner.from_json(json)
# print the JSON string representation of the object
print(GetReadingHistory200ResponseRatingsInner.to_json())

# convert the object into a dict
get_reading_history200_response_ratings_inner_dict = get_reading_history200_response_ratings_inner_instance.to_dict()
# create an instance of GetReadingHistory200ResponseRatingsInner from a dict
get_reading_history200_response_ratings_inner_form_dict = get_reading_history200_response_ratings_inner.from_dict(get_reading_history200_response_ratings_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


