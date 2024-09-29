# MangaList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**result** | **str** |  | [optional] [default to 'ok']
**response** | **str** |  | [optional] [default to 'collection']
**data** | [**List[Manga]**](Manga.md) |  | [optional] 
**limit** | **int** |  | [optional] 
**offset** | **int** |  | [optional] 
**total** | **int** |  | [optional] 

## Example

```python
from mangadex_openapi.models.manga_list import MangaList

# TODO update the JSON string below
json = "{}"
# create an instance of MangaList from a JSON string
manga_list_instance = MangaList.from_json(json)
# print the JSON string representation of the object
print(MangaList.to_json())

# convert the object into a dict
manga_list_dict = manga_list_instance.to_dict()
# create an instance of MangaList from a dict
manga_list_form_dict = manga_list.from_dict(manga_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


