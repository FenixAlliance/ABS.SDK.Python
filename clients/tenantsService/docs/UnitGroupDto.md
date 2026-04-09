# UnitGroupDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] 
**name** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**tenant_id** | **str** |  | [optional] 
**enrollment_id** | **str** |  | [optional] 
**unit_count** | **int** |  | [optional] 

## Example

```python
from openapi_client.models.unit_group_dto import UnitGroupDto

# TODO update the JSON string below
json = "{}"
# create an instance of UnitGroupDto from a JSON string
unit_group_dto_instance = UnitGroupDto.from_json(json)
# print the JSON string representation of the object
print(UnitGroupDto.to_json())

# convert the object into a dict
unit_group_dto_dict = unit_group_dto_instance.to_dict()
# create an instance of UnitGroupDto from a dict
unit_group_dto_from_dict = UnitGroupDto.from_dict(unit_group_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


