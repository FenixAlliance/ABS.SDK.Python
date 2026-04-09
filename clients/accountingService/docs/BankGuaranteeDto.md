# BankGuaranteeDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] 
**margin** | **float** |  | [optional] 
**charges** | **float** |  | [optional] 
**beneficiary_name** | **str** |  | [optional] 
**guarantee_number** | **str** |  | [optional] 
**guarantee_conditions** | **str** |  | [optional] 
**fixed_deposit_number** | **float** |  | [optional] 
**start_date** | **datetime** |  | [optional] 
**end_date** | **datetime** |  | [optional] 
**validity_in_days** | **int** |  | [optional] 
**tenant_id** | **str** |  | [optional] 
**bank_guarantee_type** | **str** |  | [optional] 
**enrollment_id** | **str** |  | [optional] 
**contact_id** | **str** |  | [optional] 
**project_id** | **str** |  | [optional] 
**order_id** | **str** |  | [optional] 
**bank_profile_id** | **str** |  | [optional] 
**bank_account_id** | **str** |  | [optional] 
**currency_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.bank_guarantee_dto import BankGuaranteeDto

# TODO update the JSON string below
json = "{}"
# create an instance of BankGuaranteeDto from a JSON string
bank_guarantee_dto_instance = BankGuaranteeDto.from_json(json)
# print the JSON string representation of the object
print(BankGuaranteeDto.to_json())

# convert the object into a dict
bank_guarantee_dto_dict = bank_guarantee_dto_instance.to_dict()
# create an instance of BankGuaranteeDto from a dict
bank_guarantee_dto_from_dict = BankGuaranteeDto.from_dict(bank_guarantee_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


