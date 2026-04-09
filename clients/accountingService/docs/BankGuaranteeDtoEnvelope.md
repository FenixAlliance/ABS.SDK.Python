# BankGuaranteeDtoEnvelope


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_success** | **bool** |  | [optional] [readonly] 
**error_message** | **str** |  | [optional] 
**correlation_id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] [readonly] 
**activity_id** | **str** |  | [optional] [readonly] 
**result** | [**BankGuaranteeDto**](BankGuaranteeDto.md) |  | [optional] 

## Example

```python
from openapi_client.models.bank_guarantee_dto_envelope import BankGuaranteeDtoEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of BankGuaranteeDtoEnvelope from a JSON string
bank_guarantee_dto_envelope_instance = BankGuaranteeDtoEnvelope.from_json(json)
# print the JSON string representation of the object
print(BankGuaranteeDtoEnvelope.to_json())

# convert the object into a dict
bank_guarantee_dto_envelope_dict = bank_guarantee_dto_envelope_instance.to_dict()
# create an instance of BankGuaranteeDtoEnvelope from a dict
bank_guarantee_dto_envelope_from_dict = BankGuaranteeDtoEnvelope.from_dict(bank_guarantee_dto_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


