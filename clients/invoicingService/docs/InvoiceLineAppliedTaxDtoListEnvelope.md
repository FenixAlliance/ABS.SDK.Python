# InvoiceLineAppliedTaxDtoListEnvelope


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_success** | **bool** |  | [optional] [readonly] 
**error_message** | **str** |  | [optional] 
**correlation_id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] [readonly] 
**activity_id** | **str** |  | [optional] [readonly] 
**result** | [**List[InvoiceLineAppliedTaxDto]**](InvoiceLineAppliedTaxDto.md) |  | [optional] 

## Example

```python
from openapi_client.models.invoice_line_applied_tax_dto_list_envelope import InvoiceLineAppliedTaxDtoListEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of InvoiceLineAppliedTaxDtoListEnvelope from a JSON string
invoice_line_applied_tax_dto_list_envelope_instance = InvoiceLineAppliedTaxDtoListEnvelope.from_json(json)
# print the JSON string representation of the object
print(InvoiceLineAppliedTaxDtoListEnvelope.to_json())

# convert the object into a dict
invoice_line_applied_tax_dto_list_envelope_dict = invoice_line_applied_tax_dto_list_envelope_instance.to_dict()
# create an instance of InvoiceLineAppliedTaxDtoListEnvelope from a dict
invoice_line_applied_tax_dto_list_envelope_from_dict = InvoiceLineAppliedTaxDtoListEnvelope.from_dict(invoice_line_applied_tax_dto_list_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


