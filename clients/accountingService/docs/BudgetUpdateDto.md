# BudgetUpdateDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**fiscal_year_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.budget_update_dto import BudgetUpdateDto

# TODO update the JSON string below
json = "{}"
# create an instance of BudgetUpdateDto from a JSON string
budget_update_dto_instance = BudgetUpdateDto.from_json(json)
# print the JSON string representation of the object
print(BudgetUpdateDto.to_json())

# convert the object into a dict
budget_update_dto_dict = budget_update_dto_instance.to_dict()
# create an instance of BudgetUpdateDto from a dict
budget_update_dto_from_dict = BudgetUpdateDto.from_dict(budget_update_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


