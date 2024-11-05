# InvoiceLineAppliedTaxUpdateDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tax_policy_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.invoice_line_applied_tax_update_dto import InvoiceLineAppliedTaxUpdateDto

# TODO update the JSON string below
json = "{}"
# create an instance of InvoiceLineAppliedTaxUpdateDto from a JSON string
invoice_line_applied_tax_update_dto_instance = InvoiceLineAppliedTaxUpdateDto.from_json(json)
# print the JSON string representation of the object
print(InvoiceLineAppliedTaxUpdateDto.to_json())

# convert the object into a dict
invoice_line_applied_tax_update_dto_dict = invoice_line_applied_tax_update_dto_instance.to_dict()
# create an instance of InvoiceLineAppliedTaxUpdateDto from a dict
invoice_line_applied_tax_update_dto_from_dict = InvoiceLineAppliedTaxUpdateDto.from_dict(invoice_line_applied_tax_update_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


