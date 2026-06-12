# BlockchainCreateDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] 
**name** | **str** |  | 
**logo_url** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**difficulty** | **int** |  | [optional] 

## Example

```python
from openapi_client.models.blockchain_create_dto import BlockchainCreateDto

# TODO update the JSON string below
json = "{}"
# create an instance of BlockchainCreateDto from a JSON string
blockchain_create_dto_instance = BlockchainCreateDto.from_json(json)
# print the JSON string representation of the object
print(BlockchainCreateDto.to_json())

# convert the object into a dict
blockchain_create_dto_dict = blockchain_create_dto_instance.to_dict()
# create an instance of BlockchainCreateDto from a dict
blockchain_create_dto_from_dict = BlockchainCreateDto.from_dict(blockchain_create_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


