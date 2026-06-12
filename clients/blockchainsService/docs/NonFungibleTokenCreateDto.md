# NonFungibleTokenCreateDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] 
**title** | **str** |  | 
**description** | **str** |  | 
**summary** | **str** |  | [optional] 
**price** | **float** |  | [optional] 
**currency_id** | **str** |  | [optional] 
**blockchain_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.non_fungible_token_create_dto import NonFungibleTokenCreateDto

# TODO update the JSON string below
json = "{}"
# create an instance of NonFungibleTokenCreateDto from a JSON string
non_fungible_token_create_dto_instance = NonFungibleTokenCreateDto.from_json(json)
# print the JSON string representation of the object
print(NonFungibleTokenCreateDto.to_json())

# convert the object into a dict
non_fungible_token_create_dto_dict = non_fungible_token_create_dto_instance.to_dict()
# create an instance of NonFungibleTokenCreateDto from a dict
non_fungible_token_create_dto_from_dict = NonFungibleTokenCreateDto.from_dict(non_fungible_token_create_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


