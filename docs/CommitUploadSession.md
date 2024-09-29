# CommitUploadSession


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**chapter_draft** | [**ChapterDraft**](ChapterDraft.md) |  | [optional] 
**page_order** | **List[str]** | ordered list of Upload Session File ids | [optional] 

## Example

```python
from mangadex_openapi.models.commit_upload_session import CommitUploadSession

# TODO update the JSON string below
json = "{}"
# create an instance of CommitUploadSession from a JSON string
commit_upload_session_instance = CommitUploadSession.from_json(json)
# print the JSON string representation of the object
print(CommitUploadSession.to_json())

# convert the object into a dict
commit_upload_session_dict = commit_upload_session_instance.to_dict()
# create an instance of CommitUploadSession from a dict
commit_upload_session_form_dict = commit_upload_session.from_dict(commit_upload_session_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


