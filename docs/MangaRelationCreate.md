# MangaRelationCreate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**target_manga** | **str** |  | 
**relation** | **str** |  | 

## Example

```python
from mangadex_openapi.models.manga_relation_create import MangaRelationCreate

# TODO update the JSON string below
json = "{}"
# create an instance of MangaRelationCreate from a JSON string
manga_relation_create_instance = MangaRelationCreate.from_json(json)
# print the JSON string representation of the object
print(MangaRelationCreate.to_json())

# convert the object into a dict
manga_relation_create_dict = manga_relation_create_instance.to_dict()
# create an instance of MangaRelationCreate from a dict
manga_relation_create_form_dict = manga_relation_create.from_dict(manga_relation_create_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


