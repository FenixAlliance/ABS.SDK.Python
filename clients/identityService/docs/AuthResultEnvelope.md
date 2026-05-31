# AuthResultEnvelope


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_success** | **bool** |  | [optional] [readonly] 
**error_message** | **str** |  | [optional] 
**correlation_id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] [readonly] 
**activity_id** | **str** |  | [optional] [readonly] 
**result** | [**AuthResult**](AuthResult.md) |  | [optional] 

## Example

```python
from openapi_client.models.auth_result_envelope import AuthResultEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of AuthResultEnvelope from a JSON string
auth_result_envelope_instance = AuthResultEnvelope.from_json(json)
# print the JSON string representation of the object
print(AuthResultEnvelope.to_json())

# convert the object into a dict
auth_result_envelope_dict = auth_result_envelope_instance.to_dict()
# create an instance of AuthResultEnvelope from a dict
auth_result_envelope_from_dict = AuthResultEnvelope.from_dict(auth_result_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


