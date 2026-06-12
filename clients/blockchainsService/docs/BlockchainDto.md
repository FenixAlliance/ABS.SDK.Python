# BlockchainDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] 
**name** | **str** |  | [optional] 
**logo_url** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**difficulty** | **int** |  | [optional] 
**tenant_id** | **str** |  | [optional] 
**enrollment_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.blockchain_dto import BlockchainDto

# TODO update the JSON string below
json = "{}"
# create an instance of BlockchainDto from a JSON string
blockchain_dto_instance = BlockchainDto.from_json(json)
# print the JSON string representation of the object
print(BlockchainDto.to_json())

# convert the object into a dict
blockchain_dto_dict = blockchain_dto_instance.to_dict()
# create an instance of BlockchainDto from a dict
blockchain_dto_from_dict = BlockchainDto.from_dict(blockchain_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


