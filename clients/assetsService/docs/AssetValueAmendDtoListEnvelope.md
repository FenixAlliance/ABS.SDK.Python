# AssetValueAmendDtoListEnvelope


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_success** | **bool** |  | [optional] [readonly] 
**error_message** | **str** |  | [optional] 
**correlation_id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] [readonly] 
**activity_id** | **str** |  | [optional] [readonly] 
**result** | [**List[AssetValueAmendDto]**](AssetValueAmendDto.md) |  | [optional] 

## Example

```python
from openapi_client.models.asset_value_amend_dto_list_envelope import AssetValueAmendDtoListEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of AssetValueAmendDtoListEnvelope from a JSON string
asset_value_amend_dto_list_envelope_instance = AssetValueAmendDtoListEnvelope.from_json(json)
# print the JSON string representation of the object
print(AssetValueAmendDtoListEnvelope.to_json())

# convert the object into a dict
asset_value_amend_dto_list_envelope_dict = asset_value_amend_dto_list_envelope_instance.to_dict()
# create an instance of AssetValueAmendDtoListEnvelope from a dict
asset_value_amend_dto_list_envelope_from_dict = AssetValueAmendDtoListEnvelope.from_dict(asset_value_amend_dto_list_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


