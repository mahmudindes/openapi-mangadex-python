# PutUploadSessionFile200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**result** | **str** |  | [optional] 
**errors** | [**List[Error]**](Error.md) |  | [optional] 
**data** | [**List[UploadSessionFile]**](UploadSessionFile.md) |  | [optional] 

## Example

```python
from mangadex_openapi.models.put_upload_session_file200_response import PutUploadSessionFile200Response

# TODO update the JSON string below
json = "{}"
# create an instance of PutUploadSessionFile200Response from a JSON string
put_upload_session_file200_response_instance = PutUploadSessionFile200Response.from_json(json)
# print the JSON string representation of the object
print(PutUploadSessionFile200Response.to_json())

# convert the object into a dict
put_upload_session_file200_response_dict = put_upload_session_file200_response_instance.to_dict()
# create an instance of PutUploadSessionFile200Response from a dict
put_upload_session_file200_response_form_dict = put_upload_session_file200_response.from_dict(put_upload_session_file200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


