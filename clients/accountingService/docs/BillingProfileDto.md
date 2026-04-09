# BillingProfileDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] 
**tenant_id** | **str** |  | [optional] 
**contact_id** | **str** |  | [optional] 
**enrollment_id** | **str** |  | [optional] 
**about** | **str** |  | [optional] 
**verified** | **bool** |  | [optional] 
**submitted** | **bool** |  | [optional] 
**avatar_url** | **str** |  | [optional] 
**qualified_name** | **str** |  | [optional] 
**verification_timestamp** | **datetime** |  | [optional] 
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
**tax_id** | **str** |  | 
**email** | **str** |  | 
**phone** | **str** |  | [optional] 
**address** | **str** |  | [optional] 
**address1** | **str** |  | [optional] 
**address2** | **str** |  | [optional] 
**postal_code** | **str** |  | [optional] 
**business_name** | **str** |  | [optional] 
**commercial_name** | **str** |  | [optional] 
**ticker** | **str** |  | [optional] 
**duns** | **str** |  | [optional] 
**is_public_company** | **bool** |  | [optional] 
**is_facta_customer** | **bool** |  | [optional] 
**tax_payer_type** | **str** |  | [optional] 
**country_id** | **str** |  | 
**state_id** | **str** |  | [optional] 
**city_id** | **str** |  | [optional] 
**fiscal_identification_type_id** | **str** |  | [optional] 
**fiscal_authority_id** | **str** |  | [optional] 
**fiscal_regime_id** | **str** |  | [optional] 
**contact_name** | **str** |  | [optional] 
**fiscal_authority_name** | **str** |  | [optional] 
**country_name** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.billing_profile_dto import BillingProfileDto

# TODO update the JSON string below
json = "{}"
# create an instance of BillingProfileDto from a JSON string
billing_profile_dto_instance = BillingProfileDto.from_json(json)
# print the JSON string representation of the object
print(BillingProfileDto.to_json())

# convert the object into a dict
billing_profile_dto_dict = billing_profile_dto_instance.to_dict()
# create an instance of BillingProfileDto from a dict
billing_profile_dto_from_dict = BillingProfileDto.from_dict(billing_profile_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


