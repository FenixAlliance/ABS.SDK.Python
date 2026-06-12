# ItemBundleDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] 
**name** | **str** |  | [optional] 
**code** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**disabled** | **bool** |  | [optional] 
**tenant_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.item_bundle_dto import ItemBundleDto

# TODO update the JSON string below
json = "{}"
# create an instance of ItemBundleDto from a JSON string
item_bundle_dto_instance = ItemBundleDto.from_json(json)
# print the JSON string representation of the object
print(ItemBundleDto.to_json())

# convert the object into a dict
item_bundle_dto_dict = item_bundle_dto_instance.to_dict()
# create an instance of ItemBundleDto from a dict
item_bundle_dto_from_dict = ItemBundleDto.from_dict(item_bundle_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


