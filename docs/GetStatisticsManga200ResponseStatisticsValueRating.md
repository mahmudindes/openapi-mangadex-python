# GetStatisticsManga200ResponseStatisticsValueRating


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**average** | **float** | Will be nullable if no ratings has been done | [optional] 
**bayesian** | **float** | Average weighted on all the Manga population | [optional] 

## Example

```python
from mangadex_openapi.models.get_statistics_manga200_response_statistics_value_rating import GetStatisticsManga200ResponseStatisticsValueRating

# TODO update the JSON string below
json = "{}"
# create an instance of GetStatisticsManga200ResponseStatisticsValueRating from a JSON string
get_statistics_manga200_response_statistics_value_rating_instance = GetStatisticsManga200ResponseStatisticsValueRating.from_json(json)
# print the JSON string representation of the object
print(GetStatisticsManga200ResponseStatisticsValueRating.to_json())

# convert the object into a dict
get_statistics_manga200_response_statistics_value_rating_dict = get_statistics_manga200_response_statistics_value_rating_instance.to_dict()
# create an instance of GetStatisticsManga200ResponseStatisticsValueRating from a dict
get_statistics_manga200_response_statistics_value_rating_form_dict = get_statistics_manga200_response_statistics_value_rating.from_dict(get_statistics_manga200_response_statistics_value_rating_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


