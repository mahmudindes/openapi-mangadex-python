# ChapterReadMarkerBatch


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**chapter_ids_read** | **List[str]** |  | [optional] 
**chapter_ids_unread** | **List[str]** |  | [optional] 

## Example

```python
from mangadex_openapi.models.chapter_read_marker_batch import ChapterReadMarkerBatch

# TODO update the JSON string below
json = "{}"
# create an instance of ChapterReadMarkerBatch from a JSON string
chapter_read_marker_batch_instance = ChapterReadMarkerBatch.from_json(json)
# print the JSON string representation of the object
print(ChapterReadMarkerBatch.to_json())

# convert the object into a dict
chapter_read_marker_batch_dict = chapter_read_marker_batch_instance.to_dict()
# create an instance of ChapterReadMarkerBatch from a dict
chapter_read_marker_batch_form_dict = chapter_read_marker_batch.from_dict(chapter_read_marker_batch_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


