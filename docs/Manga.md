# Manga


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**attributes** | [**MangaAttributes**](MangaAttributes.md) |  | [optional] 
**relationships** | [**List[Relationship]**](Relationship.md) |  | [optional] 

## Example

```python
from mangadex_openapi.models.manga import Manga

# TODO update the JSON string below
json = "{}"
# create an instance of Manga from a JSON string
manga_instance = Manga.from_json(json)
# print the JSON string representation of the object
print(Manga.to_json())

# convert the object into a dict
manga_dict = manga_instance.to_dict()
# create an instance of Manga from a dict
manga_form_dict = manga.from_dict(manga_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


