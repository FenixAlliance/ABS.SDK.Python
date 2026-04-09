# TransactionDtoListEnvelope


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_success** | **bool** |  | [optional] [readonly] 
**error_message** | **str** |  | [optional] 
**correlation_id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] [readonly] 
**activity_id** | **str** |  | [optional] [readonly] 
**result** | [**List[TransactionDto]**](TransactionDto.md) |  | [optional] 

## Example

```python
from openapi_client.models.transaction_dto_list_envelope import TransactionDtoListEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of TransactionDtoListEnvelope from a JSON string
transaction_dto_list_envelope_instance = TransactionDtoListEnvelope.from_json(json)
# print the JSON string representation of the object
print(TransactionDtoListEnvelope.to_json())

# convert the object into a dict
transaction_dto_list_envelope_dict = transaction_dto_list_envelope_instance.to_dict()
# create an instance of TransactionDtoListEnvelope from a dict
transaction_dto_list_envelope_from_dict = TransactionDtoListEnvelope.from_dict(transaction_dto_list_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


