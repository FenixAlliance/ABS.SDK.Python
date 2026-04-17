# BudgetCreateDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] 
**name** | **str** |  | [optional] 
**fiscal_year_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.budget_create_dto import BudgetCreateDto

# TODO update the JSON string below
json = "{}"
# create an instance of BudgetCreateDto from a JSON string
budget_create_dto_instance = BudgetCreateDto.from_json(json)
# print the JSON string representation of the object
print(BudgetCreateDto.to_json())

# convert the object into a dict
budget_create_dto_dict = budget_create_dto_instance.to_dict()
# create an instance of BudgetCreateDto from a dict
budget_create_dto_from_dict = BudgetCreateDto.from_dict(budget_create_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


