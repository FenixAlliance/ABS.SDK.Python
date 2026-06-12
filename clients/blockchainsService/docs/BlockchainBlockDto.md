# BlockchainBlockDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] 
**index** | **int** |  | [optional] 
**hash** | **str** |  | [optional] 
**data** | **str** |  | [optional] 
**nonce** | **int** |  | [optional] 
**previous_hash** | **str** |  | [optional] 
**blockchain_id** | **str** |  | [optional] 
**wallet_account_id** | **str** |  | [optional] 
**tenant_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.blockchain_block_dto import BlockchainBlockDto

# TODO update the JSON string below
json = "{}"
# create an instance of BlockchainBlockDto from a JSON string
blockchain_block_dto_instance = BlockchainBlockDto.from_json(json)
# print the JSON string representation of the object
print(BlockchainBlockDto.to_json())

# convert the object into a dict
blockchain_block_dto_dict = blockchain_block_dto_instance.to_dict()
# create an instance of BlockchainBlockDto from a dict
blockchain_block_dto_from_dict = BlockchainBlockDto.from_dict(blockchain_block_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


