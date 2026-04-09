# AuthorizationResultEnvelope


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_success** | **bool** |  | [optional] [readonly] 
**error_message** | **str** |  | [optional] 
**correlation_id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] [readonly] 
**activity_id** | **str** |  | [optional] [readonly] 
**result** | [**AuthorizationResult**](AuthorizationResult.md) |  | [optional] 

## Example

```python
from openapi_client.models.authorization_result_envelope import AuthorizationResultEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of AuthorizationResultEnvelope from a JSON string
authorization_result_envelope_instance = AuthorizationResultEnvelope.from_json(json)
# print the JSON string representation of the object
print(AuthorizationResultEnvelope.to_json())

# convert the object into a dict
authorization_result_envelope_dict = authorization_result_envelope_instance.to_dict()
# create an instance of AuthorizationResultEnvelope from a dict
authorization_result_envelope_from_dict = AuthorizationResultEnvelope.from_dict(authorization_result_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


