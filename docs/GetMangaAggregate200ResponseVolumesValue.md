# GetMangaAggregate200ResponseVolumesValue


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**volume** | **str** |  | [optional] 
**count** | **int** |  | [optional] 
**chapters** | [**Dict[str, GetMangaAggregate200ResponseVolumesValueChaptersValue]**](GetMangaAggregate200ResponseVolumesValueChaptersValue.md) |  | [optional] 

## Example

```python
from mangadex_openapi.models.get_manga_aggregate200_response_volumes_value import GetMangaAggregate200ResponseVolumesValue

# TODO update the JSON string below
json = "{}"
# create an instance of GetMangaAggregate200ResponseVolumesValue from a JSON string
get_manga_aggregate200_response_volumes_value_instance = GetMangaAggregate200ResponseVolumesValue.from_json(json)
# print the JSON string representation of the object
print(GetMangaAggregate200ResponseVolumesValue.to_json())

# convert the object into a dict
get_manga_aggregate200_response_volumes_value_dict = get_manga_aggregate200_response_volumes_value_instance.to_dict()
# create an instance of GetMangaAggregate200ResponseVolumesValue from a dict
get_manga_aggregate200_response_volumes_value_form_dict = get_manga_aggregate200_response_volumes_value.from_dict(get_manga_aggregate200_response_volumes_value_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


