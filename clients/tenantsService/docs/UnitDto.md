# UnitDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] 
**name** | **str** |  | [optional] 
**unit_group_id** | **str** |  | [optional] 
**base_unit_amount** | **float** |  | [optional] 
**base_unit_id** | **str** |  | [optional] 
**tenant_id** | **str** |  | [optional] 
**enrollment_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.unit_dto import UnitDto

# TODO update the JSON string below
json = "{}"
# create an instance of UnitDto from a JSON string
unit_dto_instance = UnitDto.from_json(json)
# print the JSON string representation of the object
print(UnitDto.to_json())

# convert the object into a dict
unit_dto_dict = unit_dto_instance.to_dict()
# create an instance of UnitDto from a dict
unit_dto_from_dict = UnitDto.from_dict(unit_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


