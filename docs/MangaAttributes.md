# MangaAttributes


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **Dict[str, str]** |  | [optional] 
**alt_titles** | **List[Dict[str, str]]** |  | [optional] 
**description** | **Dict[str, str]** |  | [optional] 
**is_locked** | **bool** |  | [optional] 
**links** | **Dict[str, str]** |  | [optional] 
**original_language** | **str** |  | [optional] 
**last_volume** | **str** |  | [optional] 
**last_chapter** | **str** |  | [optional] 
**publication_demographic** | **str** |  | [optional] 
**status** | **str** |  | [optional] 
**year** | **int** | Year of release | [optional] 
**content_rating** | **str** |  | [optional] 
**chapter_numbers_reset_on_new_volume** | **bool** |  | [optional] 
**available_translated_languages** | **List[Optional[str]]** |  | [optional] 
**latest_uploaded_chapter** | **str** |  | [optional] 
**tags** | [**List[Tag]**](Tag.md) |  | [optional] 
**state** | **str** |  | [optional] 
**version** | **int** |  | [optional] 
**created_at** | **str** |  | [optional] 
**updated_at** | **str** |  | [optional] 

## Example

```python
from mangadex_openapi.models.manga_attributes import MangaAttributes

# TODO update the JSON string below
json = "{}"
# create an instance of MangaAttributes from a JSON string
manga_attributes_instance = MangaAttributes.from_json(json)
# print the JSON string representation of the object
print(MangaAttributes.to_json())

# convert the object into a dict
manga_attributes_dict = manga_attributes_instance.to_dict()
# create an instance of MangaAttributes from a dict
manga_attributes_form_dict = manga_attributes.from_dict(manga_attributes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


