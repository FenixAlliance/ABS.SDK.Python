# InvoiceLineUpdateDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**price** | **float** |  | [optional] 
**unit_id** | **str** |  | [optional] 
**percent** | **float** |  | [optional] 
**unit_group_id** | **str** |  | [optional] 
**currency_id** | **str** |  | [optional] 
**discount_list_id** | **str** |  | [optional] 
**rounding_policy_id** | **str** |  | [optional] 
**quantity** | **int** |  | [optional] 
**item_id** | **str** |  | [optional] 
**item_price_id** | **str** |  | [optional] 
**invoice_line_id** | **str** |  | [optional] 
**tax_amount_in_usd** | **float** |  | [optional] 
**tax_base_amount_in_usd** | **float** |  | [optional] 

## Example

```python
from openapi_client.models.invoice_line_update_dto import InvoiceLineUpdateDto

# TODO update the JSON string below
json = "{}"
# create an instance of InvoiceLineUpdateDto from a JSON string
invoice_line_update_dto_instance = InvoiceLineUpdateDto.from_json(json)
# print the JSON string representation of the object
print(InvoiceLineUpdateDto.to_json())

# convert the object into a dict
invoice_line_update_dto_dict = invoice_line_update_dto_instance.to_dict()
# create an instance of InvoiceLineUpdateDto from a dict
invoice_line_update_dto_from_dict = InvoiceLineUpdateDto.from_dict(invoice_line_update_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


