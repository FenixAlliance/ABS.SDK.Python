# AssetDepreciationRecordDtoEnvelope


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_success** | **bool** |  | [optional] [readonly] 
**error_message** | **str** |  | [optional] 
**correlation_id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] [readonly] 
**activity_id** | **str** |  | [optional] [readonly] 
**result** | [**AssetDepreciationRecordDto**](AssetDepreciationRecordDto.md) |  | [optional] 

## Example

```python
from openapi_client.models.asset_depreciation_record_dto_envelope import AssetDepreciationRecordDtoEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of AssetDepreciationRecordDtoEnvelope from a JSON string
asset_depreciation_record_dto_envelope_instance = AssetDepreciationRecordDtoEnvelope.from_json(json)
# print the JSON string representation of the object
print(AssetDepreciationRecordDtoEnvelope.to_json())

# convert the object into a dict
asset_depreciation_record_dto_envelope_dict = asset_depreciation_record_dto_envelope_instance.to_dict()
# create an instance of AssetDepreciationRecordDtoEnvelope from a dict
asset_depreciation_record_dto_envelope_from_dict = AssetDepreciationRecordDtoEnvelope.from_dict(asset_depreciation_record_dto_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


