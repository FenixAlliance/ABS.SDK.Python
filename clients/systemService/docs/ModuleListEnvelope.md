# ModuleListEnvelope


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_success** | **bool** |  | [optional] [readonly] 
**error_message** | **str** |  | [optional] 
**correlation_id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] [readonly] 
**activity_id** | **str** |  | [optional] [readonly] 
**result** | [**List[Module]**](Module.md) |  | [optional] 

## Example

```python
from openapi_client.models.module_list_envelope import ModuleListEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of ModuleListEnvelope from a JSON string
module_list_envelope_instance = ModuleListEnvelope.from_json(json)
# print the JSON string representation of the object
print(ModuleListEnvelope.to_json())

# convert the object into a dict
module_list_envelope_dict = module_list_envelope_instance.to_dict()
# create an instance of ModuleListEnvelope from a dict
module_list_envelope_from_dict = ModuleListEnvelope.from_dict(module_list_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


