# UnitDtoEnvelope


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_success** | **bool** |  | [optional] [readonly] 
**error_message** | **str** |  | [optional] 
**correlation_id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] [readonly] 
**activity_id** | **str** |  | [optional] [readonly] 
**result** | [**UnitDto**](UnitDto.md) |  | [optional] 

## Example

```python
from openapi_client.models.unit_dto_envelope import UnitDtoEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of UnitDtoEnvelope from a JSON string
unit_dto_envelope_instance = UnitDtoEnvelope.from_json(json)
# print the JSON string representation of the object
print(UnitDtoEnvelope.to_json())

# convert the object into a dict
unit_dto_envelope_dict = unit_dto_envelope_instance.to_dict()
# create an instance of UnitDtoEnvelope from a dict
unit_dto_envelope_from_dict = UnitDtoEnvelope.from_dict(unit_dto_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


