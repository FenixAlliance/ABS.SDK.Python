# InvoiceReferenceCreateDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] [readonly] 
**timestamp** | **datetime** |  | [optional] [readonly] 
**tenant_id** | **str** |  | [optional] 
**enrollment_id** | **str** |  | [optional] 
**referral_invoice_id** | **str** |  | [optional] 
**referenced_invoice_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.invoice_reference_create_dto import InvoiceReferenceCreateDto

# TODO update the JSON string below
json = "{}"
# create an instance of InvoiceReferenceCreateDto from a JSON string
invoice_reference_create_dto_instance = InvoiceReferenceCreateDto.from_json(json)
# print the JSON string representation of the object
print(InvoiceReferenceCreateDto.to_json())

# convert the object into a dict
invoice_reference_create_dto_dict = invoice_reference_create_dto_instance.to_dict()
# create an instance of InvoiceReferenceCreateDto from a dict
invoice_reference_create_dto_from_dict = InvoiceReferenceCreateDto.from_dict(invoice_reference_create_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


