# BudgetDtoEnvelope


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_success** | **bool** |  | [optional] [readonly] 
**error_message** | **str** |  | [optional] 
**correlation_id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] [readonly] 
**activity_id** | **str** |  | [optional] [readonly] 
**result** | [**BudgetDto**](BudgetDto.md) |  | [optional] 

## Example

```python
from openapi_client.models.budget_dto_envelope import BudgetDtoEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of BudgetDtoEnvelope from a JSON string
budget_dto_envelope_instance = BudgetDtoEnvelope.from_json(json)
# print the JSON string representation of the object
print(BudgetDtoEnvelope.to_json())

# convert the object into a dict
budget_dto_envelope_dict = budget_dto_envelope_instance.to_dict()
# create an instance of BudgetDtoEnvelope from a dict
budget_dto_envelope_from_dict = BudgetDtoEnvelope.from_dict(budget_dto_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


