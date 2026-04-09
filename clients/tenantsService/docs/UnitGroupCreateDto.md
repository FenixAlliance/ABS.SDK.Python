# UnitGroupCreateDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] 
**name** | **str** |  | 
**description** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.unit_group_create_dto import UnitGroupCreateDto

# TODO update the JSON string below
json = "{}"
# create an instance of UnitGroupCreateDto from a JSON string
unit_group_create_dto_instance = UnitGroupCreateDto.from_json(json)
# print the JSON string representation of the object
print(UnitGroupCreateDto.to_json())

# convert the object into a dict
unit_group_create_dto_dict = unit_group_create_dto_instance.to_dict()
# create an instance of UnitGroupCreateDto from a dict
unit_group_create_dto_from_dict = UnitGroupCreateDto.from_dict(unit_group_create_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


