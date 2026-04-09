# CostCentreBudgetCreateDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] 
**name** | **str** |  | [optional] 
**tenant_id** | **str** |  | [optional] 
**fiscal_year_id** | **str** |  | [optional] 
**cost_centre_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.cost_centre_budget_create_dto import CostCentreBudgetCreateDto

# TODO update the JSON string below
json = "{}"
# create an instance of CostCentreBudgetCreateDto from a JSON string
cost_centre_budget_create_dto_instance = CostCentreBudgetCreateDto.from_json(json)
# print the JSON string representation of the object
print(CostCentreBudgetCreateDto.to_json())

# convert the object into a dict
cost_centre_budget_create_dto_dict = cost_centre_budget_create_dto_instance.to_dict()
# create an instance of CostCentreBudgetCreateDto from a dict
cost_centre_budget_create_dto_from_dict = CostCentreBudgetCreateDto.from_dict(cost_centre_budget_create_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


