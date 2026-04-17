# ItemBrandCreateDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] 
**code** | **str** |  | [optional] 
**name** | **str** |  | 
**description** | **str** |  | [optional] 
**website_url** | **str** |  | [optional] 
**featured** | **bool** |  | [optional] 
**trending** | **bool** |  | [optional] 

## Example

```python
from openapi_client.models.item_brand_create_dto import ItemBrandCreateDto

# TODO update the JSON string below
json = "{}"
# create an instance of ItemBrandCreateDto from a JSON string
item_brand_create_dto_instance = ItemBrandCreateDto.from_json(json)
# print the JSON string representation of the object
print(ItemBrandCreateDto.to_json())

# convert the object into a dict
item_brand_create_dto_dict = item_brand_create_dto_instance.to_dict()
# create an instance of ItemBrandCreateDto from a dict
item_brand_create_dto_from_dict = ItemBrandCreateDto.from_dict(item_brand_create_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


