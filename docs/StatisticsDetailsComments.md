# StatisticsDetailsComments

Comments-related statistics of an entity. If it is `null`, the entity doesn't have a backing comments thread, and therefore has no comments yet. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**thread_id** | **float** | The id of the thread backing the comments for that entity on the MangaDex Forums. | [optional] 
**replies_count** | **float** | The number of replies on the MangaDex Forums thread backing this entity&#39;s comments. This excludes the initial comment that opens the thread, which is created by our systems.  | [optional] 

## Example

```python
from mangadex_openapi.models.statistics_details_comments import StatisticsDetailsComments

# TODO update the JSON string below
json = "{}"
# create an instance of StatisticsDetailsComments from a JSON string
statistics_details_comments_instance = StatisticsDetailsComments.from_json(json)
# print the JSON string representation of the object
print(StatisticsDetailsComments.to_json())

# convert the object into a dict
statistics_details_comments_dict = statistics_details_comments_instance.to_dict()
# create an instance of StatisticsDetailsComments from a dict
statistics_details_comments_form_dict = statistics_details_comments.from_dict(statistics_details_comments_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


