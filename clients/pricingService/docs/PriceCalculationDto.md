# PriceCalculationDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] 
**item_id** | **str** |  | [optional] 
**unit_id** | **str** |  | [optional] 
**unit_group_id** | **str** |  | [optional] 
**price_id** | **str** |  | [optional] 
**price_list_id** | **str** |  | [optional] 
**discount_id** | **str** |  | [optional] 
**discount_list_id** | **str** |  | [optional] 
**tenant_id** | **str** |  | [optional] 
**enrollment_id** | **str** |  | [optional] 
**rounding_policy_id** | **str** |  | [optional] 
**effective_discount_percent** | **float** |  | [optional] 
**currency_id** | **str** |  | [optional] 
**total_base_amount** | [**Money**](Money.md) |  | [optional] 
**total_discounts_amount** | [**Money**](Money.md) |  | [optional] 
**total_surcharges_amount** | [**Money**](Money.md) |  | [optional] 
**total_shipping_amount** | [**Money**](Money.md) |  | [optional] 
**total_shipping_tax_amount** | [**Money**](Money.md) |  | [optional] 
**total_tax_amount** | [**Money**](Money.md) |  | [optional] 
**total_amount** | [**Money**](Money.md) |  | [optional] 

## Example

```python
from openapi_client.models.price_calculation_dto import PriceCalculationDto

# TODO update the JSON string below
json = "{}"
# create an instance of PriceCalculationDto from a JSON string
price_calculation_dto_instance = PriceCalculationDto.from_json(json)
# print the JSON string representation of the object
print(PriceCalculationDto.to_json())

# convert the object into a dict
price_calculation_dto_dict = price_calculation_dto_instance.to_dict()
# create an instance of PriceCalculationDto from a dict
price_calculation_dto_from_dict = PriceCalculationDto.from_dict(price_calculation_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


