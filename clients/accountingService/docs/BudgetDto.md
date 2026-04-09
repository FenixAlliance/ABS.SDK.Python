# BudgetDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] 
**name** | **str** |  | [optional] 
**tenant_id** | **str** |  | [optional] 
**fiscal_year_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.budget_dto import BudgetDto

# TODO update the JSON string below
json = "{}"
# create an instance of BudgetDto from a JSON string
budget_dto_instance = BudgetDto.from_json(json)
# print the JSON string representation of the object
print(BudgetDto.to_json())

# convert the object into a dict
budget_dto_dict = budget_dto_instance.to_dict()
# create an instance of BudgetDto from a dict
budget_dto_from_dict = BudgetDto.from_dict(budget_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


