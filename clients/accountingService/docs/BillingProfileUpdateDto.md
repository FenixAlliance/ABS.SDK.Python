# BillingProfileUpdateDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**contact_id** | **str** |  | [optional] 
**tax_id** | **str** |  | [optional] 
**phone** | **str** |  | [optional] 
**email** | **str** |  | [optional] 
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
**country_id** | **str** |  | [optional] 
**state_id** | **str** |  | [optional] 
**city_id** | **str** |  | [optional] 
**fiscal_identification_type_id** | **str** |  | [optional] 
**fiscal_authority_id** | **str** |  | [optional] 
**fiscal_regime_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.billing_profile_update_dto import BillingProfileUpdateDto

# TODO update the JSON string below
json = "{}"
# create an instance of BillingProfileUpdateDto from a JSON string
billing_profile_update_dto_instance = BillingProfileUpdateDto.from_json(json)
# print the JSON string representation of the object
print(BillingProfileUpdateDto.to_json())

# convert the object into a dict
billing_profile_update_dto_dict = billing_profile_update_dto_instance.to_dict()
# create an instance of BillingProfileUpdateDto from a dict
billing_profile_update_dto_from_dict = BillingProfileUpdateDto.from_dict(billing_profile_update_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


