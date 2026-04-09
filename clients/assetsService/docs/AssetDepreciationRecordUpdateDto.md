# AssetDepreciationRecordUpdateDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**depreciation_amount** | **float** |  | [optional] 
**accumulated_depreciation** | **float** |  | [optional] 
**book_value** | **float** |  | [optional] 
**depreciation_date** | **datetime** |  | [optional] 
**year** | **int** |  | [optional] 
**month** | **int** |  | [optional] 

## Example

```python
from openapi_client.models.asset_depreciation_record_update_dto import AssetDepreciationRecordUpdateDto

# TODO update the JSON string below
json = "{}"
# create an instance of AssetDepreciationRecordUpdateDto from a JSON string
asset_depreciation_record_update_dto_instance = AssetDepreciationRecordUpdateDto.from_json(json)
# print the JSON string representation of the object
print(AssetDepreciationRecordUpdateDto.to_json())

# convert the object into a dict
asset_depreciation_record_update_dto_dict = asset_depreciation_record_update_dto_instance.to_dict()
# create an instance of AssetDepreciationRecordUpdateDto from a dict
asset_depreciation_record_update_dto_from_dict = AssetDepreciationRecordUpdateDto.from_dict(asset_depreciation_record_update_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


