# MangaCreate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **Dict[str, str]** |  | 
**alt_titles** | **List[Dict[str, str]]** |  | [optional] 
**description** | **Dict[str, str]** |  | [optional] 
**authors** | **List[str]** |  | [optional] 
**artists** | **List[str]** |  | [optional] 
**links** | **Dict[str, str]** |  | [optional] 
**original_language** | **str** |  | 
**last_volume** | **str** |  | [optional] 
**last_chapter** | **str** |  | [optional] 
**publication_demographic** | **str** |  | [optional] 
**status** | **str** |  | 
**year** | **int** | Year of release | [optional] 
**content_rating** | **str** |  | 
**chapter_numbers_reset_on_new_volume** | **bool** |  | [optional] 
**tags** | **List[str]** |  | [optional] 
**primary_cover** | **str** |  | [optional] 
**version** | **int** |  | [optional] 

## Example

```python
from mangadex_openapi.models.manga_create import MangaCreate

# TODO update the JSON string below
json = "{}"
# create an instance of MangaCreate from a JSON string
manga_create_instance = MangaCreate.from_json(json)
# print the JSON string representation of the object
print(MangaCreate.to_json())

# convert the object into a dict
manga_create_dict = manga_create_instance.to_dict()
# create an instance of MangaCreate from a dict
manga_create_form_dict = manga_create.from_dict(manga_create_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


