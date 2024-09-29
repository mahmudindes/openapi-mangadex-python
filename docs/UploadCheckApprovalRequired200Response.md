# UploadCheckApprovalRequired200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**result** | **str** |  | [optional] 
**requires_approval** | **bool** |  | [optional] 

## Example

```python
from mangadex_openapi.models.upload_check_approval_required200_response import UploadCheckApprovalRequired200Response

# TODO update the JSON string below
json = "{}"
# create an instance of UploadCheckApprovalRequired200Response from a JSON string
upload_check_approval_required200_response_instance = UploadCheckApprovalRequired200Response.from_json(json)
# print the JSON string representation of the object
print(UploadCheckApprovalRequired200Response.to_json())

# convert the object into a dict
upload_check_approval_required200_response_dict = upload_check_approval_required200_response_instance.to_dict()
# create an instance of UploadCheckApprovalRequired200Response from a dict
upload_check_approval_required200_response_form_dict = upload_check_approval_required200_response.from_dict(upload_check_approval_required200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


