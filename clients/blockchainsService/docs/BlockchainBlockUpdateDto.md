# BlockchainBlockUpdateDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | **str** |  | [optional] 
**nonce** | **int** |  | [optional] 

## Example

```python
from openapi_client.models.blockchain_block_update_dto import BlockchainBlockUpdateDto

# TODO update the JSON string below
json = "{}"
# create an instance of BlockchainBlockUpdateDto from a JSON string
blockchain_block_update_dto_instance = BlockchainBlockUpdateDto.from_json(json)
# print the JSON string representation of the object
print(BlockchainBlockUpdateDto.to_json())

# convert the object into a dict
blockchain_block_update_dto_dict = blockchain_block_update_dto_instance.to_dict()
# create an instance of BlockchainBlockUpdateDto from a dict
blockchain_block_update_dto_from_dict = BlockchainBlockUpdateDto.from_dict(blockchain_block_update_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


