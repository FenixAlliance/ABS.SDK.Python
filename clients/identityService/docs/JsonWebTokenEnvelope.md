# JsonWebTokenEnvelope


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_success** | **bool** |  | [optional] [readonly] 
**error_message** | **str** |  | [optional] 
**correlation_id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] [readonly] 
**activity_id** | **str** |  | [optional] [readonly] 
**result** | [**JsonWebToken**](JsonWebToken.md) |  | [optional] 

## Example

```python
from openapi_client.models.json_web_token_envelope import JsonWebTokenEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of JsonWebTokenEnvelope from a JSON string
json_web_token_envelope_instance = JsonWebTokenEnvelope.from_json(json)
# print the JSON string representation of the object
print(JsonWebTokenEnvelope.to_json())

# convert the object into a dict
json_web_token_envelope_dict = json_web_token_envelope_instance.to_dict()
# create an instance of JsonWebTokenEnvelope from a dict
json_web_token_envelope_from_dict = JsonWebTokenEnvelope.from_dict(json_web_token_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


