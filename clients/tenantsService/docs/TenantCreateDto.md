# TenantCreateDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] 
**name** | **str** |  | 
**legal_name** | **str** |  | [optional] 
**email** | **str** |  | 
**phone** | **str** |  | [optional] 
**web_url** | **str** |  | [optional] 
**handler** | **str** |  | [optional] 
**about** | **str** |  | [optional] 
**slogan** | **str** |  | [optional] 
**currency_id** | **str** |  | 
**duns** | **str** |  | [optional] 
**tax_id** | **str** |  | [optional] 
**avatar_url** | **str** |  | [optional] 
**country_id** | **str** |  | 
**state_id** | **str** |  | [optional] 
**city_id** | **str** |  | [optional] 
**language_id** | **str** |  | [optional] 
**timezone_id** | **str** |  | [optional] 
**business_type_id** | **str** |  | [optional] 
**business_segment_id** | **str** |  | [optional] 
**business_industry_id** | **str** |  | [optional] 
**business_size_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.tenant_create_dto import TenantCreateDto

# TODO update the JSON string below
json = "{}"
# create an instance of TenantCreateDto from a JSON string
tenant_create_dto_instance = TenantCreateDto.from_json(json)
# print the JSON string representation of the object
print(TenantCreateDto.to_json())

# convert the object into a dict
tenant_create_dto_dict = tenant_create_dto_instance.to_dict()
# create an instance of TenantCreateDto from a dict
tenant_create_dto_from_dict = TenantCreateDto.from_dict(tenant_create_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


