# ScanlationGroupResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**result** | **str** |  | [optional] 
**response** | **str** |  | [optional] [default to 'entity']
**data** | [**ScanlationGroup**](ScanlationGroup.md) |  | [optional] 

## Example

```python
from mangadex_openapi.models.scanlation_group_response import ScanlationGroupResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ScanlationGroupResponse from a JSON string
scanlation_group_response_instance = ScanlationGroupResponse.from_json(json)
# print the JSON string representation of the object
print(ScanlationGroupResponse.to_json())

# convert the object into a dict
scanlation_group_response_dict = scanlation_group_response_instance.to_dict()
# create an instance of ScanlationGroupResponse from a dict
scanlation_group_response_form_dict = scanlation_group_response.from_dict(scanlation_group_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


