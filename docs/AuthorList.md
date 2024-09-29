# AuthorList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**result** | **str** |  | [optional] [default to 'ok']
**response** | **str** |  | [optional] [default to 'collection']
**data** | [**List[Author]**](Author.md) |  | [optional] 
**limit** | **int** |  | [optional] 
**offset** | **int** |  | [optional] 
**total** | **int** |  | [optional] 

## Example

```python
from mangadex_openapi.models.author_list import AuthorList

# TODO update the JSON string below
json = "{}"
# create an instance of AuthorList from a JSON string
author_list_instance = AuthorList.from_json(json)
# print the JSON string representation of the object
print(AuthorList.to_json())

# convert the object into a dict
author_list_dict = author_list_instance.to_dict()
# create an instance of AuthorList from a dict
author_list_form_dict = author_list.from_dict(author_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


