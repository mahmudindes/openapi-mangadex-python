# UploadSessionFile


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**attributes** | [**UploadSessionFileAttributes**](UploadSessionFileAttributes.md) |  | [optional] 

## Example

```python
from mangadex_openapi.models.upload_session_file import UploadSessionFile

# TODO update the JSON string below
json = "{}"
# create an instance of UploadSessionFile from a JSON string
upload_session_file_instance = UploadSessionFile.from_json(json)
# print the JSON string representation of the object
print(UploadSessionFile.to_json())

# convert the object into a dict
upload_session_file_dict = upload_session_file_instance.to_dict()
# create an instance of UploadSessionFile from a dict
upload_session_file_form_dict = upload_session_file.from_dict(upload_session_file_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


