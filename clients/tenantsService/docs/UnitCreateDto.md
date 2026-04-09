# UnitCreateDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] 
**name** | **str** |  | 
**base_unit_amount** | **float** |  | [optional] 
**base_unit_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.unit_create_dto import UnitCreateDto

# TODO update the JSON string below
json = "{}"
# create an instance of UnitCreateDto from a JSON string
unit_create_dto_instance = UnitCreateDto.from_json(json)
# print the JSON string representation of the object
print(UnitCreateDto.to_json())

# convert the object into a dict
unit_create_dto_dict = unit_create_dto_instance.to_dict()
# create an instance of UnitCreateDto from a dict
unit_create_dto_from_dict = UnitCreateDto.from_dict(unit_create_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


