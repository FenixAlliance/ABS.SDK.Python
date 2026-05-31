# ExpenseTypeDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] 
**name** | **str** |  | [optional] 
**enabled** | **bool** |  | [optional] 
**tenant_id** | **str** |  | [optional] 
**enrollment_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.expense_type_dto import ExpenseTypeDto

# TODO update the JSON string below
json = "{}"
# create an instance of ExpenseTypeDto from a JSON string
expense_type_dto_instance = ExpenseTypeDto.from_json(json)
# print the JSON string representation of the object
print(ExpenseTypeDto.to_json())

# convert the object into a dict
expense_type_dto_dict = expense_type_dto_instance.to_dict()
# create an instance of ExpenseTypeDto from a dict
expense_type_dto_from_dict = ExpenseTypeDto.from_dict(expense_type_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


