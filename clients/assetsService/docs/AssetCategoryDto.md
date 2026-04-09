# AssetCategoryDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] 
**tenant_id** | **str** |  | [optional] 
**business_name** | **str** |  | [optional] 
**enrollment_id** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**asset_count** | **int** |  | [optional] 

## Example

```python
from openapi_client.models.asset_category_dto import AssetCategoryDto

# TODO update the JSON string below
json = "{}"
# create an instance of AssetCategoryDto from a JSON string
asset_category_dto_instance = AssetCategoryDto.from_json(json)
# print the JSON string representation of the object
print(AssetCategoryDto.to_json())

# convert the object into a dict
asset_category_dto_dict = asset_category_dto_instance.to_dict()
# create an instance of AssetCategoryDto from a dict
asset_category_dto_from_dict = AssetCategoryDto.from_dict(asset_category_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


