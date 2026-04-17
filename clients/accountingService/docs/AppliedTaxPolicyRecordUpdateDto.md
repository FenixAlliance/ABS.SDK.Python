# AppliedTaxPolicyRecordUpdateDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tax_policy_id** | **str** |  | [optional] 
**invoice_id** | **str** |  | [optional] 
**item_id** | **str** |  | [optional] 
**tax_amount_in_usd** | **float** |  | [optional] 
**tax_base_amount_in_usd** | **float** |  | [optional] 

## Example

```python
from openapi_client.models.applied_tax_policy_record_update_dto import AppliedTaxPolicyRecordUpdateDto

# TODO update the JSON string below
json = "{}"
# create an instance of AppliedTaxPolicyRecordUpdateDto from a JSON string
applied_tax_policy_record_update_dto_instance = AppliedTaxPolicyRecordUpdateDto.from_json(json)
# print the JSON string representation of the object
print(AppliedTaxPolicyRecordUpdateDto.to_json())

# convert the object into a dict
applied_tax_policy_record_update_dto_dict = applied_tax_policy_record_update_dto_instance.to_dict()
# create an instance of AppliedTaxPolicyRecordUpdateDto from a dict
applied_tax_policy_record_update_dto_from_dict = AppliedTaxPolicyRecordUpdateDto.from_dict(applied_tax_policy_record_update_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


