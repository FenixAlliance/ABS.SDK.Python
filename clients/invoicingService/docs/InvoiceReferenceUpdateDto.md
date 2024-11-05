# InvoiceReferenceUpdateDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**referenced_invoice_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.invoice_reference_update_dto import InvoiceReferenceUpdateDto

# TODO update the JSON string below
json = "{}"
# create an instance of InvoiceReferenceUpdateDto from a JSON string
invoice_reference_update_dto_instance = InvoiceReferenceUpdateDto.from_json(json)
# print the JSON string representation of the object
print(InvoiceReferenceUpdateDto.to_json())

# convert the object into a dict
invoice_reference_update_dto_dict = invoice_reference_update_dto_instance.to_dict()
# create an instance of InvoiceReferenceUpdateDto from a dict
invoice_reference_update_dto_from_dict = InvoiceReferenceUpdateDto.from_dict(invoice_reference_update_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


