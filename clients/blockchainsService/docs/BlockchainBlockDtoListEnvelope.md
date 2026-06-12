# BlockchainBlockDtoListEnvelope


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_success** | **bool** |  | [optional] [readonly] 
**error_message** | **str** |  | [optional] 
**correlation_id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] [readonly] 
**activity_id** | **str** |  | [optional] [readonly] 
**result** | [**List[BlockchainBlockDto]**](BlockchainBlockDto.md) |  | [optional] 

## Example

```python
from openapi_client.models.blockchain_block_dto_list_envelope import BlockchainBlockDtoListEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of BlockchainBlockDtoListEnvelope from a JSON string
blockchain_block_dto_list_envelope_instance = BlockchainBlockDtoListEnvelope.from_json(json)
# print the JSON string representation of the object
print(BlockchainBlockDtoListEnvelope.to_json())

# convert the object into a dict
blockchain_block_dto_list_envelope_dict = blockchain_block_dto_list_envelope_instance.to_dict()
# create an instance of BlockchainBlockDtoListEnvelope from a dict
blockchain_block_dto_list_envelope_from_dict = BlockchainBlockDtoListEnvelope.from_dict(blockchain_block_dto_list_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


