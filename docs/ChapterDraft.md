# ChapterDraft


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**volume** | **str** |  | 
**chapter** | **str** |  | 
**title** | **str** |  | 
**translated_language** | **str** |  | 
**external_url** | **str** |  | [optional] 
**publish_at** | **str** |  | [optional] 

## Example

```python
from mangadex_openapi.models.chapter_draft import ChapterDraft

# TODO update the JSON string below
json = "{}"
# create an instance of ChapterDraft from a JSON string
chapter_draft_instance = ChapterDraft.from_json(json)
# print the JSON string representation of the object
print(ChapterDraft.to_json())

# convert the object into a dict
chapter_draft_dict = chapter_draft_instance.to_dict()
# create an instance of ChapterDraft from a dict
chapter_draft_form_dict = chapter_draft.from_dict(chapter_draft_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


