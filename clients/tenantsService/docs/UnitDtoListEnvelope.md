# UnitDtoListEnvelope


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_success** | **bool** |  | [optional] [readonly] 
**error_message** | **str** |  | [optional] 
**correlation_id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] [readonly] 
**activity_id** | **str** |  | [optional] [readonly] 
**result** | [**List[UnitDto]**](UnitDto.md) |  | [optional] 

## Example

```python
from openapi_client.models.unit_dto_list_envelope import UnitDtoListEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of UnitDtoListEnvelope from a JSON string
unit_dto_list_envelope_instance = UnitDtoListEnvelope.from_json(json)
# print the JSON string representation of the object
print(UnitDtoListEnvelope.to_json())

# convert the object into a dict
unit_dto_list_envelope_dict = unit_dto_list_envelope_instance.to_dict()
# create an instance of UnitDtoListEnvelope from a dict
unit_dto_list_envelope_from_dict = UnitDtoListEnvelope.from_dict(unit_dto_list_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


