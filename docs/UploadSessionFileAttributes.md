# UploadSessionFileAttributes


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**original_file_name** | **str** |  | [optional] 
**file_hash** | **str** |  | [optional] 
**file_size** | **float** |  | [optional] 
**mime_type** | **str** |  | [optional] 
**source** | **str** |  | [optional] 
**version** | **int** |  | [optional] 

## Example

```python
from mangadex_openapi.models.upload_session_file_attributes import UploadSessionFileAttributes

# TODO update the JSON string below
json = "{}"
# create an instance of UploadSessionFileAttributes from a JSON string
upload_session_file_attributes_instance = UploadSessionFileAttributes.from_json(json)
# print the JSON string representation of the object
print(UploadSessionFileAttributes.to_json())

# convert the object into a dict
upload_session_file_attributes_dict = upload_session_file_attributes_instance.to_dict()
# create an instance of UploadSessionFileAttributes from a dict
upload_session_file_attributes_form_dict = upload_session_file_attributes.from_dict(upload_session_file_attributes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


