# SupportEntitlementUpdateDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**end_date_time** | **datetime** |  | [optional] 
**next_invoice_date_time** | **datetime** |  | [optional] 
**code** | **str** |  | [optional] 
**signature** | **str** |  | [optional] 
**quantity** | **int** |  | [optional] 
**repetitions** | **int** |  | [optional] 
**charge_attempts** | **int** |  | [optional] 
**free_trial_in_days** | **int** |  | [optional] 
**grace_period_in_days** | **int** |  | [optional] 
**custom_renewal_period** | **int** |  | [optional] 
**enable_automatic_renew** | **bool** |  | [optional] 
**enable_pro_rate_billing** | **bool** |  | [optional] 
**enable_usage_threshold** | **bool** |  | [optional] 
**enable_automatic_disable** | **bool** |  | [optional] 
**enable_automatic_payments** | **bool** |  | [optional] 
**usage_threshold** | **int** |  | [optional] 
**data** | **str** |  | [optional] 
**data_label** | **str** |  | [optional] 
**data1** | **str** |  | [optional] 
**data1_label** | **str** |  | [optional] 
**data2** | **str** |  | [optional] 
**data2_label** | **str** |  | [optional] 
**data3** | **str** |  | [optional] 
**data3_label** | **str** |  | [optional] 
**data4** | **str** |  | [optional] 
**data4_label** | **str** |  | [optional] 
**data5** | **str** |  | [optional] 
**data5_label** | **str** |  | [optional] 
**data6** | **str** |  | [optional] 
**data6_label** | **str** |  | [optional] 
**data7** | **str** |  | [optional] 
**data7_label** | **str** |  | [optional] 
**data8** | **str** |  | [optional] 
**data8_label** | **str** |  | [optional] 
**data9** | **str** |  | [optional] 
**data9_label** | **str** |  | [optional] 
**account_holder_id** | **str** |  | [optional] 
**individual_id** | **str** |  | [optional] 
**organization_id** | **str** |  | [optional] 
**receiver_business_id** | **str** |  | [optional] 
**business_id** | **str** |  | [optional] 
**business_profile_record_id** | **str** |  | [optional] 
**payment_token_id** | **str** |  | [optional] 
**wallet_account_id** | **str** |  | [optional] 
**security_certificate_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.support_entitlement_update_dto import SupportEntitlementUpdateDto

# TODO update the JSON string below
json = "{}"
# create an instance of SupportEntitlementUpdateDto from a JSON string
support_entitlement_update_dto_instance = SupportEntitlementUpdateDto.from_json(json)
# print the JSON string representation of the object
print(SupportEntitlementUpdateDto.to_json())

# convert the object into a dict
support_entitlement_update_dto_dict = support_entitlement_update_dto_instance.to_dict()
# create an instance of SupportEntitlementUpdateDto from a dict
support_entitlement_update_dto_from_dict = SupportEntitlementUpdateDto.from_dict(support_entitlement_update_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


