# PriceCalculationDtoEnvelope


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_success** | **bool** |  | [optional] [readonly] 
**error_message** | **str** |  | [optional] 
**correlation_id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] [readonly] 
**activity_id** | **str** |  | [optional] [readonly] 
**result** | [**PriceCalculationDto**](PriceCalculationDto.md) |  | [optional] 

## Example

```python
from openapi_client.models.price_calculation_dto_envelope import PriceCalculationDtoEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of PriceCalculationDtoEnvelope from a JSON string
price_calculation_dto_envelope_instance = PriceCalculationDtoEnvelope.from_json(json)
# print the JSON string representation of the object
print(PriceCalculationDtoEnvelope.to_json())

# convert the object into a dict
price_calculation_dto_envelope_dict = price_calculation_dto_envelope_instance.to_dict()
# create an instance of PriceCalculationDtoEnvelope from a dict
price_calculation_dto_envelope_from_dict = PriceCalculationDtoEnvelope.from_dict(price_calculation_dto_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


