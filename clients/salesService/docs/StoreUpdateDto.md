# StoreUpdateDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**e_commerce** | **bool** |  | [optional] 
**currency_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.store_update_dto import StoreUpdateDto

# TODO update the JSON string below
json = "{}"
# create an instance of StoreUpdateDto from a JSON string
store_update_dto_instance = StoreUpdateDto.from_json(json)
# print the JSON string representation of the object
print(StoreUpdateDto.to_json())

# convert the object into a dict
store_update_dto_dict = store_update_dto_instance.to_dict()
# create an instance of StoreUpdateDto from a dict
store_update_dto_from_dict = StoreUpdateDto.from_dict(store_update_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


