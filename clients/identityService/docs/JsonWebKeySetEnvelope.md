# JsonWebKeySetEnvelope


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_success** | **bool** |  | [optional] [readonly] 
**error_message** | **str** |  | [optional] 
**correlation_id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] [readonly] 
**activity_id** | **str** |  | [optional] [readonly] 
**result** | [**JsonWebKeySet**](JsonWebKeySet.md) |  | [optional] 

## Example

```python
from openapi_client.models.json_web_key_set_envelope import JsonWebKeySetEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of JsonWebKeySetEnvelope from a JSON string
json_web_key_set_envelope_instance = JsonWebKeySetEnvelope.from_json(json)
# print the JSON string representation of the object
print(JsonWebKeySetEnvelope.to_json())

# convert the object into a dict
json_web_key_set_envelope_dict = json_web_key_set_envelope_instance.to_dict()
# create an instance of JsonWebKeySetEnvelope from a dict
json_web_key_set_envelope_from_dict = JsonWebKeySetEnvelope.from_dict(json_web_key_set_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


