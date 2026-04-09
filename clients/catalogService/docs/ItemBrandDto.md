# ItemBrandDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] 
**code** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**website_url** | **str** |  | [optional] 
**logo_url** | **str** |  | [optional] 
**featured** | **bool** |  | [optional] 
**trending** | **bool** |  | [optional] 
**business_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.item_brand_dto import ItemBrandDto

# TODO update the JSON string below
json = "{}"
# create an instance of ItemBrandDto from a JSON string
item_brand_dto_instance = ItemBrandDto.from_json(json)
# print the JSON string representation of the object
print(ItemBrandDto.to_json())

# convert the object into a dict
item_brand_dto_dict = item_brand_dto_instance.to_dict()
# create an instance of ItemBrandDto from a dict
item_brand_dto_from_dict = ItemBrandDto.from_dict(item_brand_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


