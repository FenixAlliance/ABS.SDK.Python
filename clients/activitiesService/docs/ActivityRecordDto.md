# ActivityRecordDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] 
**type** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**completed** | **bool** |  | [optional] 
**due_date** | **datetime** |  | [optional] 
**activity_feed_id** | **str** |  | [optional] 
**activity_type_id** | **str** |  | [optional] 
**tenant_id** | **str** |  | [optional] 
**enrollment_id** | **str** |  | [optional] 
**social_profile_id** | **str** |  | [optional] 
**parent_activity_id** | **str** |  | [optional] 
**in_charge_enrollment_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.activity_record_dto import ActivityRecordDto

# TODO update the JSON string below
json = "{}"
# create an instance of ActivityRecordDto from a JSON string
activity_record_dto_instance = ActivityRecordDto.from_json(json)
# print the JSON string representation of the object
print(ActivityRecordDto.to_json())

# convert the object into a dict
activity_record_dto_dict = activity_record_dto_instance.to_dict()
# create an instance of ActivityRecordDto from a dict
activity_record_dto_from_dict = ActivityRecordDto.from_dict(activity_record_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


