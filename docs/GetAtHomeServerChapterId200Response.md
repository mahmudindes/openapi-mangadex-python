# GetAtHomeServerChapterId200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**result** | **str** |  | [optional] [default to 'ok']
**base_url** | **str** | The base URL to construct final image URLs from. The URL returned is valid for the requested chapter only, and for a duration of 15 minutes from the time of the response. | [optional] 
**chapter** | [**GetAtHomeServerChapterId200ResponseChapter**](GetAtHomeServerChapterId200ResponseChapter.md) |  | [optional] 

## Example

```python
from mangadex_openapi.models.get_at_home_server_chapter_id200_response import GetAtHomeServerChapterId200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetAtHomeServerChapterId200Response from a JSON string
get_at_home_server_chapter_id200_response_instance = GetAtHomeServerChapterId200Response.from_json(json)
# print the JSON string representation of the object
print(GetAtHomeServerChapterId200Response.to_json())

# convert the object into a dict
get_at_home_server_chapter_id200_response_dict = get_at_home_server_chapter_id200_response_instance.to_dict()
# create an instance of GetAtHomeServerChapterId200Response from a dict
get_at_home_server_chapter_id200_response_form_dict = get_at_home_server_chapter_id200_response.from_dict(get_at_home_server_chapter_id200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


