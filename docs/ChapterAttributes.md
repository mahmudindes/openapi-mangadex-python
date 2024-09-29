# ChapterAttributes


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** |  | [optional] 
**volume** | **str** |  | [optional] 
**chapter** | **str** |  | [optional] 
**pages** | **int** | Count of readable images for this chapter | [optional] 
**translated_language** | **str** |  | [optional] 
**uploader** | **str** |  | [optional] 
**external_url** | **str** | Denotes a chapter that links to an external source. | [optional] 
**version** | **int** |  | [optional] 
**created_at** | **str** |  | [optional] 
**updated_at** | **str** |  | [optional] 
**publish_at** | **str** |  | [optional] 
**readable_at** | **str** |  | [optional] 

## Example

```python
from mangadex_openapi.models.chapter_attributes import ChapterAttributes

# TODO update the JSON string below
json = "{}"
# create an instance of ChapterAttributes from a JSON string
chapter_attributes_instance = ChapterAttributes.from_json(json)
# print the JSON string representation of the object
print(ChapterAttributes.to_json())

# convert the object into a dict
chapter_attributes_dict = chapter_attributes_instance.to_dict()
# create an instance of ChapterAttributes from a dict
chapter_attributes_form_dict = chapter_attributes.from_dict(chapter_attributes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


