# WishListDtoEnvelope


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_success** | **bool** |  | [optional] [readonly] 
**error_message** | **str** |  | [optional] 
**correlation_id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] [readonly] 
**activity_id** | **str** |  | [optional] [readonly] 
**result** | [**WishListDto**](WishListDto.md) |  | [optional] 

## Example

```python
from openapi_client.models.wish_list_dto_envelope import WishListDtoEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of WishListDtoEnvelope from a JSON string
wish_list_dto_envelope_instance = WishListDtoEnvelope.from_json(json)
# print the JSON string representation of the object
print(WishListDtoEnvelope.to_json())

# convert the object into a dict
wish_list_dto_envelope_dict = wish_list_dto_envelope_instance.to_dict()
# create an instance of WishListDtoEnvelope from a dict
wish_list_dto_envelope_from_dict = WishListDtoEnvelope.from_dict(wish_list_dto_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


