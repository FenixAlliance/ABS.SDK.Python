# AssetTypeCreateDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] 
**business_id** | **str** |  | [optional] 
**business_profile_record_id** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**description** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.asset_type_create_dto import AssetTypeCreateDto

# TODO update the JSON string below
json = "{}"
# create an instance of AssetTypeCreateDto from a JSON string
asset_type_create_dto_instance = AssetTypeCreateDto.from_json(json)
# print the JSON string representation of the object
print(AssetTypeCreateDto.to_json())

# convert the object into a dict
asset_type_create_dto_dict = asset_type_create_dto_instance.to_dict()
# create an instance of AssetTypeCreateDto from a dict
asset_type_create_dto_from_dict = AssetTypeCreateDto.from_dict(asset_type_create_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


