# GetStatisticsMangaUuid200ResponseStatisticsValueRating


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**average** | **float** | Will be nullable if no ratings has been given | [optional] 
**bayesian** | **float** | Average weighted on all the Manga population | [optional] 
**distribution** | [**GetStatisticsMangaUuid200ResponseStatisticsValueRatingDistribution**](GetStatisticsMangaUuid200ResponseStatisticsValueRatingDistribution.md) |  | [optional] 

## Example

```python
from mangadex_openapi.models.get_statistics_manga_uuid200_response_statistics_value_rating import GetStatisticsMangaUuid200ResponseStatisticsValueRating

# TODO update the JSON string below
json = "{}"
# create an instance of GetStatisticsMangaUuid200ResponseStatisticsValueRating from a JSON string
get_statistics_manga_uuid200_response_statistics_value_rating_instance = GetStatisticsMangaUuid200ResponseStatisticsValueRating.from_json(json)
# print the JSON string representation of the object
print(GetStatisticsMangaUuid200ResponseStatisticsValueRating.to_json())

# convert the object into a dict
get_statistics_manga_uuid200_response_statistics_value_rating_dict = get_statistics_manga_uuid200_response_statistics_value_rating_instance.to_dict()
# create an instance of GetStatisticsMangaUuid200ResponseStatisticsValueRating from a dict
get_statistics_manga_uuid200_response_statistics_value_rating_form_dict = get_statistics_manga_uuid200_response_statistics_value_rating.from_dict(get_statistics_manga_uuid200_response_statistics_value_rating_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


