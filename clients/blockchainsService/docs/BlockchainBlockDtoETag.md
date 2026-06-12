# BlockchainBlockDtoETag


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_well_formed** | **bool** |  | [optional] 
**entity_type** | [**Type**](Type.md) |  | [optional] 
**is_any** | **bool** |  | [optional] 
**is_if_none_match** | **bool** |  | [optional] 

## Example

```python
from openapi_client.models.blockchain_block_dto_e_tag import BlockchainBlockDtoETag

# TODO update the JSON string below
json = "{}"
# create an instance of BlockchainBlockDtoETag from a JSON string
blockchain_block_dto_e_tag_instance = BlockchainBlockDtoETag.from_json(json)
# print the JSON string representation of the object
print(BlockchainBlockDtoETag.to_json())

# convert the object into a dict
blockchain_block_dto_e_tag_dict = blockchain_block_dto_e_tag_instance.to_dict()
# create an instance of BlockchainBlockDtoETag from a dict
blockchain_block_dto_e_tag_from_dict = BlockchainBlockDtoETag.from_dict(blockchain_block_dto_e_tag_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


