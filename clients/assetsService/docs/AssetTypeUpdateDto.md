# AssetTypeUpdateDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**description** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.asset_type_update_dto import AssetTypeUpdateDto

# TODO update the JSON string below
json = "{}"
# create an instance of AssetTypeUpdateDto from a JSON string
asset_type_update_dto_instance = AssetTypeUpdateDto.from_json(json)
# print the JSON string representation of the object
print(AssetTypeUpdateDto.to_json())

# convert the object into a dict
asset_type_update_dto_dict = asset_type_update_dto_instance.to_dict()
# create an instance of AssetTypeUpdateDto from a dict
asset_type_update_dto_from_dict = AssetTypeUpdateDto.from_dict(asset_type_update_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


