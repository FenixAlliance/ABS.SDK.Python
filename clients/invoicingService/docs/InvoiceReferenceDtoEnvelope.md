# InvoiceReferenceDtoEnvelope


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_success** | **bool** |  | [optional] [readonly] 
**error_message** | **str** |  | [optional] 
**correlation_id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] [readonly] 
**activity_id** | **str** |  | [optional] [readonly] 
**result** | [**InvoiceReferenceDto**](InvoiceReferenceDto.md) |  | [optional] 

## Example

```python
from openapi_client.models.invoice_reference_dto_envelope import InvoiceReferenceDtoEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of InvoiceReferenceDtoEnvelope from a JSON string
invoice_reference_dto_envelope_instance = InvoiceReferenceDtoEnvelope.from_json(json)
# print the JSON string representation of the object
print(InvoiceReferenceDtoEnvelope.to_json())

# convert the object into a dict
invoice_reference_dto_envelope_dict = invoice_reference_dto_envelope_instance.to_dict()
# create an instance of InvoiceReferenceDtoEnvelope from a dict
invoice_reference_dto_envelope_from_dict = InvoiceReferenceDtoEnvelope.from_dict(invoice_reference_dto_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


