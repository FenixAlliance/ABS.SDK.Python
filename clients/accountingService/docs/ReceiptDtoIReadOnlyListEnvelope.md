# ReceiptDtoIReadOnlyListEnvelope


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_success** | **bool** |  | [optional] [readonly] 
**error_message** | **str** |  | [optional] 
**correlation_id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] [readonly] 
**activity_id** | **str** |  | [optional] [readonly] 
**result** | [**List[ReceiptDto]**](ReceiptDto.md) |  | [optional] 

## Example

```python
from openapi_client.models.receipt_dto_i_read_only_list_envelope import ReceiptDtoIReadOnlyListEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of ReceiptDtoIReadOnlyListEnvelope from a JSON string
receipt_dto_i_read_only_list_envelope_instance = ReceiptDtoIReadOnlyListEnvelope.from_json(json)
# print the JSON string representation of the object
print(ReceiptDtoIReadOnlyListEnvelope.to_json())

# convert the object into a dict
receipt_dto_i_read_only_list_envelope_dict = receipt_dto_i_read_only_list_envelope_instance.to_dict()
# create an instance of ReceiptDtoIReadOnlyListEnvelope from a dict
receipt_dto_i_read_only_list_envelope_from_dict = ReceiptDtoIReadOnlyListEnvelope.from_dict(receipt_dto_i_read_only_list_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


