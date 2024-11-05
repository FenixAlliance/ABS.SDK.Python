# ExtendedTenantDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] 
**qualified_name** | **str** |  | [optional] [readonly] 
**tax_id** | **str** |  | [optional] 
**about** | **str** |  | [optional] 
**wallet_id** | **str** |  | [optional] 
**social_feed_id** | **str** |  | [optional] 
**business_industry_id** | **str** |  | [optional] 
**business_segment_id** | **str** |  | [optional] 
**social_profile_id** | **str** |  | [optional] 
**language_id** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**duns** | **str** |  | [optional] 
**slogan** | **str** |  | [optional] 
**legal_name** | **str** |  | [optional] 
**cover_url** | **str** |  | [optional] 
**avatar_url** | **str** |  | [optional] 
**cart_id** | **str** |  | [optional] 
**currency_id** | **str** |  | [optional] 
**timezone_id** | **str** |  | [optional] 
**country_id** | **str** |  | [optional] 
**state_id** | **str** |  | [optional] 
**city_id** | **str** |  | [optional] 
**email** | **str** |  | [optional] 
**phone** | **str** |  | [optional] 
**web_url** | **str** |  | [optional] 
**facebook_url** | **str** |  | [optional] 
**twitter_url** | **str** |  | [optional] 
**git_hub_url** | **str** |  | [optional] 
**linked_in_url** | **str** |  | [optional] 
**instagram_url** | **str** |  | [optional] 
**you_tube_url** | **str** |  | [optional] 
**whats_app_number** | **str** |  | [optional] 
**support_phone_number** | **str** |  | [optional] 
**verified** | **bool** |  | [optional] 
**business_name** | **str** |  | [optional] [readonly] 
**business_legal_name** | **str** |  | [optional] [readonly] 
**twitter_username** | **str** |  | [optional] 
**cart** | [**CartDto**](CartDto.md) |  | [optional] 
**wallet** | [**WalletDto**](WalletDto.md) |  | [optional] 
**social_profile** | [**SocialProfileDto**](SocialProfileDto.md) |  | [optional] 

## Example

```python
from openapi_client.models.extended_tenant_dto import ExtendedTenantDto

# TODO update the JSON string below
json = "{}"
# create an instance of ExtendedTenantDto from a JSON string
extended_tenant_dto_instance = ExtendedTenantDto.from_json(json)
# print the JSON string representation of the object
print(ExtendedTenantDto.to_json())

# convert the object into a dict
extended_tenant_dto_dict = extended_tenant_dto_instance.to_dict()
# create an instance of ExtendedTenantDto from a dict
extended_tenant_dto_from_dict = ExtendedTenantDto.from_dict(extended_tenant_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


