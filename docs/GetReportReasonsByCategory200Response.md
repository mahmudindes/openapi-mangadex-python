# GetReportReasonsByCategory200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**result** | **str** |  | [optional] [default to 'ok']
**response** | **str** |  | [optional] [default to 'collection']
**data** | [**List[GetReportReasonsByCategory200ResponseDataInner]**](GetReportReasonsByCategory200ResponseDataInner.md) |  | [optional] 
**limit** | **int** |  | [optional] 
**offset** | **int** |  | [optional] 
**total** | **int** |  | [optional] 

## Example

```python
from mangadex_openapi.models.get_report_reasons_by_category200_response import GetReportReasonsByCategory200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetReportReasonsByCategory200Response from a JSON string
get_report_reasons_by_category200_response_instance = GetReportReasonsByCategory200Response.from_json(json)
# print the JSON string representation of the object
print(GetReportReasonsByCategory200Response.to_json())

# convert the object into a dict
get_report_reasons_by_category200_response_dict = get_report_reasons_by_category200_response_instance.to_dict()
# create an instance of GetReportReasonsByCategory200Response from a dict
get_report_reasons_by_category200_response_form_dict = get_report_reasons_by_category200_response.from_dict(get_report_reasons_by_category200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


