# TaxCalculationOptions


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enable_taxes** | **bool** |  | [optional] 
**round_taxes_at_subtotal_level** | **bool** |  | [optional] 
**display_price_suffix** | **str** |  | [optional] 
**display_price_prefix** | **str** |  | [optional] 
**standard_rates** | **List[str]** |  | [optional] 
**zero_rate_rates** | **List[str]** |  | [optional] 
**reduced_rate_rates** | **List[str]** |  | [optional] 
**additional_tax_classes** | **Dict[str, Optional[List[str]]]** |  | [optional] 

## Example

```python
from openapi_client.models.tax_calculation_options import TaxCalculationOptions

# TODO update the JSON string below
json = "{}"
# create an instance of TaxCalculationOptions from a JSON string
tax_calculation_options_instance = TaxCalculationOptions.from_json(json)
# print the JSON string representation of the object
print(TaxCalculationOptions.to_json())

# convert the object into a dict
tax_calculation_options_dict = tax_calculation_options_instance.to_dict()
# create an instance of TaxCalculationOptions from a dict
tax_calculation_options_from_dict = TaxCalculationOptions.from_dict(tax_calculation_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


