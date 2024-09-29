# AuthorEdit


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**biography** | **Dict[str, str]** |  | [optional] 
**twitter** | **str** |  | [optional] 
**pixiv** | **str** |  | [optional] 
**melon_book** | **str** |  | [optional] 
**fan_box** | **str** |  | [optional] 
**booth** | **str** |  | [optional] 
**nico_video** | **str** |  | [optional] 
**skeb** | **str** |  | [optional] 
**fantia** | **str** |  | [optional] 
**tumblr** | **str** |  | [optional] 
**youtube** | **str** |  | [optional] 
**weibo** | **str** |  | [optional] 
**naver** | **str** |  | [optional] 
**website** | **str** |  | [optional] 
**version** | **int** |  | 

## Example

```python
from mangadex_openapi.models.author_edit import AuthorEdit

# TODO update the JSON string below
json = "{}"
# create an instance of AuthorEdit from a JSON string
author_edit_instance = AuthorEdit.from_json(json)
# print the JSON string representation of the object
print(AuthorEdit.to_json())

# convert the object into a dict
author_edit_dict = author_edit_instance.to_dict()
# create an instance of AuthorEdit from a dict
author_edit_form_dict = author_edit.from_dict(author_edit_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


