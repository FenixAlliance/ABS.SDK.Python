# Claim


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**issuer** | **str** |  | [optional] [readonly] 
**original_issuer** | **str** |  | [optional] [readonly] 
**properties** | **Dict[str, str]** |  | [optional] [readonly] 
**subject** | [**ClaimsIdentity**](ClaimsIdentity.md) |  | [optional] 
**type** | **str** |  | [optional] [readonly] 
**value** | **str** |  | [optional] [readonly] 
**value_type** | **str** |  | [optional] [readonly] 

## Example

```python
from openapi_client.models.claim import Claim

# TODO update the JSON string below
json = "{}"
# create an instance of Claim from a JSON string
claim_instance = Claim.from_json(json)
# print the JSON string representation of the object
print(Claim.to_json())

# convert the object into a dict
claim_dict = claim_instance.to_dict()
# create an instance of Claim from a dict
claim_from_dict = Claim.from_dict(claim_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


