# UpdateMangaStatus


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | 

## Example

```python
from mangadex_openapi.models.update_manga_status import UpdateMangaStatus

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateMangaStatus from a JSON string
update_manga_status_instance = UpdateMangaStatus.from_json(json)
# print the JSON string representation of the object
print(UpdateMangaStatus.to_json())

# convert the object into a dict
update_manga_status_dict = update_manga_status_instance.to_dict()
# create an instance of UpdateMangaStatus from a dict
update_manga_status_form_dict = update_manga_status.from_dict(update_manga_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


