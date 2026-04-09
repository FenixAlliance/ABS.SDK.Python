# TransactionDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] 
**description** | **str** |  | [optional] 
**price** | **float** |  | [optional] 
**quantity** | **float** |  | [optional] 
**external_description** | **str** |  | [optional] 
**basis_quantity** | **float** |  | [optional] 
**basis_amount** | **float** |  | [optional] 
**percent** | **float** |  | [optional] 
**unit_group_id** | **str** |  | [optional] 
**unit_id** | **str** |  | [optional] 
**transaction_category_id** | **str** |  | [optional] 
**currency_id** | **str** |  | [optional] 
**tenant_id** | **str** |  | [optional] 
**enrollment_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.transaction_dto import TransactionDto

# TODO update the JSON string below
json = "{}"
# create an instance of TransactionDto from a JSON string
transaction_dto_instance = TransactionDto.from_json(json)
# print the JSON string representation of the object
print(TransactionDto.to_json())

# convert the object into a dict
transaction_dto_dict = transaction_dto_instance.to_dict()
# create an instance of TransactionDto from a dict
transaction_dto_from_dict = TransactionDto.from_dict(transaction_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


