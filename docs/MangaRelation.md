# MangaRelation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**attributes** | [**MangaRelationAttributes**](MangaRelationAttributes.md) |  | [optional] 
**relationships** | [**List[Relationship]**](Relationship.md) |  | [optional] 

## Example

```python
from mangadex_openapi.models.manga_relation import MangaRelation

# TODO update the JSON string below
json = "{}"
# create an instance of MangaRelation from a JSON string
manga_relation_instance = MangaRelation.from_json(json)
# print the JSON string representation of the object
print(MangaRelation.to_json())

# convert the object into a dict
manga_relation_dict = manga_relation_instance.to_dict()
# create an instance of MangaRelation from a dict
manga_relation_form_dict = manga_relation.from_dict(manga_relation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


