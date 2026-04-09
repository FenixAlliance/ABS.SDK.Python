# AppliedTaxPolicyRecordDtoListEnvelope


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_success** | **bool** |  | [optional] [readonly] 
**error_message** | **str** |  | [optional] 
**correlation_id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] [readonly] 
**activity_id** | **str** |  | [optional] [readonly] 
**result** | [**List[AppliedTaxPolicyRecordDto]**](AppliedTaxPolicyRecordDto.md) |  | [optional] 

## Example

```python
from openapi_client.models.applied_tax_policy_record_dto_list_envelope import AppliedTaxPolicyRecordDtoListEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of AppliedTaxPolicyRecordDtoListEnvelope from a JSON string
applied_tax_policy_record_dto_list_envelope_instance = AppliedTaxPolicyRecordDtoListEnvelope.from_json(json)
# print the JSON string representation of the object
print(AppliedTaxPolicyRecordDtoListEnvelope.to_json())

# convert the object into a dict
applied_tax_policy_record_dto_list_envelope_dict = applied_tax_policy_record_dto_list_envelope_instance.to_dict()
# create an instance of AppliedTaxPolicyRecordDtoListEnvelope from a dict
applied_tax_policy_record_dto_list_envelope_from_dict = AppliedTaxPolicyRecordDtoListEnvelope.from_dict(applied_tax_policy_record_dto_list_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


