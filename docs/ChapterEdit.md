# ChapterEdit


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** |  | [optional] 
**volume** | **str** |  | [optional] 
**chapter** | **str** |  | [optional] 
**translated_language** | **str** |  | [optional] 
**groups** | **List[str]** |  | [optional] 
**version** | **int** |  | 

## Example

```python
from mangadex_openapi.models.chapter_edit import ChapterEdit

# TODO update the JSON string below
json = "{}"
# create an instance of ChapterEdit from a JSON string
chapter_edit_instance = ChapterEdit.from_json(json)
# print the JSON string representation of the object
print(ChapterEdit.to_json())

# convert the object into a dict
chapter_edit_dict = chapter_edit_instance.to_dict()
# create an instance of ChapterEdit from a dict
chapter_edit_form_dict = chapter_edit.from_dict(chapter_edit_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


