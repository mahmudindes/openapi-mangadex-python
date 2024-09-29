# PostSettingsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**settings** | **object** | A JSON object that can be validated against the lastest available template | [optional] 
**updated_at** | **datetime** | Format: 2022-03-14T13:19:37 | [optional] 

## Example

```python
from mangadex_openapi.models.post_settings_request import PostSettingsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PostSettingsRequest from a JSON string
post_settings_request_instance = PostSettingsRequest.from_json(json)
# print the JSON string representation of the object
print(PostSettingsRequest.to_json())

# convert the object into a dict
post_settings_request_dict = post_settings_request_instance.to_dict()
# create an instance of PostSettingsRequest from a dict
post_settings_request_form_dict = post_settings_request.from_dict(post_settings_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


