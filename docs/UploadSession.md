# UploadSession


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**attributes** | [**UploadSessionAttributes**](UploadSessionAttributes.md) |  | [optional] 

## Example

```python
from mangadex_openapi.models.upload_session import UploadSession

# TODO update the JSON string below
json = "{}"
# create an instance of UploadSession from a JSON string
upload_session_instance = UploadSession.from_json(json)
# print the JSON string representation of the object
print(UploadSession.to_json())

# convert the object into a dict
upload_session_dict = upload_session_instance.to_dict()
# create an instance of UploadSession from a dict
upload_session_form_dict = upload_session.from_dict(upload_session_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


