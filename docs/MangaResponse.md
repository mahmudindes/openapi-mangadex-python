# MangaResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**result** | **str** |  | [optional] 
**response** | **str** |  | [optional] [default to 'entity']
**data** | [**Manga**](Manga.md) |  | [optional] 

## Example

```python
from mangadex_openapi.models.manga_response import MangaResponse

# TODO update the JSON string below
json = "{}"
# create an instance of MangaResponse from a JSON string
manga_response_instance = MangaResponse.from_json(json)
# print the JSON string representation of the object
print(MangaResponse.to_json())

# convert the object into a dict
manga_response_dict = manga_response_instance.to_dict()
# create an instance of MangaResponse from a dict
manga_response_form_dict = manga_response.from_dict(manga_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


