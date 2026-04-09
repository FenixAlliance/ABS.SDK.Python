# AssetDepreciationRecordCreateDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**asset_id** | **str** |  | [optional] 
**asset_depreciation_policy_id** | **str** |  | [optional] 
**depreciation_amount** | **float** |  | [optional] 
**accumulated_depreciation** | **float** |  | [optional] 
**book_value** | **float** |  | [optional] 
**depreciation_date** | **datetime** |  | [optional] 
**year** | **int** |  | [optional] 
**month** | **int** |  | [optional] 

## Example

```python
from openapi_client.models.asset_depreciation_record_create_dto import AssetDepreciationRecordCreateDto

# TODO update the JSON string below
json = "{}"
# create an instance of AssetDepreciationRecordCreateDto from a JSON string
asset_depreciation_record_create_dto_instance = AssetDepreciationRecordCreateDto.from_json(json)
# print the JSON string representation of the object
print(AssetDepreciationRecordCreateDto.to_json())

# convert the object into a dict
asset_depreciation_record_create_dto_dict = asset_depreciation_record_create_dto_instance.to_dict()
# create an instance of AssetDepreciationRecordCreateDto from a dict
asset_depreciation_record_create_dto_from_dict = AssetDepreciationRecordCreateDto.from_dict(asset_depreciation_record_create_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


