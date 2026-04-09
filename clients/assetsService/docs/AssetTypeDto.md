# AssetTypeDto


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
from openapi_client.models.asset_type_dto import AssetTypeDto

# TODO update the JSON string below
json = "{}"
# create an instance of AssetTypeDto from a JSON string
asset_type_dto_instance = AssetTypeDto.from_json(json)
# print the JSON string representation of the object
print(AssetTypeDto.to_json())

# convert the object into a dict
asset_type_dto_dict = asset_type_dto_instance.to_dict()
# create an instance of AssetTypeDto from a dict
asset_type_dto_from_dict = AssetTypeDto.from_dict(asset_type_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


