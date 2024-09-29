# GetStatisticsManga200ResponseStatisticsValue


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**comments** | [**StatisticsDetailsComments**](StatisticsDetailsComments.md) |  | [optional] 
**rating** | [**GetStatisticsManga200ResponseStatisticsValueRating**](GetStatisticsManga200ResponseStatisticsValueRating.md) |  | [optional] 
**follows** | **int** |  | [optional] 

## Example

```python
from mangadex_openapi.models.get_statistics_manga200_response_statistics_value import GetStatisticsManga200ResponseStatisticsValue

# TODO update the JSON string below
json = "{}"
# create an instance of GetStatisticsManga200ResponseStatisticsValue from a JSON string
get_statistics_manga200_response_statistics_value_instance = GetStatisticsManga200ResponseStatisticsValue.from_json(json)
# print the JSON string representation of the object
print(GetStatisticsManga200ResponseStatisticsValue.to_json())

# convert the object into a dict
get_statistics_manga200_response_statistics_value_dict = get_statistics_manga200_response_statistics_value_instance.to_dict()
# create an instance of GetStatisticsManga200ResponseStatisticsValue from a dict
get_statistics_manga200_response_statistics_value_form_dict = get_statistics_manga200_response_statistics_value.from_dict(get_statistics_manga200_response_statistics_value_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


