# AssetDepreciationRecordDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **object** |  | [optional] 
**timestamp** | **datetime** |  | [optional] 
**business_id** | **object** |  | [optional] 
**business_profile_record_id** | **object** |  | [optional] 
**asset_id** | **object** |  | [optional] 
**asset_name** | **str** |  | [optional] 
**asset_depreciation_policy_id** | **str** |  | [optional] 
**asset_depreciation_policy_name** | **str** |  | [optional] 
**depreciation_amount** | **float** |  | [optional] 
**accumulated_depreciation** | **float** |  | [optional] 
**book_value** | **float** |  | [optional] 
**depreciation_date** | **datetime** |  | [optional] 
**year** | **int** |  | [optional] 
**month** | **int** |  | [optional] 
**period** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.asset_depreciation_record_dto import AssetDepreciationRecordDto

# TODO update the JSON string below
json = "{}"
# create an instance of AssetDepreciationRecordDto from a JSON string
asset_depreciation_record_dto_instance = AssetDepreciationRecordDto.from_json(json)
# print the JSON string representation of the object
print(AssetDepreciationRecordDto.to_json())

# convert the object into a dict
asset_depreciation_record_dto_dict = asset_depreciation_record_dto_instance.to_dict()
# create an instance of AssetDepreciationRecordDto from a dict
asset_depreciation_record_dto_from_dict = AssetDepreciationRecordDto.from_dict(asset_depreciation_record_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


