# UnitGroupDtoListEnvelope


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_success** | **bool** |  | [optional] [readonly] 
**error_message** | **str** |  | [optional] 
**correlation_id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] [readonly] 
**activity_id** | **str** |  | [optional] [readonly] 
**result** | [**List[UnitGroupDto]**](UnitGroupDto.md) |  | [optional] 

## Example

```python
from openapi_client.models.unit_group_dto_list_envelope import UnitGroupDtoListEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of UnitGroupDtoListEnvelope from a JSON string
unit_group_dto_list_envelope_instance = UnitGroupDtoListEnvelope.from_json(json)
# print the JSON string representation of the object
print(UnitGroupDtoListEnvelope.to_json())

# convert the object into a dict
unit_group_dto_list_envelope_dict = unit_group_dto_list_envelope_instance.to_dict()
# create an instance of UnitGroupDtoListEnvelope from a dict
unit_group_dto_list_envelope_from_dict = UnitGroupDtoListEnvelope.from_dict(unit_group_dto_list_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


