# ExpenseTypeUpdateDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**enabled** | **bool** |  | [optional] 

## Example

```python
from openapi_client.models.expense_type_update_dto import ExpenseTypeUpdateDto

# TODO update the JSON string below
json = "{}"
# create an instance of ExpenseTypeUpdateDto from a JSON string
expense_type_update_dto_instance = ExpenseTypeUpdateDto.from_json(json)
# print the JSON string representation of the object
print(ExpenseTypeUpdateDto.to_json())

# convert the object into a dict
expense_type_update_dto_dict = expense_type_update_dto_instance.to_dict()
# create an instance of ExpenseTypeUpdateDto from a dict
expense_type_update_dto_from_dict = ExpenseTypeUpdateDto.from_dict(expense_type_update_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


