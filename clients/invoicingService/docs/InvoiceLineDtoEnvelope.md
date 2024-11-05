# InvoiceLineDtoEnvelope


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_success** | **bool** |  | [optional] [readonly] 
**error_message** | **str** |  | [optional] 
**correlation_id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] [readonly] 
**activity_id** | **str** |  | [optional] [readonly] 
**result** | [**InvoiceLineDto**](InvoiceLineDto.md) |  | [optional] 

## Example

```python
from openapi_client.models.invoice_line_dto_envelope import InvoiceLineDtoEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of InvoiceLineDtoEnvelope from a JSON string
invoice_line_dto_envelope_instance = InvoiceLineDtoEnvelope.from_json(json)
# print the JSON string representation of the object
print(InvoiceLineDtoEnvelope.to_json())

# convert the object into a dict
invoice_line_dto_envelope_dict = invoice_line_dto_envelope_instance.to_dict()
# create an instance of InvoiceLineDtoEnvelope from a dict
invoice_line_dto_envelope_from_dict = InvoiceLineDtoEnvelope.from_dict(invoice_line_dto_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


