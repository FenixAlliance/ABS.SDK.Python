# ClaimsPrincipal


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**claims** | [**List[Claim]**](Claim.md) |  | [optional] [readonly] 
**identities** | [**List[ClaimsIdentity]**](ClaimsIdentity.md) |  | [optional] [readonly] 
**identity** | [**IIdentity**](IIdentity.md) |  | [optional] 

## Example

```python
from openapi_client.models.claims_principal import ClaimsPrincipal

# TODO update the JSON string below
json = "{}"
# create an instance of ClaimsPrincipal from a JSON string
claims_principal_instance = ClaimsPrincipal.from_json(json)
# print the JSON string representation of the object
print(ClaimsPrincipal.to_json())

# convert the object into a dict
claims_principal_dict = claims_principal_instance.to_dict()
# create an instance of ClaimsPrincipal from a dict
claims_principal_from_dict = ClaimsPrincipal.from_dict(claims_principal_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


