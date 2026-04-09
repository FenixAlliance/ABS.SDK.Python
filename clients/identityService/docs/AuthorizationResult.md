# AuthorizationResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_id** | **object** |  | [optional] 
**tenant_id** | **object** |  | [optional] 
**portal_id** | **object** |  | [optional] 
**application_id** | **object** |  | [optional] 
**enrollment_id** | **object** |  | [optional] 
**correlation_id** | **str** |  | [optional] 
**scopes** | **List[str]** |  | [optional] 
**error** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.authorization_result import AuthorizationResult

# TODO update the JSON string below
json = "{}"
# create an instance of AuthorizationResult from a JSON string
authorization_result_instance = AuthorizationResult.from_json(json)
# print the JSON string representation of the object
print(AuthorizationResult.to_json())

# convert the object into a dict
authorization_result_dict = authorization_result_instance.to_dict()
# create an instance of AuthorizationResult from a dict
authorization_result_from_dict = AuthorizationResult.from_dict(authorization_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


