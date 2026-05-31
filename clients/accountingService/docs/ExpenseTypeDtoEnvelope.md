# ExpenseTypeDtoEnvelope


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_success** | **bool** |  | [optional] [readonly] 
**error_message** | **str** |  | [optional] 
**correlation_id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] [readonly] 
**activity_id** | **str** |  | [optional] [readonly] 
**result** | [**ExpenseTypeDto**](ExpenseTypeDto.md) |  | [optional] 

## Example

```python
from openapi_client.models.expense_type_dto_envelope import ExpenseTypeDtoEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of ExpenseTypeDtoEnvelope from a JSON string
expense_type_dto_envelope_instance = ExpenseTypeDtoEnvelope.from_json(json)
# print the JSON string representation of the object
print(ExpenseTypeDtoEnvelope.to_json())

# convert the object into a dict
expense_type_dto_envelope_dict = expense_type_dto_envelope_instance.to_dict()
# create an instance of ExpenseTypeDtoEnvelope from a dict
expense_type_dto_envelope_from_dict = ExpenseTypeDtoEnvelope.from_dict(expense_type_dto_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


