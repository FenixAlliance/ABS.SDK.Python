# AssetCategoryUpdateDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**description** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.asset_category_update_dto import AssetCategoryUpdateDto

# TODO update the JSON string below
json = "{}"
# create an instance of AssetCategoryUpdateDto from a JSON string
asset_category_update_dto_instance = AssetCategoryUpdateDto.from_json(json)
# print the JSON string representation of the object
print(AssetCategoryUpdateDto.to_json())

# convert the object into a dict
asset_category_update_dto_dict = asset_category_update_dto_instance.to_dict()
# create an instance of AssetCategoryUpdateDto from a dict
asset_category_update_dto_from_dict = AssetCategoryUpdateDto.from_dict(asset_category_update_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


