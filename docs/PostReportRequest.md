# PostReportRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**category** | **str** |  | [optional] 
**reason** | **str** |  | [optional] 
**object_id** | **str** |  | [optional] 
**details** | **str** |  | [optional] 

## Example

```python
from mangadex_openapi.models.post_report_request import PostReportRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PostReportRequest from a JSON string
post_report_request_instance = PostReportRequest.from_json(json)
# print the JSON string representation of the object
print(PostReportRequest.to_json())

# convert the object into a dict
post_report_request_dict = post_report_request_instance.to_dict()
# create an instance of PostReportRequest from a dict
post_report_request_form_dict = post_report_request.from_dict(post_report_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


