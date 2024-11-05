# InvoiceReferenceDtoListEnvelope


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_success** | **bool** |  | [optional] [readonly] 
**error_message** | **str** |  | [optional] 
**correlation_id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] [readonly] 
**activity_id** | **str** |  | [optional] [readonly] 
**result** | [**List[InvoiceReferenceDto]**](InvoiceReferenceDto.md) |  | [optional] 

## Example

```python
from openapi_client.models.invoice_reference_dto_list_envelope import InvoiceReferenceDtoListEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of InvoiceReferenceDtoListEnvelope from a JSON string
invoice_reference_dto_list_envelope_instance = InvoiceReferenceDtoListEnvelope.from_json(json)
# print the JSON string representation of the object
print(InvoiceReferenceDtoListEnvelope.to_json())

# convert the object into a dict
invoice_reference_dto_list_envelope_dict = invoice_reference_dto_list_envelope_instance.to_dict()
# create an instance of InvoiceReferenceDtoListEnvelope from a dict
invoice_reference_dto_list_envelope_from_dict = InvoiceReferenceDtoListEnvelope.from_dict(invoice_reference_dto_list_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


