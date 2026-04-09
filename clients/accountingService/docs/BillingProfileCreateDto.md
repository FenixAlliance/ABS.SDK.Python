# BillingProfileCreateDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] 
**contact_id** | **str** |  | [optional] 
**tenant_id** | **str** |  | [optional] 
**tax_id** | **str** |  | 
**phone** | **str** |  | 
**email** | **str** |  | 
**address** | **str** |  | 
**address1** | **str** |  | [optional] 
**address2** | **str** |  | [optional] 
**postal_code** | **str** |  | 
**business_name** | **str** |  | 
**commercial_name** | **str** |  | 
**ticker** | **str** |  | [optional] 
**duns** | **str** |  | [optional] 
**is_public_company** | **bool** |  | [optional] 
**is_facta_customer** | **bool** |  | [optional] 
**country_id** | **str** |  | 
**state_id** | **str** |  | 
**city_id** | **str** |  | 
**fiscal_identification_type_id** | **str** |  | 
**fiscal_authority_id** | **str** |  | 
**fiscal_regime_id** | **str** |  | 

## Example

```python
from openapi_client.models.billing_profile_create_dto import BillingProfileCreateDto

# TODO update the JSON string below
json = "{}"
# create an instance of BillingProfileCreateDto from a JSON string
billing_profile_create_dto_instance = BillingProfileCreateDto.from_json(json)
# print the JSON string representation of the object
print(BillingProfileCreateDto.to_json())

# convert the object into a dict
billing_profile_create_dto_dict = billing_profile_create_dto_instance.to_dict()
# create an instance of BillingProfileCreateDto from a dict
billing_profile_create_dto_from_dict = BillingProfileCreateDto.from_dict(billing_profile_create_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


