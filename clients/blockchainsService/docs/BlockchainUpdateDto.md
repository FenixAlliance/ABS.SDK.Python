# BlockchainUpdateDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**logo_url** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**difficulty** | **int** |  | [optional] 

## Example

```python
from openapi_client.models.blockchain_update_dto import BlockchainUpdateDto

# TODO update the JSON string below
json = "{}"
# create an instance of BlockchainUpdateDto from a JSON string
blockchain_update_dto_instance = BlockchainUpdateDto.from_json(json)
# print the JSON string representation of the object
print(BlockchainUpdateDto.to_json())

# convert the object into a dict
blockchain_update_dto_dict = blockchain_update_dto_instance.to_dict()
# create an instance of BlockchainUpdateDto from a dict
blockchain_update_dto_from_dict = BlockchainUpdateDto.from_dict(blockchain_update_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


