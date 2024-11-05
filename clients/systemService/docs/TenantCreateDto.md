# TenantCreateDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] [readonly] 
**timestamp** | **datetime** |  | [optional] [readonly] 
**duns** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**legal_name** | **str** |  | [optional] 
**email** | **str** |  | [optional] 
**phone** | **str** |  | [optional] 
**web_url** | **str** |  | [optional] 
**about** | **str** |  | [optional] 
**handler** | **str** |  | [optional] 
**currency_id** | **str** |  | [optional] 
**language_id** | **str** |  | [optional] 
**timezone_id** | **str** |  | [optional] 
**city_id** | **str** |  | [optional] 
**state_id** | **str** |  | [optional] 
**country_id** | **str** |  | [optional] 
**tax_id** | **str** |  | [optional] 
**avatar_url** | **str** |  | [optional] 

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


