# StringEnvelope


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_success** | **bool** |  | [optional] [readonly] 
**error_message** | **str** |  | [optional] 
**correlation_id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] [readonly] 
**activity_id** | **str** |  | [optional] [readonly] 
**result** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.string_envelope import StringEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of StringEnvelope from a JSON string
string_envelope_instance = StringEnvelope.from_json(json)
# print the JSON string representation of the object
print(StringEnvelope.to_json())

# convert the object into a dict
string_envelope_dict = string_envelope_instance.to_dict()
# create an instance of StringEnvelope from a dict
string_envelope_from_dict = StringEnvelope.from_dict(string_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


