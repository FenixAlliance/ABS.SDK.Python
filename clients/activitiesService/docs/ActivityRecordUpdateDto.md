# ActivityRecordUpdateDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**completed** | **bool** |  | [optional] 
**due_date** | **datetime** |  | [optional] 
**activity_type_id** | **str** |  | [optional] 
**parent_activity_id** | **str** |  | [optional] 
**in_charge_enrollment_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.activity_record_update_dto import ActivityRecordUpdateDto

# TODO update the JSON string below
json = "{}"
# create an instance of ActivityRecordUpdateDto from a JSON string
activity_record_update_dto_instance = ActivityRecordUpdateDto.from_json(json)
# print the JSON string representation of the object
print(ActivityRecordUpdateDto.to_json())

# convert the object into a dict
activity_record_update_dto_dict = activity_record_update_dto_instance.to_dict()
# create an instance of ActivityRecordUpdateDto from a dict
activity_record_update_dto_from_dict = ActivityRecordUpdateDto.from_dict(activity_record_update_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


