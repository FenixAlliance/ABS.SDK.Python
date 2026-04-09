# AccountingPeriodDtoListEnvelope


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_success** | **bool** |  | [optional] [readonly] 
**error_message** | **str** |  | [optional] 
**correlation_id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] [readonly] 
**activity_id** | **str** |  | [optional] [readonly] 
**result** | [**List[AccountingPeriodDto]**](AccountingPeriodDto.md) |  | [optional] 

## Example

```python
from openapi_client.models.accounting_period_dto_list_envelope import AccountingPeriodDtoListEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of AccountingPeriodDtoListEnvelope from a JSON string
accounting_period_dto_list_envelope_instance = AccountingPeriodDtoListEnvelope.from_json(json)
# print the JSON string representation of the object
print(AccountingPeriodDtoListEnvelope.to_json())

# convert the object into a dict
accounting_period_dto_list_envelope_dict = accounting_period_dto_list_envelope_instance.to_dict()
# create an instance of AccountingPeriodDtoListEnvelope from a dict
accounting_period_dto_list_envelope_from_dict = AccountingPeriodDtoListEnvelope.from_dict(accounting_period_dto_list_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


