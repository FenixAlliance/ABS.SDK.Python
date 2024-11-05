# TenantUpdateDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**duns** | **str** |  | [optional] 
**slogan** | **str** |  | [optional] 
**legal_name** | **str** |  | [optional] 
**phone** | **str** |  | [optional] 
**web_url** | **str** |  | [optional] 
**twitter_username** | **str** |  | [optional] 
**facebook_url** | **str** |  | [optional] 
**twitter_url** | **str** |  | [optional] 
**git_hub_url** | **str** |  | [optional] 
**linked_in_url** | **str** |  | [optional] 
**instagram_url** | **str** |  | [optional] 
**you_tube_url** | **str** |  | [optional] 
**whats_app_number** | **str** |  | [optional] 
**support_phone_number** | **str** |  | [optional] 
**tax_id** | **str** |  | [optional] 
**about** | **str** |  | [optional] 
**currency_id** | **str** |  | [optional] 
**timezone_id** | **str** |  | [optional] 
**language_id** | **str** |  | [optional] 
**country_id** | **str** |  | [optional] 
**state_id** | **str** |  | [optional] 
**city_id** | **str** |  | [optional] 
**email** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.tenant_update_dto import TenantUpdateDto

# TODO update the JSON string below
json = "{}"
# create an instance of TenantUpdateDto from a JSON string
tenant_update_dto_instance = TenantUpdateDto.from_json(json)
# print the JSON string representation of the object
print(TenantUpdateDto.to_json())

# convert the object into a dict
tenant_update_dto_dict = tenant_update_dto_instance.to_dict()
# create an instance of TenantUpdateDto from a dict
tenant_update_dto_from_dict = TenantUpdateDto.from_dict(tenant_update_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


