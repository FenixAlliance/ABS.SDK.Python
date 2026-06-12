# NonFungibleTokenUpdateDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**summary** | **str** |  | [optional] 
**price** | **float** |  | [optional] 
**currency_id** | **str** |  | [optional] 
**published** | **bool** |  | [optional] 
**minted** | **bool** |  | [optional] 
**mint_transaction_hash** | **str** |  | [optional] 
**blockchain_block_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.non_fungible_token_update_dto import NonFungibleTokenUpdateDto

# TODO update the JSON string below
json = "{}"
# create an instance of NonFungibleTokenUpdateDto from a JSON string
non_fungible_token_update_dto_instance = NonFungibleTokenUpdateDto.from_json(json)
# print the JSON string representation of the object
print(NonFungibleTokenUpdateDto.to_json())

# convert the object into a dict
non_fungible_token_update_dto_dict = non_fungible_token_update_dto_instance.to_dict()
# create an instance of NonFungibleTokenUpdateDto from a dict
non_fungible_token_update_dto_from_dict = NonFungibleTokenUpdateDto.from_dict(non_fungible_token_update_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


