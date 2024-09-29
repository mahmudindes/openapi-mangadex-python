# Chapter


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**attributes** | [**ChapterAttributes**](ChapterAttributes.md) |  | [optional] 
**relationships** | [**List[Relationship]**](Relationship.md) |  | [optional] 

## Example

```python
from mangadex_openapi.models.chapter import Chapter

# TODO update the JSON string below
json = "{}"
# create an instance of Chapter from a JSON string
chapter_instance = Chapter.from_json(json)
# print the JSON string representation of the object
print(Chapter.to_json())

# convert the object into a dict
chapter_dict = chapter_instance.to_dict()
# create an instance of Chapter from a dict
chapter_form_dict = chapter.from_dict(chapter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


