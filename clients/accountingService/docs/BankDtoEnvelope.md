# BankDtoEnvelope


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_success** | **bool** |  | [optional] [readonly] 
**error_message** | **str** |  | [optional] 
**correlation_id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] [readonly] 
**activity_id** | **str** |  | [optional] [readonly] 
**result** | [**BankDto**](BankDto.md) |  | [optional] 

## Example

```python
from openapi_client.models.bank_dto_envelope import BankDtoEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of BankDtoEnvelope from a JSON string
bank_dto_envelope_instance = BankDtoEnvelope.from_json(json)
# print the JSON string representation of the object
print(BankDtoEnvelope.to_json())

# convert the object into a dict
bank_dto_envelope_dict = bank_dto_envelope_instance.to_dict()
# create an instance of BankDtoEnvelope from a dict
bank_dto_envelope_from_dict = BankDtoEnvelope.from_dict(bank_dto_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


