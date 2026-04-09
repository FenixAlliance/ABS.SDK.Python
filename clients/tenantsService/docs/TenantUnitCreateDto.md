# TenantUnitCreateDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] 
**business_id** | **str** |  | [optional] 
**business_profile_record_id** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**disabled** | **bool** |  | [optional] 
**business_unit_qualified_name** | **str** |  | [optional] 
**country_id** | **str** |  | [optional] 
**organization_profile_id** | **str** |  | [optional] 
**parent_business_unit_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.tenant_unit_create_dto import TenantUnitCreateDto

# TODO update the JSON string below
json = "{}"
# create an instance of TenantUnitCreateDto from a JSON string
tenant_unit_create_dto_instance = TenantUnitCreateDto.from_json(json)
# print the JSON string representation of the object
print(TenantUnitCreateDto.to_json())

# convert the object into a dict
tenant_unit_create_dto_dict = tenant_unit_create_dto_instance.to_dict()
# create an instance of TenantUnitCreateDto from a dict
tenant_unit_create_dto_from_dict = TenantUnitCreateDto.from_dict(tenant_unit_create_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


