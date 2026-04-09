# AssetRepairDtoEnvelope


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_success** | **bool** |  | [optional] [readonly] 
**error_message** | **str** |  | [optional] 
**correlation_id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] [readonly] 
**activity_id** | **str** |  | [optional] [readonly] 
**result** | [**AssetRepairDto**](AssetRepairDto.md) |  | [optional] 

## Example

```python
from openapi_client.models.asset_repair_dto_envelope import AssetRepairDtoEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of AssetRepairDtoEnvelope from a JSON string
asset_repair_dto_envelope_instance = AssetRepairDtoEnvelope.from_json(json)
# print the JSON string representation of the object
print(AssetRepairDtoEnvelope.to_json())

# convert the object into a dict
asset_repair_dto_envelope_dict = asset_repair_dto_envelope_instance.to_dict()
# create an instance of AssetRepairDtoEnvelope from a dict
asset_repair_dto_envelope_from_dict = AssetRepairDtoEnvelope.from_dict(asset_repair_dto_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


