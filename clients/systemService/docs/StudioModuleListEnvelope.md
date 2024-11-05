# StudioModuleListEnvelope


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_success** | **bool** |  | [optional] [readonly] 
**error_message** | **str** |  | [optional] 
**correlation_id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] [readonly] 
**activity_id** | **str** |  | [optional] [readonly] 
**result** | [**List[StudioModule]**](StudioModule.md) |  | [optional] 

## Example

```python
from openapi_client.models.studio_module_list_envelope import StudioModuleListEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of StudioModuleListEnvelope from a JSON string
studio_module_list_envelope_instance = StudioModuleListEnvelope.from_json(json)
# print the JSON string representation of the object
print(StudioModuleListEnvelope.to_json())

# convert the object into a dict
studio_module_list_envelope_dict = studio_module_list_envelope_instance.to_dict()
# create an instance of StudioModuleListEnvelope from a dict
studio_module_list_envelope_from_dict = StudioModuleListEnvelope.from_dict(studio_module_list_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


