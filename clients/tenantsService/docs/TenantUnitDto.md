# TenantUnitDto


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
from openapi_client.models.tenant_unit_dto import TenantUnitDto

# TODO update the JSON string below
json = "{}"
# create an instance of TenantUnitDto from a JSON string
tenant_unit_dto_instance = TenantUnitDto.from_json(json)
# print the JSON string representation of the object
print(TenantUnitDto.to_json())

# convert the object into a dict
tenant_unit_dto_dict = tenant_unit_dto_instance.to_dict()
# create an instance of TenantUnitDto from a dict
tenant_unit_dto_from_dict = TenantUnitDto.from_dict(tenant_unit_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


