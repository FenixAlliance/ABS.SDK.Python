# StoreDtoEnvelope


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_success** | **bool** |  | [optional] [readonly] 
**error_message** | **str** |  | [optional] 
**correlation_id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] [readonly] 
**activity_id** | **str** |  | [optional] [readonly] 
**result** | [**StoreDto**](StoreDto.md) |  | [optional] 

## Example

```python
from openapi_client.models.store_dto_envelope import StoreDtoEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of StoreDtoEnvelope from a JSON string
store_dto_envelope_instance = StoreDtoEnvelope.from_json(json)
# print the JSON string representation of the object
print(StoreDtoEnvelope.to_json())

# convert the object into a dict
store_dto_envelope_dict = store_dto_envelope_instance.to_dict()
# create an instance of StoreDtoEnvelope from a dict
store_dto_envelope_from_dict = StoreDtoEnvelope.from_dict(store_dto_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


