# ReportAttributes


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**details** | **str** |  | [optional] 
**object_id** | **str** |  | [optional] 
**status** | **str** |  | [optional] 
**created_at** | **str** |  | [optional] 

## Example

```python
from mangadex_openapi.models.report_attributes import ReportAttributes

# TODO update the JSON string below
json = "{}"
# create an instance of ReportAttributes from a JSON string
report_attributes_instance = ReportAttributes.from_json(json)
# print the JSON string representation of the object
print(ReportAttributes.to_json())

# convert the object into a dict
report_attributes_dict = report_attributes_instance.to_dict()
# create an instance of ReportAttributes from a dict
report_attributes_form_dict = report_attributes.from_dict(report_attributes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


