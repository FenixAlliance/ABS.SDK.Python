# ActivityRecordCreateDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] 
**type** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**due_date** | **datetime** |  | [optional] 
**activity_feed_id** | **str** |  | [optional] 
**activity_type_id** | **str** |  | [optional] 
**parent_activity_id** | **str** |  | [optional] 
**in_charge_enrollment_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.activity_record_create_dto import ActivityRecordCreateDto

# TODO update the JSON string below
json = "{}"
# create an instance of ActivityRecordCreateDto from a JSON string
activity_record_create_dto_instance = ActivityRecordCreateDto.from_json(json)
# print the JSON string representation of the object
print(ActivityRecordCreateDto.to_json())

# convert the object into a dict
activity_record_create_dto_dict = activity_record_create_dto_instance.to_dict()
# create an instance of ActivityRecordCreateDto from a dict
activity_record_create_dto_from_dict = ActivityRecordCreateDto.from_dict(activity_record_create_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


