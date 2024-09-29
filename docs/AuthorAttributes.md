# AuthorAttributes


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**image_url** | **str** |  | [optional] 
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
**namicomi** | **str** |  | [optional] 
**website** | **str** |  | [optional] 
**version** | **int** |  | [optional] 
**created_at** | **str** |  | [optional] 
**updated_at** | **str** |  | [optional] 

## Example

```python
from mangadex_openapi.models.author_attributes import AuthorAttributes

# TODO update the JSON string below
json = "{}"
# create an instance of AuthorAttributes from a JSON string
author_attributes_instance = AuthorAttributes.from_json(json)
# print the JSON string representation of the object
print(AuthorAttributes.to_json())

# convert the object into a dict
author_attributes_dict = author_attributes_instance.to_dict()
# create an instance of AuthorAttributes from a dict
author_attributes_form_dict = author_attributes.from_dict(author_attributes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


