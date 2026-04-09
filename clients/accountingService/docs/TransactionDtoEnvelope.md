# TransactionDtoEnvelope


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_success** | **bool** |  | [optional] [readonly] 
**error_message** | **str** |  | [optional] 
**correlation_id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] [readonly] 
**activity_id** | **str** |  | [optional] [readonly] 
**result** | [**TransactionDto**](TransactionDto.md) |  | [optional] 

## Example

```python
from openapi_client.models.transaction_dto_envelope import TransactionDtoEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of TransactionDtoEnvelope from a JSON string
transaction_dto_envelope_instance = TransactionDtoEnvelope.from_json(json)
# print the JSON string representation of the object
print(TransactionDtoEnvelope.to_json())

# convert the object into a dict
transaction_dto_envelope_dict = transaction_dto_envelope_instance.to_dict()
# create an instance of TransactionDtoEnvelope from a dict
transaction_dto_envelope_from_dict = TransactionDtoEnvelope.from_dict(transaction_dto_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


