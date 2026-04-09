# InvoiceEnumerationRangeDtoListEnvelope


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_success** | **bool** |  | [optional] [readonly] 
**error_message** | **str** |  | [optional] 
**correlation_id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] [readonly] 
**activity_id** | **str** |  | [optional] [readonly] 
**result** | [**List[InvoiceEnumerationRangeDto]**](InvoiceEnumerationRangeDto.md) |  | [optional] 

## Example

```python
from openapi_client.models.invoice_enumeration_range_dto_list_envelope import InvoiceEnumerationRangeDtoListEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of InvoiceEnumerationRangeDtoListEnvelope from a JSON string
invoice_enumeration_range_dto_list_envelope_instance = InvoiceEnumerationRangeDtoListEnvelope.from_json(json)
# print the JSON string representation of the object
print(InvoiceEnumerationRangeDtoListEnvelope.to_json())

# convert the object into a dict
invoice_enumeration_range_dto_list_envelope_dict = invoice_enumeration_range_dto_list_envelope_instance.to_dict()
# create an instance of InvoiceEnumerationRangeDtoListEnvelope from a dict
invoice_enumeration_range_dto_list_envelope_from_dict = InvoiceEnumerationRangeDtoListEnvelope.from_dict(invoice_enumeration_range_dto_list_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


