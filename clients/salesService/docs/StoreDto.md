# StoreDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] 
**tenant_id** | **str** |  | [optional] 
**enrollment_id** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**e_commerce** | **bool** |  | [optional] 
**currency_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.store_dto import StoreDto

# TODO update the JSON string below
json = "{}"
# create an instance of StoreDto from a JSON string
store_dto_instance = StoreDto.from_json(json)
# print the JSON string representation of the object
print(StoreDto.to_json())

# convert the object into a dict
store_dto_dict = store_dto_instance.to_dict()
# create an instance of StoreDto from a dict
store_dto_from_dict = StoreDto.from_dict(store_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


