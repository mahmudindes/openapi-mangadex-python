# GetSearchMangaOrderParameter


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** |  | [optional] 
**year** | **str** |  | [optional] 
**created_at** | **str** |  | [optional] 
**updated_at** | **str** |  | [optional] 
**latest_uploaded_chapter** | **str** |  | [optional] 
**followed_count** | **str** |  | [optional] 
**relevance** | **str** |  | [optional] 
**rating** | **str** |  | [optional] 

## Example

```python
from mangadex_openapi.models.get_search_manga_order_parameter import GetSearchMangaOrderParameter

# TODO update the JSON string below
json = "{}"
# create an instance of GetSearchMangaOrderParameter from a JSON string
get_search_manga_order_parameter_instance = GetSearchMangaOrderParameter.from_json(json)
# print the JSON string representation of the object
print(GetSearchMangaOrderParameter.to_json())

# convert the object into a dict
get_search_manga_order_parameter_dict = get_search_manga_order_parameter_instance.to_dict()
# create an instance of GetSearchMangaOrderParameter from a dict
get_search_manga_order_parameter_form_dict = get_search_manga_order_parameter.from_dict(get_search_manga_order_parameter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


