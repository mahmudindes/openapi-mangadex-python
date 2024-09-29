# MangaRequest



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **Dict[str, str]** |  | [optional] 
**alt_titles** | **List[Dict[str, str]]** |  | [optional] 
**description** | **Dict[str, str]** |  | [optional] 
**authors** | **List[str]** |  | [optional] 
**artists** | **List[str]** |  | [optional] 
**links** | **Dict[str, str]** |  | [optional] 
**original_language** | **str** |  | [optional] 
**last_volume** | **str** |  | [optional] 
**last_chapter** | **str** |  | [optional] 
**publication_demographic** | **str** |  | [optional] 
**status** | **str** |  | [optional] 
**year** | **int** | Year of release | [optional] 
**content_rating** | **str** |  | [optional] 
**chapter_numbers_reset_on_new_volume** | **bool** |  | [optional] 
**tags** | **List[str]** |  | [optional] 
**primary_cover** | **str** |  | [optional] 
**version** | **int** |  | [optional] 

## Example

```python
from mangadex_openapi.models.manga_request import MangaRequest

# TODO update the JSON string below
json = "{}"
# create an instance of MangaRequest from a JSON string
manga_request_instance = MangaRequest.from_json(json)
# print the JSON string representation of the object
print(MangaRequest.to_json())

# convert the object into a dict
manga_request_dict = manga_request_instance.to_dict()
# create an instance of MangaRequest from a dict
manga_request_form_dict = manga_request.from_dict(manga_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


