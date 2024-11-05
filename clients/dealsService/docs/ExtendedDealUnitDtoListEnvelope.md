# ExtendedDealUnitDtoListEnvelope


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_success** | **bool** |  | [optional] [readonly] 
**error_message** | **str** |  | [optional] 
**correlation_id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] [readonly] 
**activity_id** | **str** |  | [optional] [readonly] 
**result** | [**List[ExtendedDealUnitDto]**](ExtendedDealUnitDto.md) |  | [optional] 

## Example

```python
from openapi_client.models.extended_deal_unit_dto_list_envelope import ExtendedDealUnitDtoListEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of ExtendedDealUnitDtoListEnvelope from a JSON string
extended_deal_unit_dto_list_envelope_instance = ExtendedDealUnitDtoListEnvelope.from_json(json)
# print the JSON string representation of the object
print(ExtendedDealUnitDtoListEnvelope.to_json())

# convert the object into a dict
extended_deal_unit_dto_list_envelope_dict = extended_deal_unit_dto_list_envelope_instance.to_dict()
# create an instance of ExtendedDealUnitDtoListEnvelope from a dict
extended_deal_unit_dto_list_envelope_from_dict = ExtendedDealUnitDtoListEnvelope.from_dict(extended_deal_unit_dto_list_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


