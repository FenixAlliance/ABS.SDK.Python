# InvoiceDtoEnvelope


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_success** | **bool** |  | [optional] [readonly] 
**error_message** | **str** |  | [optional] 
**correlation_id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] [readonly] 
**activity_id** | **str** |  | [optional] [readonly] 
**result** | [**InvoiceDto**](InvoiceDto.md) |  | [optional] 

## Example

```python
from openapi_client.models.invoice_dto_envelope import InvoiceDtoEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of InvoiceDtoEnvelope from a JSON string
invoice_dto_envelope_instance = InvoiceDtoEnvelope.from_json(json)
# print the JSON string representation of the object
print(InvoiceDtoEnvelope.to_json())

# convert the object into a dict
invoice_dto_envelope_dict = invoice_dto_envelope_instance.to_dict()
# create an instance of InvoiceDtoEnvelope from a dict
invoice_dto_envelope_from_dict = InvoiceDtoEnvelope.from_dict(invoice_dto_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


