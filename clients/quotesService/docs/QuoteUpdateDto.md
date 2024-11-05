# QuoteUpdateDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**closed** | **bool** |  | [optional] 
**title** | **str** |  | [optional] 
**user_id** | **str** |  | [optional] 
**tenant_id** | **str** |  | [optional] 
**forex_rate** | **float** |  | [optional] 
**currency_id** | **str** |  | [optional] 
**price_list_id** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**enrollment_id** | **str** |  | [optional] 
**individual_id** | **str** |  | [optional] 
**payment_term_id** | **str** |  | [optional] 
**organization_id** | **str** |  | [optional] 
**receiver_tenant_id** | **str** |  | [optional] 
**first_name** | **str** |  | [optional] 
**last_name** | **str** |  | [optional] 
**company_name** | **str** |  | [optional] 
**billing_email** | **str** |  | [optional] 
**address_line1** | **str** |  | [optional] 
**address_line2** | **str** |  | [optional] 
**postal_code** | **str** |  | [optional] 
**country_id** | **str** |  | [optional] 
**state_id** | **str** |  | [optional] 
**city_id** | **str** |  | [optional] 
**billing_location_id** | **str** |  | [optional] 
**shipping_location_id** | **str** |  | [optional] 
**shipping_method_id** | **str** |  | [optional] 
**cart_id** | **str** |  | [optional] 
**total** | **float** |  | [optional] 
**total_taxes** | **float** |  | [optional] 
**quote_status** | **int** |  | [optional] 
**freight_terms** | **int** |  | [optional] 
**cost_calculation_method** | **int** |  | [optional] 
**effective_to** | **datetime** |  | [optional] 
**effective_from** | **datetime** |  | [optional] 
**custom_tax_amount** | **float** |  | [optional] 
**custom_total_amount** | **float** |  | [optional] 
**custom_detail_amount** | **float** |  | [optional] 
**custom_profit_amount** | **float** |  | [optional] 
**custom_discounts_amount** | **float** |  | [optional] 
**custom_surcharges_amount** | **float** |  | [optional] 
**custom_shipping_cost_amount** | **float** |  | [optional] 
**custom_shipping_tax_amount** | **float** |  | [optional] 
**custom_withholding_tax_amount** | **float** |  | [optional] 

## Example

```python
from openapi_client.models.quote_update_dto import QuoteUpdateDto

# TODO update the JSON string below
json = "{}"
# create an instance of QuoteUpdateDto from a JSON string
quote_update_dto_instance = QuoteUpdateDto.from_json(json)
# print the JSON string representation of the object
print(QuoteUpdateDto.to_json())

# convert the object into a dict
quote_update_dto_dict = quote_update_dto_instance.to_dict()
# create an instance of QuoteUpdateDto from a dict
quote_update_dto_from_dict = QuoteUpdateDto.from_dict(quote_update_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


