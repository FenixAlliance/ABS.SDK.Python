# DealUnitDtoEnvelope


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_success** | **bool** |  | [optional] [readonly] 
**error_message** | **str** |  | [optional] 
**correlation_id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] [readonly] 
**activity_id** | **str** |  | [optional] [readonly] 
**result** | [**DealUnitDto**](DealUnitDto.md) |  | [optional] 

## Example

```python
from openapi_client.models.deal_unit_dto_envelope import DealUnitDtoEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of DealUnitDtoEnvelope from a JSON string
deal_unit_dto_envelope_instance = DealUnitDtoEnvelope.from_json(json)
# print the JSON string representation of the object
print(DealUnitDtoEnvelope.to_json())

# convert the object into a dict
deal_unit_dto_envelope_dict = deal_unit_dto_envelope_instance.to_dict()
# create an instance of DealUnitDtoEnvelope from a dict
deal_unit_dto_envelope_from_dict = DealUnitDtoEnvelope.from_dict(deal_unit_dto_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


