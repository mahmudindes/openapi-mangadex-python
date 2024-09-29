# GetReportReasonsByCategory200ResponseDataInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**type** | **str** |  | [optional] [default to 'report_reason']
**attributes** | [**GetReportReasonsByCategory200ResponseDataInnerAttributes**](GetReportReasonsByCategory200ResponseDataInnerAttributes.md) |  | [optional] 

## Example

```python
from mangadex_openapi.models.get_report_reasons_by_category200_response_data_inner import GetReportReasonsByCategory200ResponseDataInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetReportReasonsByCategory200ResponseDataInner from a JSON string
get_report_reasons_by_category200_response_data_inner_instance = GetReportReasonsByCategory200ResponseDataInner.from_json(json)
# print the JSON string representation of the object
print(GetReportReasonsByCategory200ResponseDataInner.to_json())

# convert the object into a dict
get_report_reasons_by_category200_response_data_inner_dict = get_report_reasons_by_category200_response_data_inner_instance.to_dict()
# create an instance of GetReportReasonsByCategory200ResponseDataInner from a dict
get_report_reasons_by_category200_response_data_inner_form_dict = get_report_reasons_by_category200_response_data_inner.from_dict(get_report_reasons_by_category200_response_data_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


