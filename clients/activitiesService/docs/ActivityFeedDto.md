# ActivityFeedDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] 
**activities_count** | **int** |  | [optional] 
**tenant_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.activity_feed_dto import ActivityFeedDto

# TODO update the JSON string below
json = "{}"
# create an instance of ActivityFeedDto from a JSON string
activity_feed_dto_instance = ActivityFeedDto.from_json(json)
# print the JSON string representation of the object
print(ActivityFeedDto.to_json())

# convert the object into a dict
activity_feed_dto_dict = activity_feed_dto_instance.to_dict()
# create an instance of ActivityFeedDto from a dict
activity_feed_dto_from_dict = ActivityFeedDto.from_dict(activity_feed_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


