# TransactionCategoryCreateDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] 
**name** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**enrollment_id** | **str** |  | [optional] 
**tenant_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.transaction_category_create_dto import TransactionCategoryCreateDto

# TODO update the JSON string below
json = "{}"
# create an instance of TransactionCategoryCreateDto from a JSON string
transaction_category_create_dto_instance = TransactionCategoryCreateDto.from_json(json)
# print the JSON string representation of the object
print(TransactionCategoryCreateDto.to_json())

# convert the object into a dict
transaction_category_create_dto_dict = transaction_category_create_dto_instance.to_dict()
# create an instance of TransactionCategoryCreateDto from a dict
transaction_category_create_dto_from_dict = TransactionCategoryCreateDto.from_dict(transaction_category_create_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


