# UnitUpdateDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**base_unit_amount** | **float** |  | [optional] 
**base_unit_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.unit_update_dto import UnitUpdateDto

# TODO update the JSON string below
json = "{}"
# create an instance of UnitUpdateDto from a JSON string
unit_update_dto_instance = UnitUpdateDto.from_json(json)
# print the JSON string representation of the object
print(UnitUpdateDto.to_json())

# convert the object into a dict
unit_update_dto_dict = unit_update_dto_instance.to_dict()
# create an instance of UnitUpdateDto from a dict
unit_update_dto_from_dict = UnitUpdateDto.from_dict(unit_update_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


