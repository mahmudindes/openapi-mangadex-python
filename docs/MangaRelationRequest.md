# MangaRelationRequest



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**target_manga** | **str** |  | [optional] 
**relation** | **str** |  | [optional] 

## Example

```python
from mangadex_openapi.models.manga_relation_request import MangaRelationRequest

# TODO update the JSON string below
json = "{}"
# create an instance of MangaRelationRequest from a JSON string
manga_relation_request_instance = MangaRelationRequest.from_json(json)
# print the JSON string representation of the object
print(MangaRelationRequest.to_json())

# convert the object into a dict
manga_relation_request_dict = manga_relation_request_instance.to_dict()
# create an instance of MangaRelationRequest from a dict
manga_relation_request_form_dict = manga_relation_request.from_dict(manga_relation_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


