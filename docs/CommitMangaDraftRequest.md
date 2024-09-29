# CommitMangaDraftRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**version** | **int** |  | [optional] 

## Example

```python
from mangadex_openapi.models.commit_manga_draft_request import CommitMangaDraftRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CommitMangaDraftRequest from a JSON string
commit_manga_draft_request_instance = CommitMangaDraftRequest.from_json(json)
# print the JSON string representation of the object
print(CommitMangaDraftRequest.to_json())

# convert the object into a dict
commit_manga_draft_request_dict = commit_manga_draft_request_instance.to_dict()
# create an instance of CommitMangaDraftRequest from a dict
commit_manga_draft_request_form_dict = commit_manga_draft_request.from_dict(commit_manga_draft_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


