# GetReportReasonsByCategory200ResponseDataInnerAttributes


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reason** | **Dict[str, str]** |  | [optional] 
**details_required** | **bool** |  | [optional] 
**category** | **str** |  | [optional] 
**version** | **int** |  | [optional] 

## Example

```python
from mangadex_openapi.models.get_report_reasons_by_category200_response_data_inner_attributes import GetReportReasonsByCategory200ResponseDataInnerAttributes

# TODO update the JSON string below
json = "{}"
# create an instance of GetReportReasonsByCategory200ResponseDataInnerAttributes from a JSON string
get_report_reasons_by_category200_response_data_inner_attributes_instance = GetReportReasonsByCategory200ResponseDataInnerAttributes.from_json(json)
# print the JSON string representation of the object
print(GetReportReasonsByCategory200ResponseDataInnerAttributes.to_json())

# convert the object into a dict
get_report_reasons_by_category200_response_data_inner_attributes_dict = get_report_reasons_by_category200_response_data_inner_attributes_instance.to_dict()
# create an instance of GetReportReasonsByCategory200ResponseDataInnerAttributes from a dict
get_report_reasons_by_category200_response_data_inner_attributes_form_dict = get_report_reasons_by_category200_response_data_inner_attributes.from_dict(get_report_reasons_by_category200_response_data_inner_attributes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


