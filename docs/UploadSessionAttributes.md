# UploadSessionAttributes


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_committed** | **bool** |  | [optional] 
**is_processed** | **bool** |  | [optional] 
**is_deleted** | **bool** |  | [optional] 
**version** | **int** |  | [optional] 
**created_at** | **str** |  | [optional] 
**updated_at** | **str** |  | [optional] 

## Example

```python
from mangadex_openapi.models.upload_session_attributes import UploadSessionAttributes

# TODO update the JSON string below
json = "{}"
# create an instance of UploadSessionAttributes from a JSON string
upload_session_attributes_instance = UploadSessionAttributes.from_json(json)
# print the JSON string representation of the object
print(UploadSessionAttributes.to_json())

# convert the object into a dict
upload_session_attributes_dict = upload_session_attributes_instance.to_dict()
# create an instance of UploadSessionAttributes from a dict
upload_session_attributes_form_dict = upload_session_attributes.from_dict(upload_session_attributes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


