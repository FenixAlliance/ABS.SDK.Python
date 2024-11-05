# InvoiceAdjustmentDtoListEnvelope


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_success** | **bool** |  | [optional] [readonly] 
**error_message** | **str** |  | [optional] 
**correlation_id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] [readonly] 
**activity_id** | **str** |  | [optional] [readonly] 
**result** | [**List[InvoiceAdjustmentDto]**](InvoiceAdjustmentDto.md) |  | [optional] 

## Example

```python
from openapi_client.models.invoice_adjustment_dto_list_envelope import InvoiceAdjustmentDtoListEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of InvoiceAdjustmentDtoListEnvelope from a JSON string
invoice_adjustment_dto_list_envelope_instance = InvoiceAdjustmentDtoListEnvelope.from_json(json)
# print the JSON string representation of the object
print(InvoiceAdjustmentDtoListEnvelope.to_json())

# convert the object into a dict
invoice_adjustment_dto_list_envelope_dict = invoice_adjustment_dto_list_envelope_instance.to_dict()
# create an instance of InvoiceAdjustmentDtoListEnvelope from a dict
invoice_adjustment_dto_list_envelope_from_dict = InvoiceAdjustmentDtoListEnvelope.from_dict(invoice_adjustment_dto_list_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


