# AuthorCreate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
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

## Example

```python
from mangadex_openapi.models.author_create import AuthorCreate

# TODO update the JSON string below
json = "{}"
# create an instance of AuthorCreate from a JSON string
author_create_instance = AuthorCreate.from_json(json)
# print the JSON string representation of the object
print(AuthorCreate.to_json())

# convert the object into a dict
author_create_dict = author_create_instance.to_dict()
# create an instance of AuthorCreate from a dict
author_create_form_dict = author_create.from_dict(author_create_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


