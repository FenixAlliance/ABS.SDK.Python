# ReceiptDtoEnvelope


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_success** | **bool** |  | [optional] [readonly] 
**error_message** | **str** |  | [optional] 
**correlation_id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] [readonly] 
**activity_id** | **str** |  | [optional] [readonly] 
**result** | [**ReceiptDto**](ReceiptDto.md) |  | [optional] 

## Example

```python
from openapi_client.models.receipt_dto_envelope import ReceiptDtoEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of ReceiptDtoEnvelope from a JSON string
receipt_dto_envelope_instance = ReceiptDtoEnvelope.from_json(json)
# print the JSON string representation of the object
print(ReceiptDtoEnvelope.to_json())

# convert the object into a dict
receipt_dto_envelope_dict = receipt_dto_envelope_instance.to_dict()
# create an instance of ReceiptDtoEnvelope from a dict
receipt_dto_envelope_from_dict = ReceiptDtoEnvelope.from_dict(receipt_dto_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


