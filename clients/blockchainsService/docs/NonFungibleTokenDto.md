# NonFungibleTokenDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] 
**title** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**summary** | **str** |  | [optional] 
**price** | **float** |  | [optional] 
**currency_id** | **str** |  | [optional] 
**published** | **bool** |  | [optional] 
**minted** | **bool** |  | [optional] 
**blockchain_id** | **str** |  | [optional] 
**blockchain_name** | **str** |  | [optional] 
**minted_timestamp** | **datetime** |  | [optional] 
**mint_transaction_hash** | **str** |  | [optional] 
**blockchain_block_id** | **str** |  | [optional] 
**primary_image_url** | **str** |  | [optional] 
**cover_url** | **str** |  | [optional] 
**tenant_id** | **str** |  | [optional] 
**enrollment_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.non_fungible_token_dto import NonFungibleTokenDto

# TODO update the JSON string below
json = "{}"
# create an instance of NonFungibleTokenDto from a JSON string
non_fungible_token_dto_instance = NonFungibleTokenDto.from_json(json)
# print the JSON string representation of the object
print(NonFungibleTokenDto.to_json())

# convert the object into a dict
non_fungible_token_dto_dict = non_fungible_token_dto_instance.to_dict()
# create an instance of NonFungibleTokenDto from a dict
non_fungible_token_dto_from_dict = NonFungibleTokenDto.from_dict(non_fungible_token_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


