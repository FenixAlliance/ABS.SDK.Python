# ExtendedDealUnitDtoEnvelope


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_success** | **bool** |  | [optional] [readonly] 
**error_message** | **str** |  | [optional] 
**correlation_id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] [readonly] 
**activity_id** | **str** |  | [optional] [readonly] 
**result** | [**ExtendedDealUnitDto**](ExtendedDealUnitDto.md) |  | [optional] 

## Example

```python
from openapi_client.models.extended_deal_unit_dto_envelope import ExtendedDealUnitDtoEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of ExtendedDealUnitDtoEnvelope from a JSON string
extended_deal_unit_dto_envelope_instance = ExtendedDealUnitDtoEnvelope.from_json(json)
# print the JSON string representation of the object
print(ExtendedDealUnitDtoEnvelope.to_json())

# convert the object into a dict
extended_deal_unit_dto_envelope_dict = extended_deal_unit_dto_envelope_instance.to_dict()
# create an instance of ExtendedDealUnitDtoEnvelope from a dict
extended_deal_unit_dto_envelope_from_dict = ExtendedDealUnitDtoEnvelope.from_dict(extended_deal_unit_dto_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


