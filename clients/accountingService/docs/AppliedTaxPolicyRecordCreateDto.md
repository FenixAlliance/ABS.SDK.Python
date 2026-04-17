# AppliedTaxPolicyRecordCreateDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] 
**tax_policy_id** | **str** |  | [optional] 
**invoice_id** | **str** |  | [optional] 
**item_id** | **str** |  | [optional] 
**tax_amount_in_usd** | **float** |  | [optional] 
**tax_base_amount_in_usd** | **float** |  | [optional] 

## Example

```python
from openapi_client.models.applied_tax_policy_record_create_dto import AppliedTaxPolicyRecordCreateDto

# TODO update the JSON string below
json = "{}"
# create an instance of AppliedTaxPolicyRecordCreateDto from a JSON string
applied_tax_policy_record_create_dto_instance = AppliedTaxPolicyRecordCreateDto.from_json(json)
# print the JSON string representation of the object
print(AppliedTaxPolicyRecordCreateDto.to_json())

# convert the object into a dict
applied_tax_policy_record_create_dto_dict = applied_tax_policy_record_create_dto_instance.to_dict()
# create an instance of AppliedTaxPolicyRecordCreateDto from a dict
applied_tax_policy_record_create_dto_from_dict = AppliedTaxPolicyRecordCreateDto.from_dict(applied_tax_policy_record_create_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


