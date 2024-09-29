# PostRatingMangaIdRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rating** | **int** |  | [optional] 

## Example

```python
from mangadex_openapi.models.post_rating_manga_id_request import PostRatingMangaIdRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PostRatingMangaIdRequest from a JSON string
post_rating_manga_id_request_instance = PostRatingMangaIdRequest.from_json(json)
# print the JSON string representation of the object
print(PostRatingMangaIdRequest.to_json())

# convert the object into a dict
post_rating_manga_id_request_dict = post_rating_manga_id_request_instance.to_dict()
# create an instance of PostRatingMangaIdRequest from a dict
post_rating_manga_id_request_form_dict = post_rating_manga_id_request.from_dict(post_rating_manga_id_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


