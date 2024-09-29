# ChapterResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**result** | **str** |  | [optional] 
**response** | **str** |  | [optional] [default to 'entity']
**data** | [**Chapter**](Chapter.md) |  | [optional] 

## Example

```python
from mangadex_openapi.models.chapter_response import ChapterResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ChapterResponse from a JSON string
chapter_response_instance = ChapterResponse.from_json(json)
# print the JSON string representation of the object
print(ChapterResponse.to_json())

# convert the object into a dict
chapter_response_dict = chapter_response_instance.to_dict()
# create an instance of ChapterResponse from a dict
chapter_response_form_dict = chapter_response.from_dict(chapter_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


