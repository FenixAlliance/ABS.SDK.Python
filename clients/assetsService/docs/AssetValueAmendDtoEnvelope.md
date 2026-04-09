# AssetValueAmendDtoEnvelope


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_success** | **bool** |  | [optional] [readonly] 
**error_message** | **str** |  | [optional] 
**correlation_id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] [readonly] 
**activity_id** | **str** |  | [optional] [readonly] 
**result** | [**AssetValueAmendDto**](AssetValueAmendDto.md) |  | [optional] 

## Example

```python
from openapi_client.models.asset_value_amend_dto_envelope import AssetValueAmendDtoEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of AssetValueAmendDtoEnvelope from a JSON string
asset_value_amend_dto_envelope_instance = AssetValueAmendDtoEnvelope.from_json(json)
# print the JSON string representation of the object
print(AssetValueAmendDtoEnvelope.to_json())

# convert the object into a dict
asset_value_amend_dto_envelope_dict = asset_value_amend_dto_envelope_instance.to_dict()
# create an instance of AssetValueAmendDtoEnvelope from a dict
asset_value_amend_dto_envelope_from_dict = AssetValueAmendDtoEnvelope.from_dict(asset_value_amend_dto_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


