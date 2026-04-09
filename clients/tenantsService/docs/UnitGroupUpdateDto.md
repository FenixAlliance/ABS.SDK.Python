# UnitGroupUpdateDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**description** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.unit_group_update_dto import UnitGroupUpdateDto

# TODO update the JSON string below
json = "{}"
# create an instance of UnitGroupUpdateDto from a JSON string
unit_group_update_dto_instance = UnitGroupUpdateDto.from_json(json)
# print the JSON string representation of the object
print(UnitGroupUpdateDto.to_json())

# convert the object into a dict
unit_group_update_dto_dict = unit_group_update_dto_instance.to_dict()
# create an instance of UnitGroupUpdateDto from a dict
unit_group_update_dto_from_dict = UnitGroupUpdateDto.from_dict(unit_group_update_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


