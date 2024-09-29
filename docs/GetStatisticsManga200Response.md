# GetStatisticsManga200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**result** | **str** |  | [optional] [default to 'ok']
**statistics** | [**Dict[str, GetStatisticsManga200ResponseStatisticsValue]**](GetStatisticsManga200ResponseStatisticsValue.md) |  | [optional] 

## Example

```python
from mangadex_openapi.models.get_statistics_manga200_response import GetStatisticsManga200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetStatisticsManga200Response from a JSON string
get_statistics_manga200_response_instance = GetStatisticsManga200Response.from_json(json)
# print the JSON string representation of the object
print(GetStatisticsManga200Response.to_json())

# convert the object into a dict
get_statistics_manga200_response_dict = get_statistics_manga200_response_instance.to_dict()
# create an instance of GetStatisticsManga200Response from a dict
get_statistics_manga200_response_form_dict = get_statistics_manga200_response.from_dict(get_statistics_manga200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


