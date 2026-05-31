# ExpenseTypeCreateDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] 
**name** | **str** |  | [optional] 
**enabled** | **bool** |  | [optional] 

## Example

```python
from openapi_client.models.expense_type_create_dto import ExpenseTypeCreateDto

# TODO update the JSON string below
json = "{}"
# create an instance of ExpenseTypeCreateDto from a JSON string
expense_type_create_dto_instance = ExpenseTypeCreateDto.from_json(json)
# print the JSON string representation of the object
print(ExpenseTypeCreateDto.to_json())

# convert the object into a dict
expense_type_create_dto_dict = expense_type_create_dto_instance.to_dict()
# create an instance of ExpenseTypeCreateDto from a dict
expense_type_create_dto_from_dict = ExpenseTypeCreateDto.from_dict(expense_type_create_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


