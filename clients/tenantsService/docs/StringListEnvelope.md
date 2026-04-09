# StringListEnvelope


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_success** | **bool** |  | [optional] [readonly] 
**error_message** | **str** |  | [optional] 
**correlation_id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] [readonly] 
**activity_id** | **str** |  | [optional] [readonly] 
**result** | **List[str]** |  | [optional] 

## Example

```python
from openapi_client.models.string_list_envelope import StringListEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of StringListEnvelope from a JSON string
string_list_envelope_instance = StringListEnvelope.from_json(json)
# print the JSON string representation of the object
print(StringListEnvelope.to_json())

# convert the object into a dict
string_list_envelope_dict = string_list_envelope_instance.to_dict()
# create an instance of StringListEnvelope from a dict
string_list_envelope_from_dict = StringListEnvelope.from_dict(string_list_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


