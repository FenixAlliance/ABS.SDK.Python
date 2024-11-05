# InvoiceLineAppliedTaxDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] 
**tenant_id** | **str** |  | [optional] 
**invoice_id** | **str** |  | [optional] 
**enrollment_id** | **str** |  | [optional] 
**invoice_line_id** | **str** |  | [optional] 
**tax_policy_id** | **str** |  | [optional] 
**item_price_id** | **str** |  | [optional] 
**item_id** | **str** |  | [optional] 
**tax_amount_in_usd** | **float** |  | [optional] 
**tax_base_amount_in_usd** | **float** |  | [optional] 
**tax_policy_name** | **str** |  | [optional] 
**tax_policy_description** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.invoice_line_applied_tax_dto import InvoiceLineAppliedTaxDto

# TODO update the JSON string below
json = "{}"
# create an instance of InvoiceLineAppliedTaxDto from a JSON string
invoice_line_applied_tax_dto_instance = InvoiceLineAppliedTaxDto.from_json(json)
# print the JSON string representation of the object
print(InvoiceLineAppliedTaxDto.to_json())

# convert the object into a dict
invoice_line_applied_tax_dto_dict = invoice_line_applied_tax_dto_instance.to_dict()
# create an instance of InvoiceLineAppliedTaxDto from a dict
invoice_line_applied_tax_dto_from_dict = InvoiceLineAppliedTaxDto.from_dict(invoice_line_applied_tax_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


