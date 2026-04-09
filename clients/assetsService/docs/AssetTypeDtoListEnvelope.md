# AssetTypeDtoListEnvelope


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_success** | **bool** |  | [optional] [readonly] 
**error_message** | **str** |  | [optional] 
**correlation_id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] [readonly] 
**activity_id** | **str** |  | [optional] [readonly] 
**result** | [**List[AssetTypeDto]**](AssetTypeDto.md) |  | [optional] 

## Example

```python
from openapi_client.models.asset_type_dto_list_envelope import AssetTypeDtoListEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of AssetTypeDtoListEnvelope from a JSON string
asset_type_dto_list_envelope_instance = AssetTypeDtoListEnvelope.from_json(json)
# print the JSON string representation of the object
print(AssetTypeDtoListEnvelope.to_json())

# convert the object into a dict
asset_type_dto_list_envelope_dict = asset_type_dto_list_envelope_instance.to_dict()
# create an instance of AssetTypeDtoListEnvelope from a dict
asset_type_dto_list_envelope_from_dict = AssetTypeDtoListEnvelope.from_dict(asset_type_dto_list_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


