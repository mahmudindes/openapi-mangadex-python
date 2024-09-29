# ReportListResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**result** | **str** |  | [optional] 
**response** | **str** |  | [optional] [default to 'collection']
**data** | [**List[Report]**](Report.md) |  | [optional] 
**limit** | **int** |  | [optional] 
**offset** | **int** |  | [optional] 
**total** | **int** |  | [optional] 

## Example

```python
from mangadex_openapi.models.report_list_response import ReportListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ReportListResponse from a JSON string
report_list_response_instance = ReportListResponse.from_json(json)
# print the JSON string representation of the object
print(ReportListResponse.to_json())

# convert the object into a dict
report_list_response_dict = report_list_response_instance.to_dict()
# create an instance of ReportListResponse from a dict
report_list_response_form_dict = report_list_response.from_dict(report_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


