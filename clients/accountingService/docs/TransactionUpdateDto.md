# TransactionUpdateDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
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
from openapi_client.models.transaction_update_dto import TransactionUpdateDto

# TODO update the JSON string below
json = "{}"
# create an instance of TransactionUpdateDto from a JSON string
transaction_update_dto_instance = TransactionUpdateDto.from_json(json)
# print the JSON string representation of the object
print(TransactionUpdateDto.to_json())

# convert the object into a dict
transaction_update_dto_dict = transaction_update_dto_instance.to_dict()
# create an instance of TransactionUpdateDto from a dict
transaction_update_dto_from_dict = TransactionUpdateDto.from_dict(transaction_update_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


