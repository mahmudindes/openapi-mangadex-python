# MangaRelationList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**result** | **str** |  | [optional] [default to 'ok']
**response** | **str** |  | [optional] [default to 'collection']
**data** | [**List[MangaRelation]**](MangaRelation.md) |  | [optional] 
**limit** | **int** |  | [optional] 
**offset** | **int** |  | [optional] 
**total** | **int** |  | [optional] 

## Example

```python
from mangadex_openapi.models.manga_relation_list import MangaRelationList

# TODO update the JSON string below
json = "{}"
# create an instance of MangaRelationList from a JSON string
manga_relation_list_instance = MangaRelationList.from_json(json)
# print the JSON string representation of the object
print(MangaRelationList.to_json())

# convert the object into a dict
manga_relation_list_dict = manga_relation_list_instance.to_dict()
# create an instance of MangaRelationList from a dict
manga_relation_list_form_dict = manga_relation_list.from_dict(manga_relation_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


