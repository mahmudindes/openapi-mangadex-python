# ChapterList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**result** | **str** |  | [optional] [default to 'ok']
**response** | **str** |  | [optional] [default to 'collection']
**data** | [**List[Chapter]**](Chapter.md) |  | [optional] 
**limit** | **int** |  | [optional] 
**offset** | **int** |  | [optional] 
**total** | **int** |  | [optional] 

## Example

```python
from mangadex_openapi.models.chapter_list import ChapterList

# TODO update the JSON string below
json = "{}"
# create an instance of ChapterList from a JSON string
chapter_list_instance = ChapterList.from_json(json)
# print the JSON string representation of the object
print(ChapterList.to_json())

# convert the object into a dict
chapter_list_dict = chapter_list_instance.to_dict()
# create an instance of ChapterList from a dict
chapter_list_form_dict = chapter_list.from_dict(chapter_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


