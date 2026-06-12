# ClaimsIdentity


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**authentication_type** | **str** |  | [optional] [readonly] 
**is_authenticated** | **bool** |  | [optional] [readonly] 
**actor** | [**ClaimsIdentity**](ClaimsIdentity.md) |  | [optional] 
**bootstrap_context** | **object** |  | [optional] 
**claims** | [**List[Claim]**](Claim.md) |  | [optional] [readonly] 
**label** | **str** |  | [optional] 
**name** | **str** |  | [optional] [readonly] 
**name_claim_type** | **str** |  | [optional] [readonly] 
**role_claim_type** | **str** |  | [optional] [readonly] 

## Example

```python
from openapi_client.models.claims_identity import ClaimsIdentity

# TODO update the JSON string below
json = "{}"
# create an instance of ClaimsIdentity from a JSON string
claims_identity_instance = ClaimsIdentity.from_json(json)
# print the JSON string representation of the object
print(ClaimsIdentity.to_json())

# convert the object into a dict
claims_identity_dict = claims_identity_instance.to_dict()
# create an instance of ClaimsIdentity from a dict
claims_identity_from_dict = ClaimsIdentity.from_dict(claims_identity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


