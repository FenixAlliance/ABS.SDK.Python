# NonFungibleTokenDtoListEnvelope


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_success** | **bool** |  | [optional] [readonly] 
**error_message** | **str** |  | [optional] 
**correlation_id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] [readonly] 
**activity_id** | **str** |  | [optional] [readonly] 
**result** | [**List[NonFungibleTokenDto]**](NonFungibleTokenDto.md) |  | [optional] 

## Example

```python
from openapi_client.models.non_fungible_token_dto_list_envelope import NonFungibleTokenDtoListEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of NonFungibleTokenDtoListEnvelope from a JSON string
non_fungible_token_dto_list_envelope_instance = NonFungibleTokenDtoListEnvelope.from_json(json)
# print the JSON string representation of the object
print(NonFungibleTokenDtoListEnvelope.to_json())

# convert the object into a dict
non_fungible_token_dto_list_envelope_dict = non_fungible_token_dto_list_envelope_instance.to_dict()
# create an instance of NonFungibleTokenDtoListEnvelope from a dict
non_fungible_token_dto_list_envelope_from_dict = NonFungibleTokenDtoListEnvelope.from_dict(non_fungible_token_dto_list_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


