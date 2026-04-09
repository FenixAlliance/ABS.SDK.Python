# AppliedTaxPolicyRecordDtoEnvelope


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_success** | **bool** |  | [optional] [readonly] 
**error_message** | **str** |  | [optional] 
**correlation_id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] [readonly] 
**activity_id** | **str** |  | [optional] [readonly] 
**result** | [**AppliedTaxPolicyRecordDto**](AppliedTaxPolicyRecordDto.md) |  | [optional] 

## Example

```python
from openapi_client.models.applied_tax_policy_record_dto_envelope import AppliedTaxPolicyRecordDtoEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of AppliedTaxPolicyRecordDtoEnvelope from a JSON string
applied_tax_policy_record_dto_envelope_instance = AppliedTaxPolicyRecordDtoEnvelope.from_json(json)
# print the JSON string representation of the object
print(AppliedTaxPolicyRecordDtoEnvelope.to_json())

# convert the object into a dict
applied_tax_policy_record_dto_envelope_dict = applied_tax_policy_record_dto_envelope_instance.to_dict()
# create an instance of AppliedTaxPolicyRecordDtoEnvelope from a dict
applied_tax_policy_record_dto_envelope_from_dict = AppliedTaxPolicyRecordDtoEnvelope.from_dict(applied_tax_policy_record_dto_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


