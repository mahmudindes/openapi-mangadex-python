# BeginUploadSession


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**groups** | **List[str]** |  | 
**manga** | **str** |  | 

## Example

```python
from mangadex_openapi.models.begin_upload_session import BeginUploadSession

# TODO update the JSON string below
json = "{}"
# create an instance of BeginUploadSession from a JSON string
begin_upload_session_instance = BeginUploadSession.from_json(json)
# print the JSON string representation of the object
print(BeginUploadSession.to_json())

# convert the object into a dict
begin_upload_session_dict = begin_upload_session_instance.to_dict()
# create an instance of BeginUploadSession from a dict
begin_upload_session_form_dict = begin_upload_session.from_dict(begin_upload_session_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


