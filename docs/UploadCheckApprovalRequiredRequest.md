# UploadCheckApprovalRequiredRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**manga** | **str** |  | [optional] 
**locale** | **str** |  | [optional] 

## Example

```python
from mangadex_openapi.models.upload_check_approval_required_request import UploadCheckApprovalRequiredRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UploadCheckApprovalRequiredRequest from a JSON string
upload_check_approval_required_request_instance = UploadCheckApprovalRequiredRequest.from_json(json)
# print the JSON string representation of the object
print(UploadCheckApprovalRequiredRequest.to_json())

# convert the object into a dict
upload_check_approval_required_request_dict = upload_check_approval_required_request_instance.to_dict()
# create an instance of UploadCheckApprovalRequiredRequest from a dict
upload_check_approval_required_request_form_dict = upload_check_approval_required_request.from_dict(upload_check_approval_required_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


