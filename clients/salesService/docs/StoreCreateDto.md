# StoreCreateDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] 
**name** | **str** |  | 
**e_commerce** | **bool** |  | [optional] 
**currency_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.store_create_dto import StoreCreateDto

# TODO update the JSON string below
json = "{}"
# create an instance of StoreCreateDto from a JSON string
store_create_dto_instance = StoreCreateDto.from_json(json)
# print the JSON string representation of the object
print(StoreCreateDto.to_json())

# convert the object into a dict
store_create_dto_dict = store_create_dto_instance.to_dict()
# create an instance of StoreCreateDto from a dict
store_create_dto_from_dict = StoreCreateDto.from_dict(store_create_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


