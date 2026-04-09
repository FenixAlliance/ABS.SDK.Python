# CostCentreBudgetUpdateDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**fiscal_year_id** | **str** |  | [optional] 
**cost_centre_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.cost_centre_budget_update_dto import CostCentreBudgetUpdateDto

# TODO update the JSON string below
json = "{}"
# create an instance of CostCentreBudgetUpdateDto from a JSON string
cost_centre_budget_update_dto_instance = CostCentreBudgetUpdateDto.from_json(json)
# print the JSON string representation of the object
print(CostCentreBudgetUpdateDto.to_json())

# convert the object into a dict
cost_centre_budget_update_dto_dict = cost_centre_budget_update_dto_instance.to_dict()
# create an instance of CostCentreBudgetUpdateDto from a dict
cost_centre_budget_update_dto_from_dict = CostCentreBudgetUpdateDto.from_dict(cost_centre_budget_update_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


