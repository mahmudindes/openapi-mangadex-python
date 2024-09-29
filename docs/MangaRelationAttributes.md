# MangaRelationAttributes


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**relation** | **str** |  | [optional] 
**version** | **int** |  | [optional] 

## Example

```python
from mangadex_openapi.models.manga_relation_attributes import MangaRelationAttributes

# TODO update the JSON string below
json = "{}"
# create an instance of MangaRelationAttributes from a JSON string
manga_relation_attributes_instance = MangaRelationAttributes.from_json(json)
# print the JSON string representation of the object
print(MangaRelationAttributes.to_json())

# convert the object into a dict
manga_relation_attributes_dict = manga_relation_attributes_instance.to_dict()
# create an instance of MangaRelationAttributes from a dict
manga_relation_attributes_form_dict = manga_relation_attributes.from_dict(manga_relation_attributes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


