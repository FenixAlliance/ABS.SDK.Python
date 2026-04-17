# TaxRateCreateDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] 
**name** | **str** |  | [optional] 
**rate** | **float** |  | [optional] 
**value** | **float** |  | [optional] 
**um** | **str** |  | [optional] 
**unit_id** | **str** |  | [optional] 
**unit_group_id** | **str** |  | [optional] 
**priority** | **int** |  | [optional] 
**compound** | **bool** |  | [optional] 
**shipping** | **bool** |  | [optional] 
**withholding** | **bool** |  | [optional] 
**single_transaction_threshold** | **float** |  | [optional] 
**cumulative_transaction_threshold** | **float** |  | [optional] 
**fiscal_authority_id** | **str** |  | [optional] 
**fiscal_year_id** | **str** |  | [optional] 
**country_id** | **str** |  | [optional] 
**tax_class_id** | **str** |  | [optional] 
**currency_id** | **str** |  | [optional] 
**tax_policy_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.tax_rate_create_dto import TaxRateCreateDto

# TODO update the JSON string below
json = "{}"
# create an instance of TaxRateCreateDto from a JSON string
tax_rate_create_dto_instance = TaxRateCreateDto.from_json(json)
# print the JSON string representation of the object
print(TaxRateCreateDto.to_json())

# convert the object into a dict
tax_rate_create_dto_dict = tax_rate_create_dto_instance.to_dict()
# create an instance of TaxRateCreateDto from a dict
tax_rate_create_dto_from_dict = TaxRateCreateDto.from_dict(tax_rate_create_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


