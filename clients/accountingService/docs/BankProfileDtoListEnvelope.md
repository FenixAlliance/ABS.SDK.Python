# BankProfileDtoListEnvelope


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_success** | **bool** |  | [optional] [readonly] 
**error_message** | **str** |  | [optional] 
**correlation_id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] [readonly] 
**activity_id** | **str** |  | [optional] [readonly] 
**result** | [**List[BankProfileDto]**](BankProfileDto.md) |  | [optional] 

## Example

```python
from openapi_client.models.bank_profile_dto_list_envelope import BankProfileDtoListEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of BankProfileDtoListEnvelope from a JSON string
bank_profile_dto_list_envelope_instance = BankProfileDtoListEnvelope.from_json(json)
# print the JSON string representation of the object
print(BankProfileDtoListEnvelope.to_json())

# convert the object into a dict
bank_profile_dto_list_envelope_dict = bank_profile_dto_list_envelope_instance.to_dict()
# create an instance of BankProfileDtoListEnvelope from a dict
bank_profile_dto_list_envelope_from_dict = BankProfileDtoListEnvelope.from_dict(bank_profile_dto_list_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


