# TransactionCategoryUpdateDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**enrollment_id** | **str** |  | [optional] 
**tenant_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.transaction_category_update_dto import TransactionCategoryUpdateDto

# TODO update the JSON string below
json = "{}"
# create an instance of TransactionCategoryUpdateDto from a JSON string
transaction_category_update_dto_instance = TransactionCategoryUpdateDto.from_json(json)
# print the JSON string representation of the object
print(TransactionCategoryUpdateDto.to_json())

# convert the object into a dict
transaction_category_update_dto_dict = transaction_category_update_dto_instance.to_dict()
# create an instance of TransactionCategoryUpdateDto from a dict
transaction_category_update_dto_from_dict = TransactionCategoryUpdateDto.from_dict(transaction_category_update_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


