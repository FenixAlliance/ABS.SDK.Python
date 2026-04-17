# AssetCategoryCreateDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] 
**name** | **str** |  | [optional] 
**description** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.asset_category_create_dto import AssetCategoryCreateDto

# TODO update the JSON string below
json = "{}"
# create an instance of AssetCategoryCreateDto from a JSON string
asset_category_create_dto_instance = AssetCategoryCreateDto.from_json(json)
# print the JSON string representation of the object
print(AssetCategoryCreateDto.to_json())

# convert the object into a dict
asset_category_create_dto_dict = asset_category_create_dto_instance.to_dict()
# create an instance of AssetCategoryCreateDto from a dict
asset_category_create_dto_from_dict = AssetCategoryCreateDto.from_dict(asset_category_create_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


