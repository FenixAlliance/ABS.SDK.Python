# CostCentreBudgetDtoEnvelope


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_success** | **bool** |  | [optional] [readonly] 
**error_message** | **str** |  | [optional] 
**correlation_id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] [readonly] 
**activity_id** | **str** |  | [optional] [readonly] 
**result** | [**CostCentreBudgetDto**](CostCentreBudgetDto.md) |  | [optional] 

## Example

```python
from openapi_client.models.cost_centre_budget_dto_envelope import CostCentreBudgetDtoEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of CostCentreBudgetDtoEnvelope from a JSON string
cost_centre_budget_dto_envelope_instance = CostCentreBudgetDtoEnvelope.from_json(json)
# print the JSON string representation of the object
print(CostCentreBudgetDtoEnvelope.to_json())

# convert the object into a dict
cost_centre_budget_dto_envelope_dict = cost_centre_budget_dto_envelope_instance.to_dict()
# create an instance of CostCentreBudgetDtoEnvelope from a dict
cost_centre_budget_dto_envelope_from_dict = CostCentreBudgetDtoEnvelope.from_dict(cost_centre_budget_dto_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


