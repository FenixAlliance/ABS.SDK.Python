# ItemBrandUpdateDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**description** | **str** |  | [optional] 
**website_url** | **str** |  | [optional] 
**logo_url** | **str** |  | [optional] 
**featured** | **bool** |  | [optional] 
**trending** | **bool** |  | [optional] 

## Example

```python
from openapi_client.models.item_brand_update_dto import ItemBrandUpdateDto

# TODO update the JSON string below
json = "{}"
# create an instance of ItemBrandUpdateDto from a JSON string
item_brand_update_dto_instance = ItemBrandUpdateDto.from_json(json)
# print the JSON string representation of the object
print(ItemBrandUpdateDto.to_json())

# convert the object into a dict
item_brand_update_dto_dict = item_brand_update_dto_instance.to_dict()
# create an instance of ItemBrandUpdateDto from a dict
item_brand_update_dto_from_dict = ItemBrandUpdateDto.from_dict(item_brand_update_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


