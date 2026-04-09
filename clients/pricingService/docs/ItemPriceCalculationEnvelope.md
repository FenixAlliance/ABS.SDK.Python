# ItemPriceCalculationEnvelope


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_success** | **bool** |  | [optional] [readonly] 
**error_message** | **str** |  | [optional] 
**correlation_id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] [readonly] 
**activity_id** | **str** |  | [optional] [readonly] 
**result** | [**ItemPriceCalculation**](ItemPriceCalculation.md) |  | [optional] 

## Example

```python
from openapi_client.models.item_price_calculation_envelope import ItemPriceCalculationEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of ItemPriceCalculationEnvelope from a JSON string
item_price_calculation_envelope_instance = ItemPriceCalculationEnvelope.from_json(json)
# print the JSON string representation of the object
print(ItemPriceCalculationEnvelope.to_json())

# convert the object into a dict
item_price_calculation_envelope_dict = item_price_calculation_envelope_instance.to_dict()
# create an instance of ItemPriceCalculationEnvelope from a dict
item_price_calculation_envelope_from_dict = ItemPriceCalculationEnvelope.from_dict(item_price_calculation_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


