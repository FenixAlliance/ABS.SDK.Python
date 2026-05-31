# ItemBundleUpdateDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**code** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**disabled** | **bool** |  | [optional] 

## Example

```python
from openapi_client.models.item_bundle_update_dto import ItemBundleUpdateDto

# TODO update the JSON string below
json = "{}"
# create an instance of ItemBundleUpdateDto from a JSON string
item_bundle_update_dto_instance = ItemBundleUpdateDto.from_json(json)
# print the JSON string representation of the object
print(ItemBundleUpdateDto.to_json())

# convert the object into a dict
item_bundle_update_dto_dict = item_bundle_update_dto_instance.to_dict()
# create an instance of ItemBundleUpdateDto from a dict
item_bundle_update_dto_from_dict = ItemBundleUpdateDto.from_dict(item_bundle_update_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


