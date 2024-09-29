# ChapterRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** |  | [optional] 
**volume** | **str** |  | [optional] 
**chapter** | **str** |  | [optional] 
**translated_language** | **str** |  | [optional] 
**groups** | **List[str]** |  | [optional] 
**version** | **int** |  | [optional] 

## Example

```python
from mangadex_openapi.models.chapter_request import ChapterRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ChapterRequest from a JSON string
chapter_request_instance = ChapterRequest.from_json(json)
# print the JSON string representation of the object
print(ChapterRequest.to_json())

# convert the object into a dict
chapter_request_dict = chapter_request_instance.to_dict()
# create an instance of ChapterRequest from a dict
chapter_request_form_dict = chapter_request.from_dict(chapter_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


