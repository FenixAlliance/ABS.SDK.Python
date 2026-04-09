# AssetRepairDtoListEnvelope


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_success** | **bool** |  | [optional] [readonly] 
**error_message** | **str** |  | [optional] 
**correlation_id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] [readonly] 
**activity_id** | **str** |  | [optional] [readonly] 
**result** | [**List[AssetRepairDto]**](AssetRepairDto.md) |  | [optional] 

## Example

```python
from openapi_client.models.asset_repair_dto_list_envelope import AssetRepairDtoListEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of AssetRepairDtoListEnvelope from a JSON string
asset_repair_dto_list_envelope_instance = AssetRepairDtoListEnvelope.from_json(json)
# print the JSON string representation of the object
print(AssetRepairDtoListEnvelope.to_json())

# convert the object into a dict
asset_repair_dto_list_envelope_dict = asset_repair_dto_list_envelope_instance.to_dict()
# create an instance of AssetRepairDtoListEnvelope from a dict
asset_repair_dto_list_envelope_from_dict = AssetRepairDtoListEnvelope.from_dict(asset_repair_dto_list_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


