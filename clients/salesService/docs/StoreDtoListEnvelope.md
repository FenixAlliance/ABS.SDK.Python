# StoreDtoListEnvelope


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_success** | **bool** |  | [optional] [readonly] 
**error_message** | **str** |  | [optional] 
**correlation_id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] [readonly] 
**activity_id** | **str** |  | [optional] [readonly] 
**result** | [**List[StoreDto]**](StoreDto.md) |  | [optional] 

## Example

```python
from openapi_client.models.store_dto_list_envelope import StoreDtoListEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of StoreDtoListEnvelope from a JSON string
store_dto_list_envelope_instance = StoreDtoListEnvelope.from_json(json)
# print the JSON string representation of the object
print(StoreDtoListEnvelope.to_json())

# convert the object into a dict
store_dto_list_envelope_dict = store_dto_list_envelope_instance.to_dict()
# create an instance of StoreDtoListEnvelope from a dict
store_dto_list_envelope_from_dict = StoreDtoListEnvelope.from_dict(store_dto_list_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


