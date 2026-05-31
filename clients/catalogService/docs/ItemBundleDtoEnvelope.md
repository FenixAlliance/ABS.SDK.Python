# ItemBundleDtoEnvelope


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_success** | **bool** |  | [optional] [readonly] 
**error_message** | **str** |  | [optional] 
**correlation_id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] [readonly] 
**activity_id** | **str** |  | [optional] [readonly] 
**result** | [**ItemBundleDto**](ItemBundleDto.md) |  | [optional] 

## Example

```python
from openapi_client.models.item_bundle_dto_envelope import ItemBundleDtoEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of ItemBundleDtoEnvelope from a JSON string
item_bundle_dto_envelope_instance = ItemBundleDtoEnvelope.from_json(json)
# print the JSON string representation of the object
print(ItemBundleDtoEnvelope.to_json())

# convert the object into a dict
item_bundle_dto_envelope_dict = item_bundle_dto_envelope_instance.to_dict()
# create an instance of ItemBundleDtoEnvelope from a dict
item_bundle_dto_envelope_from_dict = ItemBundleDtoEnvelope.from_dict(item_bundle_dto_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


