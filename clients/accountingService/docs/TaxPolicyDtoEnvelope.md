# TaxPolicyDtoEnvelope


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_success** | **bool** |  | [optional] [readonly] 
**error_message** | **str** |  | [optional] 
**correlation_id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] [readonly] 
**activity_id** | **str** |  | [optional] [readonly] 
**result** | [**TaxPolicyDto**](TaxPolicyDto.md) |  | [optional] 

## Example

```python
from openapi_client.models.tax_policy_dto_envelope import TaxPolicyDtoEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of TaxPolicyDtoEnvelope from a JSON string
tax_policy_dto_envelope_instance = TaxPolicyDtoEnvelope.from_json(json)
# print the JSON string representation of the object
print(TaxPolicyDtoEnvelope.to_json())

# convert the object into a dict
tax_policy_dto_envelope_dict = tax_policy_dto_envelope_instance.to_dict()
# create an instance of TaxPolicyDtoEnvelope from a dict
tax_policy_dto_envelope_from_dict = TaxPolicyDtoEnvelope.from_dict(tax_policy_dto_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


