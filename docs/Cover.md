# Cover


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**attributes** | [**CoverAttributes**](CoverAttributes.md) |  | [optional] 
**relationships** | [**List[Relationship]**](Relationship.md) |  | [optional] 

## Example

```python
from mangadex_openapi.models.cover import Cover

# TODO update the JSON string below
json = "{}"
# create an instance of Cover from a JSON string
cover_instance = Cover.from_json(json)
# print the JSON string representation of the object
print(Cover.to_json())

# convert the object into a dict
cover_dict = cover_instance.to_dict()
# create an instance of Cover from a dict
cover_form_dict = cover.from_dict(cover_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


