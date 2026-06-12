# NonFungibleTokenDtoETag


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_well_formed** | **bool** |  | [optional] 
**entity_type** | [**Type**](Type.md) |  | [optional] 
**is_any** | **bool** |  | [optional] 
**is_if_none_match** | **bool** |  | [optional] 

## Example

```python
from openapi_client.models.non_fungible_token_dto_e_tag import NonFungibleTokenDtoETag

# TODO update the JSON string below
json = "{}"
# create an instance of NonFungibleTokenDtoETag from a JSON string
non_fungible_token_dto_e_tag_instance = NonFungibleTokenDtoETag.from_json(json)
# print the JSON string representation of the object
print(NonFungibleTokenDtoETag.to_json())

# convert the object into a dict
non_fungible_token_dto_e_tag_dict = non_fungible_token_dto_e_tag_instance.to_dict()
# create an instance of NonFungibleTokenDtoETag from a dict
non_fungible_token_dto_e_tag_from_dict = NonFungibleTokenDtoETag.from_dict(non_fungible_token_dto_e_tag_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


