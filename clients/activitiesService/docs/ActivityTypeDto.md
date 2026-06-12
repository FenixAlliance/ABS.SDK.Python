# ActivityTypeDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] 
**name** | **str** |  | [optional] 
**tenant_id** | **str** |  | [optional] 
**enrollment_id** | **str** |  | [optional] 
**activity_records_count** | **int** |  | [optional] 

## Example

```python
from openapi_client.models.activity_type_dto import ActivityTypeDto

# TODO update the JSON string below
json = "{}"
# create an instance of ActivityTypeDto from a JSON string
activity_type_dto_instance = ActivityTypeDto.from_json(json)
# print the JSON string representation of the object
print(ActivityTypeDto.to_json())

# convert the object into a dict
activity_type_dto_dict = activity_type_dto_instance.to_dict()
# create an instance of ActivityTypeDto from a dict
activity_type_dto_from_dict = ActivityTypeDto.from_dict(activity_type_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


