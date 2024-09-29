# MangaRelationResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**result** | **str** |  | [optional] 
**response** | **str** |  | [optional] [default to 'entity']
**data** | [**MangaRelation**](MangaRelation.md) |  | [optional] 

## Example

```python
from mangadex_openapi.models.manga_relation_response import MangaRelationResponse

# TODO update the JSON string below
json = "{}"
# create an instance of MangaRelationResponse from a JSON string
manga_relation_response_instance = MangaRelationResponse.from_json(json)
# print the JSON string representation of the object
print(MangaRelationResponse.to_json())

# convert the object into a dict
manga_relation_response_dict = manga_relation_response_instance.to_dict()
# create an instance of MangaRelationResponse from a dict
manga_relation_response_form_dict = manga_relation_response.from_dict(manga_relation_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


