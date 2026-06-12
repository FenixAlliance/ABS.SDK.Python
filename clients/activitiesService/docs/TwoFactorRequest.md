# TwoFactorRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enable** | **bool** |  | [optional] 
**two_factor_code** | **str** |  | [optional] 
**reset_shared_key** | **bool** |  | [optional] 
**reset_recovery_codes** | **bool** |  | [optional] 
**forget_machine** | **bool** |  | [optional] 

## Example

```python
from openapi_client.models.two_factor_request import TwoFactorRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TwoFactorRequest from a JSON string
two_factor_request_instance = TwoFactorRequest.from_json(json)
# print the JSON string representation of the object
print(TwoFactorRequest.to_json())

# convert the object into a dict
two_factor_request_dict = two_factor_request_instance.to_dict()
# create an instance of TwoFactorRequest from a dict
two_factor_request_from_dict = TwoFactorRequest.from_dict(two_factor_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


