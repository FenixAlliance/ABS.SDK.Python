# TwoFactorResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**shared_key** | **str** |  | 
**recovery_codes_left** | **int** |  | 
**recovery_codes** | **List[str]** |  | [optional] 
**is_two_factor_enabled** | **bool** |  | 
**is_machine_remembered** | **bool** |  | 

## Example

```python
from openapi_client.models.two_factor_response import TwoFactorResponse

# TODO update the JSON string below
json = "{}"
# create an instance of TwoFactorResponse from a JSON string
two_factor_response_instance = TwoFactorResponse.from_json(json)
# print the JSON string representation of the object
print(TwoFactorResponse.to_json())

# convert the object into a dict
two_factor_response_dict = two_factor_response_instance.to_dict()
# create an instance of TwoFactorResponse from a dict
two_factor_response_from_dict = TwoFactorResponse.from_dict(two_factor_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


