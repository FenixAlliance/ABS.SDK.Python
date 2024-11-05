# InvoiceReferenceDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] 
**tenant_id** | **str** |  | [optional] 
**enrollment_id** | **str** |  | [optional] 
**referral_invoice_id** | **str** |  | [optional] 
**referenced_invoice_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.invoice_reference_dto import InvoiceReferenceDto

# TODO update the JSON string below
json = "{}"
# create an instance of InvoiceReferenceDto from a JSON string
invoice_reference_dto_instance = InvoiceReferenceDto.from_json(json)
# print the JSON string representation of the object
print(InvoiceReferenceDto.to_json())

# convert the object into a dict
invoice_reference_dto_dict = invoice_reference_dto_instance.to_dict()
# create an instance of InvoiceReferenceDto from a dict
invoice_reference_dto_from_dict = InvoiceReferenceDto.from_dict(invoice_reference_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


