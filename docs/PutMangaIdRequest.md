# PutMangaIdRequest


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
**version** | **int** |  | 

## Example

```python
from mangadex_openapi.models.put_manga_id_request import PutMangaIdRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PutMangaIdRequest from a JSON string
put_manga_id_request_instance = PutMangaIdRequest.from_json(json)
# print the JSON string representation of the object
print(PutMangaIdRequest.to_json())

# convert the object into a dict
put_manga_id_request_dict = put_manga_id_request_instance.to_dict()
# create an instance of PutMangaIdRequest from a dict
put_manga_id_request_form_dict = put_manga_id_request.from_dict(put_manga_id_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


