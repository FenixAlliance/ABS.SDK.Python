# ActivityTypeCreateDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.activity_type_create_dto import ActivityTypeCreateDto

# TODO update the JSON string below
json = "{}"
# create an instance of ActivityTypeCreateDto from a JSON string
activity_type_create_dto_instance = ActivityTypeCreateDto.from_json(json)
# print the JSON string representation of the object
print(ActivityTypeCreateDto.to_json())

# convert the object into a dict
activity_type_create_dto_dict = activity_type_create_dto_instance.to_dict()
# create an instance of ActivityTypeCreateDto from a dict
activity_type_create_dto_from_dict = ActivityTypeCreateDto.from_dict(activity_type_create_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


