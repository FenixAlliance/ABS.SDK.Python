# BlockchainBlockCreateDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] 
**hash** | **str** |  | 
**data** | **str** |  | [optional] 
**nonce** | **int** |  | [optional] 
**previous_hash** | **str** |  | [optional] 
**blockchain_id** | **str** |  | 
**wallet_account_id** | **str** |  | 

## Example

```python
from openapi_client.models.blockchain_block_create_dto import BlockchainBlockCreateDto

# TODO update the JSON string below
json = "{}"
# create an instance of BlockchainBlockCreateDto from a JSON string
blockchain_block_create_dto_instance = BlockchainBlockCreateDto.from_json(json)
# print the JSON string representation of the object
print(BlockchainBlockCreateDto.to_json())

# convert the object into a dict
blockchain_block_create_dto_dict = blockchain_block_create_dto_instance.to_dict()
# create an instance of BlockchainBlockCreateDto from a dict
blockchain_block_create_dto_from_dict = BlockchainBlockCreateDto.from_dict(blockchain_block_create_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


