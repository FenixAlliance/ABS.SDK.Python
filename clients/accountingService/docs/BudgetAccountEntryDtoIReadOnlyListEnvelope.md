# BudgetAccountEntryDtoIReadOnlyListEnvelope


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_success** | **bool** |  | [optional] [readonly] 
**error_message** | **str** |  | [optional] 
**correlation_id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] [readonly] 
**activity_id** | **str** |  | [optional] [readonly] 
**result** | [**List[BudgetAccountEntryDto]**](BudgetAccountEntryDto.md) |  | [optional] 

## Example

```python
from openapi_client.models.budget_account_entry_dto_i_read_only_list_envelope import BudgetAccountEntryDtoIReadOnlyListEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of BudgetAccountEntryDtoIReadOnlyListEnvelope from a JSON string
budget_account_entry_dto_i_read_only_list_envelope_instance = BudgetAccountEntryDtoIReadOnlyListEnvelope.from_json(json)
# print the JSON string representation of the object
print(BudgetAccountEntryDtoIReadOnlyListEnvelope.to_json())

# convert the object into a dict
budget_account_entry_dto_i_read_only_list_envelope_dict = budget_account_entry_dto_i_read_only_list_envelope_instance.to_dict()
# create an instance of BudgetAccountEntryDtoIReadOnlyListEnvelope from a dict
budget_account_entry_dto_i_read_only_list_envelope_from_dict = BudgetAccountEntryDtoIReadOnlyListEnvelope.from_dict(budget_account_entry_dto_i_read_only_list_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


