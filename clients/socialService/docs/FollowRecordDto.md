# FollowRecordDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**follower_id** | **str** |  | [optional] 
**followed_id** | **str** |  | [optional] 
**alerts** | **bool** |  | [optional] 

## Example

```python
from openapi_client.models.follow_record_dto import FollowRecordDto

# TODO update the JSON string below
json = "{}"
# create an instance of FollowRecordDto from a JSON string
follow_record_dto_instance = FollowRecordDto.from_json(json)
# print the JSON string representation of the object
print(FollowRecordDto.to_json())

# convert the object into a dict
follow_record_dto_dict = follow_record_dto_instance.to_dict()
# create an instance of FollowRecordDto from a dict
follow_record_dto_from_dict = FollowRecordDto.from_dict(follow_record_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


