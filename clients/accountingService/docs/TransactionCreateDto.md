# TransactionCreateDto


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

## Example

```python
from openapi_client.models.transaction_create_dto import TransactionCreateDto

# TODO update the JSON string below
json = "{}"
# create an instance of TransactionCreateDto from a JSON string
transaction_create_dto_instance = TransactionCreateDto.from_json(json)
# print the JSON string representation of the object
print(TransactionCreateDto.to_json())

# convert the object into a dict
transaction_create_dto_dict = transaction_create_dto_instance.to_dict()
# create an instance of TransactionCreateDto from a dict
transaction_create_dto_from_dict = TransactionCreateDto.from_dict(transaction_create_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


