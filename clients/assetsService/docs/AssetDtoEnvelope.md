# AssetDtoEnvelope


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_success** | **bool** |  | [optional] [readonly] 
**error_message** | **str** |  | [optional] 
**correlation_id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] [readonly] 
**activity_id** | **str** |  | [optional] [readonly] 
**result** | [**AssetDto**](AssetDto.md) |  | [optional] 

## Example

```python
from openapi_client.models.asset_dto_envelope import AssetDtoEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of AssetDtoEnvelope from a JSON string
asset_dto_envelope_instance = AssetDtoEnvelope.from_json(json)
# print the JSON string representation of the object
print(AssetDtoEnvelope.to_json())

# convert the object into a dict
asset_dto_envelope_dict = asset_dto_envelope_instance.to_dict()
# create an instance of AssetDtoEnvelope from a dict
asset_dto_envelope_from_dict = AssetDtoEnvelope.from_dict(asset_dto_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


